# -*- encoding: utf-8 -*-
from flask import render_template
from repositories.expense import ExpenseRepository


@app.route('/')
def index:
    return render_template('index.html')


@app.route('/expenses/<company_id>')
def show(company_id=None):
    return render_template('index.html', company_id=None)
