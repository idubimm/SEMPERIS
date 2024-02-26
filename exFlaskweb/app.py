from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'your-secret-key'

class User(UserMixin):
    def __init__(self, id):
        self.id = id
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    user = User(request.form['username'])
    login_user(user)
    return redirect(url_for('success'))

@app.route('/success')
@login_required
def success():
    return render_template('success.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)