#!/usr/bin/env python3

import os
import json
from flask import Flask, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return map()

@app.route("/users/")
def users():
    users_json = '''{"users": [
        {"name": "u1", "bacts": [
            {"owner": "u1", "amount": 94},
            {"owner": "u2", "amount": 6}]},
        {"name": "u2", "bacts": [
            {"owner": "u2", "amount": 100}]}
            ]}'''
    users = json.loads(users_json)
    return render_template("users_list.html", users=users['users'])

@app.route("/map/")
def map():
    users_json = '''{"users": [
        {"name": "u1", "lat": 55.10, "long": 82.85, "bacts": [
            {"owner": "u1", "amount": 94},
            {"owner": "u2", "amount": 6}]},
        {"name": "u2", "lat": 55.01, "long": 82.93, "bacts": [
            {"owner": "u2", "amount": 100}]}
            ]}'''
    users = json.loads(users_json)
    return render_template("map.html", users=users['users'])

@app.route("/users/<name>")
def user(name):
    user_json = '''{"name": "u2", "lat": 55.10, "long": 82.85, "bacts": [
            {"owner": "u2", "amount": 100}
        ]}'''
    user = json.loads(user_json)
    return render_template("user.html", user=user)

@app.route('/favicon.ico')
def favicon():
    return ""

if __name__ == "__main__":
    app.run(host="cryptobact.io", debug=True)
