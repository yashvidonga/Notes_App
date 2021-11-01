from flask import Flask, render_template, request, redirect, flash
from modelapp import Users, db
# from werkzeug.utils import redirect

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login')
def login():
    return render_template('Login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email_id = request.form['email']
        password1 = request.form['password']
        password_copy = request.form['cpassword']
        if password_copy == password1 and len(password1) > 8:
            new_user = Users(email=email_id, password=password1)
            flash('Account Created Successfully')
            try:
                db.session.add(new_user)
                db.session.commit()
                return redirect('/')
            except:
                return 'Database Issue'

        else:
            error = 'Error: Incorrect Password'
            return render_template('SignUp.html', error=error)

    else:
        return render_template('SignUp.html')


@app.route('/notes')
def notes():
    return render_template('notes.html')

# @app.route('/home')
# def home():
#     return "<h1>Welcome to the Home Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)
