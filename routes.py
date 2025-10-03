from flask import Flask , render_template , redirect , url_for , session , request
from .models import BlogPost , BlogUser
from .forms import RegistrationForm , LoginForm 
from . import db , create_app

def register_app(app):

    @app.route("/")
    def home():
        
        return render_template("home.html")
    
    @app.route("/registration.html" ,methods = ['GET' , "POST"])
    def registration():
        form = RegistrationForm()
        if form.validate_on_submit():
            new_registration = BlogUser(
               username = form.username.data,
                password = form.password.data,
               

            )
            db.session.add(new_registration)
            db.session.commit()

            return redirect(url_for('home'))
        return render_template("registration.html", form = form)
        


    @app.route('/create_post.html',   methods = ["GET" , "POST"] )
    def create():
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            

            new_post = BlogPost(title=title, content=content)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('home'))  # after saving, go back to home page
    
        return render_template('create_post.html')


    @app.route('/post.html')
    def display_post():
        posts = BlogPost.query.order_by(BlogPost.date_created.desc()).all()
        return render_template('post.html', posts=posts)

    @app.route('/delete')
    def delete():
        pass
    @app.route('/login.html' , methods = ['GET' , "POST"])
    def login():
        form = LoginForm()
        # if form.validate_on_submit():
        #     new_login = RegistrationForm(
        #         form.username.data,
        #         form.password.data,
        #         form.submit.data

        #     )
        #     db.session.add(new_login)

        #     return redirect(url_for('post'))
        return render_template('login.html', form = form)
    @app.route('/logout')
    def logout():
        pass