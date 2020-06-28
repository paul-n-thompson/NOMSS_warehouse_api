#Coded By: Paul N Thompson
#Coded for the NOMSS Tech Challenge

from flask import Flask, render_template, jsonify, request
import json
from warehouse_api import warehouse_blueprint

app = Flask(__name__)

app.register_blueprint(warehouse_blueprint)
@app.route("/")
def home():
    return render_template("main.html")

if __name__ == "__main__":
    app.run(debug=True)