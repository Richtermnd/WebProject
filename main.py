from flask import Flask, url_for, render_template, redirect
from forms import LoginForm

app = Flask(__name__)
# S - safety
app.config['SECRET_KEY'] = 'SECRET_KEY'


@app.route('/messanger')
def messanger():
    return render_template('messanger.html', title='Messanger')


@app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.data)
        return redirect('/')
    return render_template('login.html', title='Login', form=form)


@app.route('/<user_id>')
def user_page(user_id):
    return render_template('user_page.html', title='My page')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='index')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
