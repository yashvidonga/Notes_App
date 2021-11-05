from flask import Flask, render_template, request, redirect, flash
from modelapp import Users, db, Contact, Notes

app = Flask(__name__, template_folder='templates')
app.secret_key = 'super secret key'


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email_id = request.form['email']
        password1 = request.form['password']
        check_email = Users.query.filter_by(email=email_id).first()
        if check_email is not None and check_email.password == password1:
            success = 'Login SUCCESSFUL'
            return render_template('notes.html')
        else:
            error = 'Login NOT successful!'
            # print(list(Users.query.order_by(Users.email).first()))
            return render_template('Login.html', error=error)
    else:
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
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        else:
            error = 'Error: Incorrect Password'
            # print(list(Users.query.order_by(Users.email).first()))
            return render_template('SignUp.html', error=error)

    else:
        return render_template('SignUp.html')


@app.route('/notes')
def notes():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        new_note = Notes(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return render_template('notes.html', saved=True)
    else:
        return render_template('notes.html', saved=False)

    return render_template('homepage.html')

# @app.route('/home')
# def home():
#     return "<h1>Welcome to the Home Page</h1>"


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        email_id = request.form['email']
        name1 = request.form['name']
        message1 = request.form['message']
        new_message = Contact(name=name1, email=email_id, message=message1)
        flash('Message Sunday!')
        db.session.add(new_message)
        db.session.commit()
        return redirect('/')

    else:
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
