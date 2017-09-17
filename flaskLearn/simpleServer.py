from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')
@app.route('/home')
def home():
    if session == {}:
        return redirect(url_for('welcome'))
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('request', request.form['username'])
        session['username'] = request.form['username']
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    print('session', session == {})
    # session.pop('username', None)    
    return 'haha'
    # return redirect(url_for('welcome'))
# set the secret key.
app.secret_key = 'Yyt1109Lxy123!*(qwert'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)