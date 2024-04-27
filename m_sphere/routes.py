from flask import render_template
from m_sphere import app, db
from m_sphere.models import User, Group, Product, Account


@app.route('/')
def home():
    return render_template('base.html')