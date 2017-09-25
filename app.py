from flask import Flask, Response, send_from_directory, render_template, request, flash, session, abort, json
from flask import url_for, redirect
import os.path
import jinja2
import re
import os
import socket
import time
from datetime import timedelta
import datetime
import hashlib
import random 



app = Flask(__name__, static_url_path='/static')
app.debug = True
app.secret_key = os.urandom(24)


current = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date = datetime.datetime.now().date()
ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')



@app.route("/")
# @app.cache.cached(timeout=300)  # cache this view for 5 minutes
def login():
	if session.get('logged_in'):
		return redirect(url_for('dashboard'))
	else:
		error = None
		return render_template('login.html')





if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True,debug=True)
