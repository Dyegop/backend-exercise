"""
The test task is pretty simple: You need to create an API (only one endpoint like /data) with content negotiation which
answers with text/html and application/json (depending the header content-type) and this endpoint needs to have
pagination. So if you add a special query argument to the endpoint (up to you what are they), you can get the next
iteration of data and so on until the end of the "dataset".

Concerns:
    -The text/html version needs to be so simple using Jinja2 engine and a simple HTML table with the data
    (no need for styling or JavaScript at all).
    -For the backend the micro-framework to be used is Flask and you can use all the libraries as you want for this
    little test task.
    -The database needs to be ElasticSearch and it is up to you how to save the data, the used mapping for the
    documents, etc.
    -CSV sample data columns: id, inventory name, contact name, stock, last revenue, current revenue, refund,
    company name, categories, rating
    -Max items per scroll = 20. CSV has 5000 rows so you can do 250 scrolls.
    -Unittests could be included, are not mandatory but it would be great to see something about this.
    -The code needs to be uploaded to a git repository using gitflow if it is possible (use the SaaS that you prefer,
    Github, Gitlab, Bitbucket, etc) and share with me the URL when you finish.
"""

from flask import Flask



app = Flask(__name__)


@app.route('/')
def home():
    pass


@app.route('/data/<int:page>')
def data(page):
    """API route"""
    pass





# Run application
if __name__ == '__main__':
    app.run(port=5000, debug=True)