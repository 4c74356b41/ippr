"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Институт парламентаризма',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Институт парламентаризма',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Институт парламентаризма',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/history')
def history():
    return '200'

@app.route('/media')
def media():
    return '200'

@app.route('/jobs')
def jobs():
    return '200'

@app.route('/service')
def service():
    return '200'

@app.route('/pravo')
def pravo():
    return '200'

@app.route('/zakon')
def zakon():
    return '200'

@app.route('/material')
def material():
    return '200'

@app.route('/archive')
def archive():
    return '200'
