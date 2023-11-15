from flask import Flask, render_template, request, redirect, url_for, session
import fileinput
import sys
import math

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, world!'

@app.route('/hi')
def hi():
    return 'Hi, world!'

@app.route('/statapp')
def statapp():
    return render_template("statapp.html")

@app.route('/statapp_action')
def statapp_action():
    input_line = request.args.get("scores")

    scores=input_line.split(",")

    for i in range(len(scores)):
      scores[i]=int(scores[i])

    mean = sum(scores) / len(scores)
    res = sum((x - mean) ** 2 for x in scores) / len(scores)
    sd = math.sqrt(res)

    webpage = "<html>"
# printing result
    webpage +=("The mean of list is : " + str(mean))
    webpage +=("The mean of list is : " + str(mean))
    webpage +=("The variance of list is : " + str(res))
    webpage +=("The sd of list is : " + str(sd))

    return webpage
    
if __name__ == "__main__":
    app.run("0.0.0.0",port=5100)
