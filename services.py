from bs4 import BeautifulSoup, SoupStrainer
import requests
import cchardet
import lxml
import time
import json

session = requests.Session()

# Using beautiful soup to get all html data from the url 
def get_page(url):
    try:
        response = session.get(url)
        page = BeautifulSoup(response.text, 'lxml')
        return page.select('.reviewTitle')
    except:
        return "Url is invalid or does not exist!"


for i in range(499):
    url = "https://www.lendingtree.com/reviews/personal/onemain-financial-inc/291320?pid={}".format(str(i))
    print(get_page(url))

# # parsing the url html content to get all the reviews
# def get_reviews(page):
#     main_reviews = page.find_all('div', {'class': 'col-xs-12 mainReviews'})
#     hidden_reviews = page.find_all('div', {'class': 'col-xs-12 mainReviews hiddenReviews'})
#     all_reviews = main_reviews + hidden_reviews
#     print(all_reviews)
#     reviews = []

#     for review in all_reviews:
#         consumer_info = review.find('p',{'class': 'consumerName'}).text.strip().replace('                                                                       ','').split(' ')
#         review_content ={
#         'lender': page.title.text.replace(' – Personal Loan Company Reviews | LendingTree',''),
#         'title' : review.find('p',{'class': 'reviewTitle'}).text.strip(),
#         'content' : review.find('p',{'class': 'reviewText'}).text.strip(),
#         'author' : consumer_info[0],
#         'location': ' '.join(consumer_info[2:]),
#         'rating' : float(review.find('div',{'class': 'numRec'}).text.replace(' of 5)stars','').replace('(','').strip()),
#         'date' : review.find('p',{'class': 'consumerReviewDate'}).text.replace('Reviewed in ','').strip(),
#         }
#         reviews.append(review_content)
    
#     return reviews


    
