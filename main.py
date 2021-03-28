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


@app.route('/list_prof/<list>')
def list_prof(list):
    param = {}
    param['list'] = list
    param['l1'] = ['инженер', 'программист', 'пилот', 'гений', 'не гуманитарий', 'ладно гуманитарий тоже', 'шут', 'марсианин']
    return render_template('prof_list.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
