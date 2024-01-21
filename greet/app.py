from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
        <html>
            <body>
                <h1>Home Page</h1>
                <p>Welcome to my digital tree fort!</p>
                <a href='/hello'>Go to hello</a>
            </body>
        </html>
    """
    return html

@app.route('/welcome')
def welcome():
    html = """
    welcome
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    welcome home
    """
    return html

@app.route('/welcome/back')
def welcome_back():
    html = """
    welcome back
    """
    return html