# Set the path
import os, sys
from flask import Flask, url_for, render_template
from flask.ext.script import Manager, Server
from cardbox import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

# example url taking a variable
@app.route('/about/<username>')
def about_user(username):
    return 'About %s' % username

# example url taking a variable as an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %s' % post_id


# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

if __name__ == "__main__":
    manager.run()