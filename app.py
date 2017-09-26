from flask import Flask, Response, send_from_directory, render_template, request, flash, session, abort, json
from flask import url_for, redirect
import os.path
import re
import os
import timeit



app = Flask(__name__, static_url_path='/static')
app.debug = True
app.secret_key = os.urandom(24)





@app.route("/")
def index():
	#define number between 1 to 10
	number = 6
	a=1
	b=2
	m=5000
	x=3
	lst=[]
	for i in range(10):
	  x=(a*x+b)%m
	  lst.append(x)
	print(lst)
	if len(lst) != len(set(lst)):
	    print("it has duplicates but possibly random numbers")
	else:
	    print("those were random numbers")
	random = timeit.Timer('for i in range(1000):i**i').timeit(1)*10032890%100*number
	print random
	return str(random)





if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True,debug=True)
