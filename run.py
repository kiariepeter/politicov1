
from app import create_app

app = create_app()


@app.route('/')
def hello_world():
    return 'welcome to ploiticov1'


if __name__ == '__main__':
    app.run(debug=True)
