from flask import render_template
from m_sphere import app, db


@app.route('/')
def home():
    return render_template('base.html')