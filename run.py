from app import create_app
import os
import urllib.request
app = create_app()


@app.route('/')
def index():
	url ="http://139.162.205.192/ts/"
	request = urllib.request.Request(url)
	response = urllib.request.urlopen(request)
	return (response.read().decode('utf-8'))


if __name__ == '__main__':
    app.run(debug=True)
