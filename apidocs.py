from app import create_app
from flasgger import Swagger
app = create_app()
swagger = Swagger(app)


@app.route('/api/v2/users', methods =['GET'])
def get_users():
    """This returns all users
    ---
    tags:
        - users
    responses:
            200
    """

if __name__ == "__main__":
    app.run()