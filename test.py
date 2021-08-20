from app import app
import requests
from queue import Queue
from bs4 import BeautifulSoup
from services import get_page, get_reviews
import unittest

class Test(unittest.TestCase):
    #Check for response code 200
    def test_search(self):
        tester = app.test_client(self)
        response = tester.get("/1st-heritage-credit/90918362")
        _statuscode = response.status_code
        self.assertEqual(_statuscode, 200)

    #Check for response code 400
    def test_search_fail(self):
        tester = app.test_client(self)

        response = tester.get("/reviews/1st-heritage-credit/90918362")
        _statuscode = response.status_code
        self.assertEqual(_statuscode, 404)

        response2 = tester.get("/1st-hcredit/962")
        _statuscode2 = response2.status_code
        self.assertEqual(_statuscode2, 400)

    #Check for json return data
    def test_search_content(self):
        tester = app.test_client(self)
        response = tester.get("/1st-heritage-credit/90918362")
        self.assertEqual(response.content_type, "application/json")

    #Check get_page function
    def test_get_page(self):
        url = "https://www.lendingtree.com/reviews/personal/1st-heritage-credit/90918362"
        page = get_page(url, Queue())
        self.assertIsInstance(page, BeautifulSoup)

    #Check get_reviews function
    def test_get_reviews(self):
        url = "https://www.lendingtree.com/reviews/personal/1st-heritage-credit/90918362"
        page = get_page(url, Queue())
        actual = get_reviews(page, Queue())
        expected = [{'lender': '1st Heritage Credit', 'title': 'Great company that will work with you and your situation!', 'content': "I have family that you guys have helped out and others I've heard about as well, whether I'm approved or not you guys really make people want to come back.", 'author': 'Ethan', 'location': 'Murfreesboro,  TN', 'rating': 5.0, 'date': 'March 2020'}]
        self.assertEqual(actual, expected)

    #Check url parse threadig
    def test_url_threading(self):
        pass

    #Check page reviews content threading
    def test_page_reviews(self):
        pass


if __name__ == '__main__':
    unittest.main()