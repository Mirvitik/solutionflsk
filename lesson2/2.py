from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'pluto_is_planet_and_cuba_is_free'


@app.route('/index/<username>')
def news(username):
    return render_template('index.html', title=username)


@app.route('/training/<username>')
def image(username):
    return render_template('training.html', title=username)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')