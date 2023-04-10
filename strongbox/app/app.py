import flask
from flask import render_template, redirect, request, url_for
from flask import session

import auth
from config import configs
import store

app = flask.Flask(__name__)


def enable_debug():
    from werkzeug.debug import DebuggedApplication
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
    app.debug = True


def configure():
    app.config['SECRET_KEY'] = configs['SECRET_KEY']
    enable_debug()


def register_routes():
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login_view():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if auth.check_login(username, password) == 0:
                session['username'] = username
                return redirect(url_for('store_view'))
            else:
                return render_template('login.html', error='Wrong username or password')

    @app.route('/logout')
    def logout():
        if 'username' in session:
            session.clear()
        return redirect(url_for('index'))

    @app.route('/store')
    def store_view():
        if 'username' in session:
            passwords = auth.get_passwords(session['username'])
            return render_template('store/store.html', len=len(passwords), passwords=passwords)
        return redirect(url_for('login_view'))

    @app.route('/register', methods=['GET', 'POST'])
    def register_view():
        if request.method == 'GET':
            return render_template('register.html')
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            check = auth.check_register(username, password)
            if check == 0:

                return redirect(url_for('login_view'))
            else:
                return render_template('register.html', error=check)
        return 'Error'

    @app.route('/store/add', methods=['POST'])
    def add_password():
        if 'username' in session:
            current_user = session['username']
            site = request.form['site']
            user = request.form['username']
            password = request.form['password']
            error = store.add_password(current_user, site, user, password)
            if error == 0:
                return redirect('/store')
            return error
        return "Error"

    @app.route('/store/delete')
    def del_password():
        if 'username' in session:
            password_id = request.args.get('password_id')
            error = store.del_password(password_id)
            print(error)
            if error == 0:
                return redirect('/store')
            return error
        return "Error"

    @app.route('/store/export')
    def export():
        if 'username' in session:
            current_user = session['username']
            if auth.get_passwords(current_user) is not None:
                fn = store.generate_csv(current_user)
                return flask.redirect(f'/download?fn={fn}', 302)
            return "No passwords for user"
        return "Error"

    @app.route('/download')
    def download():
        if 'username' in session:
            r = flask.request
            fn = r.args.get('fn')
            with open(f'/tmp/{fn}', 'rb') as f:
                data = f.read()
            resp = flask.make_response(data)
            resp.headers['Content-Disposition'] = 'attachment; filename=superpass_export.csv'
            resp.mimetype = 'text/csv'
            return resp
        return 'Error'


def main():
    configure()
    register_routes()
    app.run(host='0.0.0.0', debug=True)


if (__name__ == '__main__') or (__name__ == 'app'):
    main()
