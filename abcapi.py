"""from flask import Flask, render_template

app = Flask(__name__)

# index
@app.route('/')
def index():
    return "Hello"

# /me    
@app.route("/me", methods=["GET"])
def get_results():
    return "Dummy Result"

if __name__ == "__main__":
    app.run()"""
print("Hello World")

#get stock data in python
import requests
import json
response = requests.get(https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow)



