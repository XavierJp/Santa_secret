#!flask/bin/python

# imports
import json
from flask import Flask, abort, render_template
from flask import make_response, jsonify

import sqlite3
import sys

app = Flask(__name__)

CREATE_USER = "INSERT INTO Users (Name) VALUES('%s');"


# root
@app.route("/addUser<name>", methods=["GET"])
def add_user(name):
    message=''
    try:
        con = sqlite3.connect('santa_secret.db');
        cur = con.cursor()
        print(CREATE_USER % name)
        cur.execute(CREATE_USER % name)
        con.commit()

    except sqlite3.Error, e:
        if con:
            con.rollback()
        print("Error %s:" %e.args[0])
        message = "Error %s:" %e.args[0]
    finally:
        if con:
            con.close()
        if message:
            return make_response(jsonify({'status':'error','message':message}))
        else:
            return make_response(jsonify({'status': 'success'}))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=3000)
