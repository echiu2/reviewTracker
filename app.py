from flask import Flask, jsonify, request
from threading import Thread
from queue import Queue
from services import find_max, get_page, get_reviews, url_threading, page_threading
from time import time

app = Flask(__name__)

# An example of a working url is http://127.0.0.1:5000/1st-heritage-credit/90918362
@app.route('/<lender_name>/<int:lender_id>')
def search(lender_name, lender_id):
    try:
        # Create the url that we are making the request for
        root_url = 'https://www.lendingtree.com/reviews/personal/' + lender_name + '/' + str(lender_id)

        # Parsing root pages html with beautiful soup
        # page = find_max(root_url)

        max_page = get_page(root_url, Queue())

        max_pages = int(max_page.find('a', {'class': 'pageNum'}).text)
        urls = []

        for i in range(1, max_pages+1):
            url = root_url + '?pid=' + str(i)
            urls.append(url)

        # Executing threading for multiple page parsing
        page = page_threading(urls)

        # Executing threading for multiple pages reviews
        res = url_threading(page)

        return jsonify(res), 200

    except:
        return "Invalid URL. Please type in a valid URL or make sure URL is in correct format", 400

if __name__ == "__main__":
    app.run(debug=True)