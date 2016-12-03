from flask import Flask, render_template
import requests
from pprint import pprint

# import foo_api
#from urllib.requests import urlopen

##################matching url

# import functools, re, urlparse
# import ssl

#old_match_hostname = ssl.match_hostname
URL = 'https://data.ct.gov/api/views/shww-dhc6/rows.json'
r = requests.get(URL)
app = Flask(__name__)

# URL = 'https://data.ct.gov/api/views/shww-dhc6/rows.json'
# r = requests.get(URL)
#r = urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
#content = urlopen("https://www.quora.com/")


@app.route('/')
def run():
	return render_template('home.html')
	#
	# print(r.content)

@app.route('/mapp22')
def run_mapp22():
	return render_template('mapp22.html')

if __name__=="__main__":
	app.run(debug=True, port=1111)