from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=['get'])

def index():
	API_KEY = 'c774c2f576b26dd9d73420ceea0f4a17'
	city = request.args.get('q')
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
	response=requests.get(url).json()
	if response.get('cod')==200:
		current_temp = response.get('main').get('temp')
		weather = f'The current temperature of {city} is {round(current_temp - 273.15, 2)}.'
		return render_template('index.html', weather = weather)
	else:
		weather = f'Error: {city} not found.'
		return render_template('index.html', weather = weather)

if __name__ == '__main__':
	app.run()
