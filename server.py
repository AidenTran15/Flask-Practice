from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/works.html')
def works():
    return render_template('works.html')