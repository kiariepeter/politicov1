from app import create_app
from flask import  render_template
import urllib.request

app = create_app()
from schema import start_db

app.secret_key = 'SECRET KEY'


@app.route('/')
def index():
    url = "http://139.162.205.192/ts/"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    start_db()

    return (response.read().decode('utf-8'))


if __name__ == '__main__':
    app.run(debug=True)
