from flask import Flask, url_for, render_template
from flask.ext.pymongo import PyMongo


app = Flask(__name__)
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

# example url taking a variable
@app.route('/about/<username>')
def about_user(username):
    return 'About %s' % username

# example url taking a variable as an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %s' % post_id


if __name__ == '__main__':
    app.run(debug=True)
