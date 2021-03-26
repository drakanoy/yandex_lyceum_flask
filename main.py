from flask import Flask
from flask import render_template, url_for, request, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/training/<prof>')
def prof(prof):
    param = {}
    param['prof'] = prof
    param['img1'] = url_for('static', filename='img/cor1.png')
    param['img2'] = url_for('static', filename='img/cor2.png')
    return render_template('prof.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
