from flask import Flask, render_template, request
#import request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ?~@~X/?~@~Y URL is bound with hello_world() function.
def hello_world():
        return 'Hello World bucio'

@app.route('/miles2km')
def miles2km():
	return render_template("miles2km.html")

@app.route('/miles2km_action')
def miles2km_action():
    miles  = request.args.get("miles")
    return "km="+str(float(miles)*1.60934)

@app.route('/feet2meters')
def feet2meters():
        return render_template("feet2meters.html")

@app.route('/feet2meters_action')
def feet2meters_action():
    feet  = request.args.get("feet")
    return "Meters="+str(float(feet)*0.3048)

@app.route('/inchtocm')
def inchtocm():
        return render_template("inchtocm.html")

@app.route('/inchtocm_action')
def inchtocm_action():
    inches  = request.args.get("inches")
    return "CM="+str(float(inches)*2.54)

# main driver function
if __name__ == '__main__':


        # run() method of Flask class runs the application
        # on the local development server.
        app.run(host="0.0.0.0",port=5100)
from flask import Flask, render_template, request
#import request

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ?~@~X/?~@~Y URL is bound with hello_world() function.
def hello_world():
        return 'Hello World bucio'

@app.route('/feet2meters')
def feet2meters():
        return render_template("feet2meters.html")

@app.route('/feet2meters_action')
def feet2meters_action():
    feet  = request.args.get("feet")
    return "Meters="+str(float(feet)*0.3048)

@app.route('/inchtocm')
def inchtocm():
        return render_template("inchtocm.html")

@app.route('/inchtocm_action')
def inchtocm_action():
    inch  = request.args.get("inch")
    return "CM="+str(float(inches)*2.54)

@app.route('/miles2km')
def miles2km():
        return render_template("miles2km.html")

@app.route('/miles2km_action')
def miles2km_action():
    miles  = request.args.get("miles")
    return "KM="+str(float(miles)*1.60934)


# main driver functio
