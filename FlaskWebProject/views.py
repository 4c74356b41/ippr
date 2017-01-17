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
        year=datetime.now().year
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='Об институте',
        year=datetime.now().year
    )

@app.route('/history')
def history():
    return render_template(
        'history.html',
        title='История участия в избирательных кампаниях',
        year=datetime.now().year
    )

@app.route('/media')
def media():
    return render_template(
        'media.html',
        title='Издания института',
        year=datetime.now().year
    )

@app.route('/jobs')
def jobs():
    return render_template(
        'jobs.html',
        title='Вакансии',
        year=datetime.now().year
    )

@app.route('/specials')
def specials():
    return render_template(
        'specials.html',
        title='Специальные технологии',
        year=datetime.now().year
    )

@app.route('/follow')
def follow():
    return render_template(
        'follow.html',
        title='Юридическое Сопровождение',
        year=datetime.now().year
    )

@app.route('/control')
def control():
    return render_template(
        'control.html',
        title='Организация контроля за ходом голосовования и подсчетом голосов',
        year=datetime.now().year
    )

@app.route('/elections')
def elections():
    return render_template(
        'elections.html',
        title='Организация выборов',
        year=datetime.now().year
    )

@app.route('/pravo')
def pravo():
    return render_template(
        'pravo.html',
        title='Нормативные акты о выборах',
        year=datetime.now().year
    )

@app.route('/zakon')
def zakon():
    return render_template(
        'zakon.html',
        title='Разработка и правовая экспертиза законопроектов',
        year=datetime.now().year
    )

@app.route('/material')
def material():
    return render_template(
        'material.html',
        title='Методические материалы для избирательных кампаний',
        year=datetime.now().year
    )

@app.route('/archive')
def archive():
    return render_template(
        'archive.html',
        title='Архив',
        year=datetime.now().year
    )

@app.route('/team')
def team():
    return render_template(
        'team.html',
        title='Команда Института Парламентаризма',
        year=datetime.now().year
    )

@app.route('/shablon')
def shablon():
    return render_template(
        'shablon.html',
        title='Учебные курсы',
        year=datetime.now().year
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='Учебные курсы', year=datetime.now().year), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html', title='Учебные курсы', year=datetime.now().year), 500
