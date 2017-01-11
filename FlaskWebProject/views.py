import os
from datetime import datetime
from flask import render_template,url_for,request,redirect,session,flash
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
    
@app.route('/contact')
def contact():
    """Renders the home page."""
    return render_template(
        'contact.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the home page."""
    return render_template(
        'about.html',
        title='Home Page',
        year=datetime.now().year,
    )
