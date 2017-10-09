from flask import Flask, render_template, request, session, redirect, url_for
import os

login_app = Flask(__name__)
login_app.secret_key = os.urandom(16)

good_user = "bob"
good_pass = "password"
user_error_msg = "Username is incorrect\n"
pass_error_msg = "Password is incorrect\n"

@login_app.route("/", methods=['POST', 'GET'])
def root():
    if "user" in session:
        return render_template('welcome.html')
    return render_template('login.html')

@login_app.route("/welcome", methods=['POST', 'GET'])
def welcome():
    user_inp = request.form["username"]
    pass_inp = request.form["password"]
    
    if good_user == user_inp and good_pass == pass_inp:
        session['user'] = user_inp
        session['pass'] = pass_inp
        return render_template('welcome.html')
    elif good_user != user_inp and good_pass != pass_inp:
        return render_template('login.html', user_error=user_error_msg, pass_error=pass_error_msg)
    elif good_user != user_inp:
        return render_template('login.html', user_error=user_error_msg)
    elif good_pass != pass_inp:
        return render_template('login.html', pass_error=pass_error_msg)
    
    return render_template('login.html')

@login_app.route("/logout", methods=['POST', 'GET'])
def logout():
    session.pop("user")
    session.pop("pass")
    return redirect(url_for('root'))

if __name__ == '__main__':
    
    login_app.debug = True
    login_app.run()
