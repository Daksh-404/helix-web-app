from flask import Flask, render_template, jsonify, request
import subprocess

app = Flask(__name__)

# landing page
@app.route('/', methods=['POST', 'GET'])
def index():

    return render_template('index.html')

# for showing image frames, videos and the captions
@app.route('/out', methods=['POST', 'GET'])
def out():
	#running the batch file
	if request.method == "POST":
		subprocess.call([r'test.bat'])
	caps = ["hcwouiv", "fvjbv", "ciujbv"]
	return render_template('soft.html', ca = caps)

if __name__ == "__main__" :
	app.run(debug = True, port = 8000)