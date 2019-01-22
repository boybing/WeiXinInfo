# coding=utf-8

import os
from flask import Flask, render_template, request, jsonify
import hashlib
import json
import datetime

app = Flask(__name__)

###`
# Routing for your application.
###

def get_token(str, token):
    retRes = False
    m1 = hashlib.md5()
    m1.update(str.encode("utf-8"))
    tk = m1.hexdigest()
    if tk == token:
        retRes = True
    print (token)
    print (tk)
    return retRes

# 校对token
def getMd5(time, token):
    try:
        tmpStr = time + app.config['KSTR']
        print (tmpStr)
        return get_token(tmpStr, token)
    except:
        raise RuntimeError('Token错误')


@app.route('/rt.html', methods=['GET'])
def home():
    """Render website's home page."""
    try:
        message = request.args.get('code')
        return jsonify(code=200, status=0, message=message+datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    except:
        return render_template('404.html'), 404


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
