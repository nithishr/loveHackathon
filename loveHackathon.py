#!/usr/bin/env python3
from flask import Flask, render_template, redirect, session, url_for, request, render_template_string

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    if 'username' in session:
        return render_template_string('##Home {{name}}', name='admin')
    else:    
        return render_template_string('#Home {{name}}', name='admin')

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        needed_info = ['username', 'password', 'sex', 'fullAge', 'partner']
        found_required_info = True
        for info in needed_info:
            if info not in request.form:
                found_required_info = False
        if found_required_info:
            # go on with the questions
            pass
        else:
            return redirect(url_for('register'))
    return render_template('register.html', error=error)


if __name__ == '__main__':
    app.config["SECRET_KEY"] = "ITSASECRET"
    app.run(host='0.0.0.0', debug=True)
