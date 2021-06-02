import os
import decision_tree
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/result')
def result():
    urlname = request.args['name']
    result = decision_tree.getResult(urlname)
    return result


@app.route('/', methods=['GET', 'POST'])
def hello():
    return render_template("phishing_detection.html")


if __name__ == '__main__':
    app.run(debug=True)
