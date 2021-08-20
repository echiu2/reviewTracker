# reviewTracker

**************
# Overview

A flask app that takes in an url and returns the json content of all reviews of the lender

Example valid URL: http://127.0.0.1:5000/1st-heritage-credit/90918362 or http://127.0.0.1:5000/first-midwest-bank/52903183

***************
# How to run:

1. Clone Repository by running command: ```git clone <repository>```
2. Install Python3 into local machine: https://www.python.org/downloads/ or run ```brew install python3``` on Macos if you have brew installed. 
3. Create a virtual environment for the project folder by running this command: ```python3 -m venv <myenvname>``` or ```py -m venv <myenvname>```.
4. Once you have your virtual environment created, activate virtual env by running: ```source /<myenvname>/bin/activate``` in terminal or ```<myenvname>\Scripts\activate``` on windows cmd.
5. Download dependencies in the requirement.txt file by running this command: ```pip3 install -r requirements.txt```
6. Run application api service application by running ```python3 app.py``` and run test application by running ```python3 test.py```.
7. Finally, go your browser and type http://127.0.0.1:5000/<lender_name>/<int:lender_id> in the address field.

****************
# Future Consideration:

1. Make application more Restful by creating POST or GET requests methods
2. Tried several ways to optimize the speed in which the application parses web pages and get their contents; added some multithreading but still took sometimes over
a minute to get all requests.
3. Saving already searched urls or requests into a database or some kind of memcache to efficiently optimize speed

