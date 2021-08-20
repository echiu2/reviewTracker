from flask import Flask, jsonify, request
import requests
import json
from services import get_page, get_reviews

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():

    # If request is a POST request
    if request.method == 'POST':
        root = str(request.form.get('root'))
        if root != '':
            page_list = []
            curr_page = 1

        page = get_page(root)
        # max_page = int(page.find('a', {'class': 'pageNum'}).text)

        while curr_page <= 10:
            url = root + '?pid=' + str(curr_page)
            page_id = get_page(url)
            review_url = {
                'id': str(curr_page),
                'reviews': get_reviews(page_id),
            }
            page_list.append(review_url) 
            curr_page += 1

        return jsonify(page_list)

    # otherwise handle the GET request
    return '''
           <form method="POST">
               <div><label>Please input the Lender's url: <input type="text" name="root"></label><input type="submit" value="Submit"></div>
           </form>'''

if __name__ == "__main__":
    app.run(debug=True)