from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/messanger')
def messanger():
    return render_template('messanger.html', title='Messanger')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
