from app import create_app

app = create_app()


@app.route('/')
def index():
    return 'welcome to politicov1 endpoint'


if __name__ == '__main__':
    app.run(debug=True)
