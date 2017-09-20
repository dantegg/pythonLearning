from flask import Flask, session, redirect, url_for, escape, request, render_template
from datetime import timedelta

app = Flask(__name__)

@app.before_request
def make_session_permanent():
    print(request.path)
    if request.path != '/':
        if not request.path == '/login':
            if not 'username' in session:
                return redirect(url_for('welcome'))
        

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    print('session', session)
    if session == {}:
        return redirect(url_for('welcome'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    print('request', request)
    if request.method == 'POST':
        print('request', request.form['username'])
        session['username'] = request.form['username']
        session.permanent = True
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    print('session', session == {})
    # session.pop('username', None)    
    return 'haha'
    # return redirect(url_for('welcome'))
# set the secret key.
app.secret_key = 'Yyt1109Lxy123!*(qwert'
app.permanent_session_lifetime = timedelta(minutes = 5)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)