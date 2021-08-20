from flask import Flask, jsonify, request
from threading import Thread
from queue import Queue
from services import get_page, get_reviews, url_threading
from time import time

app = Flask(__name__)

# An example of a working url is http://127.0.0.1:5000/first-midwest-bank/52903183
@app.route('/<lender_name>/<int:lender_id>')
def search(lender_name, lender_id):
    lender_name = lender_name
    lender_id = lender_id
    try:
        # Create the url that we are making the request for
        root_url = 'https://www.lendingtree.com/reviews/personal/' + lender_name + '/' + str(lender_id) + '/'
        print(root_url)
        # Parsing root pages html with beautiful soup
        page = get_page(root_url)

        #Check for invalid urls
        if page == "Url is invalid or does not exist!":
            return "Invalid url: Please try again", 400

        max_pages = int(page.find('a', {'class': 'pageNum'}).text)
        urls = []

        #Create url for root url existing paginations
        for i in range(1, max_pages+1):
            url = root_url + '?pid=' + str(i)
            urls.append(get_page(url))

        # Executing threading for multiple pages reviews
        res = url_threading(urls)

        return jsonify(res), 200

    except:
        return "Invalid URL Parameters"


if __name__ == "__main__":
    app.run(debug=True)