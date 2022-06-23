from flask import Flask, render_template, jsonify, request, url_for
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
	
	#setting up the captions
	caps = ["The man is riding a bicycle", "The man is on a bike", "The man is high and floating"]
 
	# setting up the main image path
	path_to_image = "/Users/daksh_mac/Desktop/everything/Dev/gitRepos/HELIX/helix-web-app/helix/templates/sample.jpg"
	return render_template('soft.html', ca = caps, path = path_to_image)

if __name__ == "__main__" :
	app.run(debug = True, port = 8000)
