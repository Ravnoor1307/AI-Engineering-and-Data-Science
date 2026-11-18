from pathlib import Path
import os

from flask import Flask, render_template, request, redirect, url_for, session

from db import Database
from nlp_tools import (
    keyword_extraction,
    language_detection,
    named_entity_recognition,
    question_answering,
    sentiment_analysis,
    text_classification,
    text_similarity,
    text_summarization,
)

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or os.urandom(32)
database = Database(Path(__file__).with_name('users.json'))

NLP_TOOLS = {
    'ner': {
        'title': 'Named Entity Recognition',
        'template': 'operations/ner.html',
        'fields': ('text',),
        'processor': named_entity_recognition.analyze,
    },
    'sentiment': {
        'title': 'Sentiment Analysis',
        'template': 'operations/sentiment.html',
        'fields': ('text',),
        'processor': sentiment_analysis.analyze,
    },
    'summarization': {
        'title': 'Text Summarization',
        'template': 'operations/summarization.html',
        'fields': ('text',),
        'processor': text_summarization.summarize,
    },
    'keywords': {
        'title': 'Keyword Extraction',
        'template': 'operations/keywords.html',
        'fields': ('text',),
        'processor': keyword_extraction.extract,
    },
    'classification': {
        'title': 'Text Classification',
        'template': 'operations/classification.html',
        'fields': ('text',),
        'processor': text_classification.classify,
    },
    'language': {
        'title': 'Language Detection',
        'template': 'operations/language.html',
        'fields': ('text',),
        'processor': language_detection.detect,
    },
    'question-answering': {
        'title': 'Question Answering',
        'template': 'operations/question_answering.html',
        'fields': ('text', 'question'),
        'processor': question_answering.answer,
    },
    'similarity': {
        'title': 'Text Similarity',
        'template': 'operations/similarity.html',
        'fields': ('first_text', 'second_text'),
        'processor': text_similarity.compare,
    },
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login():
    return render_template('login.html', message=request.args.get('message'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html', message=request.args.get('message'))

@app.route('/perform_signup', methods=['POST'])
def perform_signup():
    fullname = request.form.get('fullname', '').strip()
    email = request.form.get('email', '').strip().lower()
    password = request.form.get('password', '')
    confirm_password = request.form.get('confirm_password', '')

    if not fullname or not email or not password or not confirm_password:
        return render_template('signup.html', error='Please fill in all fields.')

    if len(password) < 8:
        return render_template('signup.html', error='Password must be at least 8 characters long.')

    if password != confirm_password:
        return render_template('signup.html', error='Passwords do not match.')

    if not database.add_user(email, password, fullname):
        return render_template('signup.html', error='An account with that email already exists.')

    return redirect(url_for('signup', message='Signup successful. Please proceed to login.'))

@app.route('/perform_login', methods=['POST'])
def perform_login():
    username = request.form.get('username', '').strip().lower()
    password = request.form.get('password', '')

    if not username or not password:
        return render_template('login.html', error='Please enter your email and password.')

    user = database.search_user(username)
    if user and database.validate_user(username, password):
        session['user_email'] = username
        return redirect(url_for('profile'))
    return render_template('login.html', error='Invalid email or password.')

@app.route('/profile')
def profile():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', tools=NLP_TOOLS)

@app.route('/nlp-operations')
def nlp_operations():
    if 'user_email' not in session:
        return redirect(url_for('login'))
    return render_template('nlp_operations.html', tools=NLP_TOOLS)

@app.route('/nlp/<operation>', methods=['GET', 'POST'])
def run_nlp_operation(operation):
    if 'user_email' not in session:
        return redirect(url_for('login'))

    tool = NLP_TOOLS.get(operation)
    if tool is None:
        return render_template('nlp_operations.html', tools=NLP_TOOLS), 404

    values = {field: '' for field in tool['fields']}
    result = None
    error = None
    if request.method == 'POST':
        values = {field: request.form.get(field, '').strip() for field in tool['fields']}
        if any(not value for value in values.values()):
            error = 'Please fill in all fields.'
        else:
            result = tool['processor'](**values)

    return render_template(
        tool['template'],
        title=tool['title'],
        values=values,
        result=result,
        error=error,
    )

@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')

if __name__ == '__main__':
    app.run(debug=True)