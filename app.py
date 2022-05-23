from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/meatandfish')
def meatandfish():  # put application's code here
    return render_template('meatandfish.html')


@app.route('/fruitandveg')
def fruitandveg():  # put application's code here
    return render_template('fruitandveg.html')


if __name__ == '__main__':
    app.run(debug=True)