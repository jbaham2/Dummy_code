from flask import Flask, render_template, session, redirect, url_for
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/<tab>')
def dashboard(tab):
    return render_template('dashboard.html', tab=tab)


if __name__ == '__main__':
    app.run(debug=True)
