from flask import render_template, flash, redirect, url_for
from app import app_variable
from app.forms import LoginForm

@app_variable.route('/')
@app_variable.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'
        },
        {
            'author': {'username': 'Twotto'},
            'body': 'Tom Watts is so good at everything'
        }
    ]
    return render_template('index.html', title= 'Home', user=user, posts=posts)

@app_variable.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title = 'Sign In', form=form)




