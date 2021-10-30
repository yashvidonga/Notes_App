from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/signup')
def signup():
    return render_template('SignUp.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

# @app.route('/home')
# def home():
#     return "<h1>Welcome to the Home Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
