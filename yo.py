import math
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def hello_world():
        return 'Hello World bucio'

@app.route('/factorial')
def factorial():
        return render_template("factorial.html")

@app.route('/factorial_action')
def factorial_action(n):
	if n==0 :
	 return 1
	else:
         return n * factorial(n-1)
n = request.args.get('n')
if __name__ == '__main__':


        app.run(host="0.0.0.0",port=5100)
