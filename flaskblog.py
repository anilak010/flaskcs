from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
=======
'''we now have to specify the URI of the database i.e. location of database.
For now lets use an SQLite db and set its location.
'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #this will create a site.db file in this directory
#with SQLite we can specify a relative path with 3 forward slashes and the URI

#now we need to create a database instance
db = SQLAlchemy(app)
'''The best thing about SQLAlchemy is that we can represent our database structure as classes
which are called models'''

'''Each class is going to be its own table in database'''
class User(db.Model):
    #now lets add columns to the table User
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg')
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy= True)
    '''Our post posts attribute has a relationship to the Post model
    the backref is similar to adding another column to Post model.
    What the back ref allows us to do is when we have a Post we can simply use
    the author attribute to get the User who created the Post.
    The lazy argument just defines when sqlalchemy loads the data from the database.
    So lazy= True means that sqlalchemy will load the data as necessary in one go.
    This is convenient bcoz with this relationship we will be able to simply use 
    this posts attribute to get all of the Post created by an individual user.
    Now notice that this is a relationship and not a Column so if we were to actually
    look at our actual db structure in some kind of sql client we wouldn't see
    this post column here. This is running an additional query in the background that
    will get all the Post the user has created'''
>>>>>>> 7088a2e6f366b5221be80dc7873fe96f001e79c7

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

<<<<<<< HEAD

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


=======
#Create a post class to hold our post
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False) 
    #user.id is lowercase coz we actually using the table name which is lower case
    #class names are automatically converted to lowercase by sqlalchemy
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

>>>>>>> 7088a2e6f366b5221be80dc7873fe96f001e79c7
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
