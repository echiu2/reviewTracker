from bs4 import BeautifulSoup, SoupStrainer
import requests
import time
from queue import Queue
from threading import Thread

session = requests.Session()

# Using beautiful soup to find max_page
def find_max(url):
    try:
        response = session.get(url)
        page = BeautifulSoup(response.text, 'lxml')
        return page
    except:
        return "Url is invalid or does not exist!"

# Using beautiful soup to get all html data from the url 
def get_page(url, queue):
    try:
        response = session.get(url)
        page = BeautifulSoup(response.text, 'lxml')
        queue.put(page)
        return page
    except:
        return "Url is invalid or does not exist!"

# parsing the url html content to get all the reviews
def get_reviews(page, queue):
    main_reviews = page.find_all('div', {'class': 'col-xs-12 mainReviews'})
    hidden_reviews = page.find_all('div', {'class': 'col-xs-12 mainReviews hiddenReviews'})
    all_reviews = main_reviews + hidden_reviews
    reviews = []

    for review in all_reviews:
        consumer_info = review.find('p',{'class': 'consumerName'}).text.strip().replace('                                                                       ','').split(' ')
        review_content ={
        'lender': page.title.text.replace(' – Personal Loan Company Reviews | LendingTree',''),
        'title' : review.find('p',{'class': 'reviewTitle'}).text.strip(),
        'content' : review.find('p',{'class': 'reviewText'}).text.strip(),
        'author' : consumer_info[0],
        'location': ' '.join(consumer_info[2:]),
        'rating' : float(review.find('div',{'class': 'numRec'}).text.replace(' of 5)stars','').replace('(','').strip()),
        'date' : review.find('p',{'class': 'consumerReviewDate'}).text.replace('Reviewed in ','').strip(),
        }
        reviews.append(review_content)
    
    queue.put(reviews)

    return reviews

# Threading function to get all content in the page
def url_threading(urls):
    all_threads = []
    all_results = []
    my_queue = Queue()

    for url in urls:
        t = Thread(target=get_reviews, args=(url, my_queue))
        t.start()
        all_threads.append(t)

    while len(all_results) < len(urls):
        data = my_queue.get()
        all_results.append(data)

    res = [item for item in all_results]

    return res

#Threading to get parse all paginated url
def page_threading(urls):
    all_threads = []
    all_results = []
    my_queue = Queue()

    for url in urls:
        t = Thread(target=get_page, args=(url, my_queue))
        t.start()
        all_threads.append(t)

    while len(all_results) < len(urls):
        data = my_queue.get()
        all_results.append(data)

    res = [item for item in all_results]

    return res



    
