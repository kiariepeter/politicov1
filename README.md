# Politicov1       [![Build Status](https://travis-ci.com/kiariepeter/politico.svg?branch=develop)](https://travis-ci.com/kiariepeter/politico)  [![Coverage Status](https://coveralls.io/repos/github/kiariepeter/politicov1/badge.svg?branch=develop)](https://coveralls.io/github/kiariepeter/politicov1?branch=develop)[![Maintainability](https://api.codeclimate.com/v1/badges/01ed269703dd07d43102/maintainability)](https://codeclimate.com/github/kiariepeter/politicov1/maintainability)

Politicov1 involves endpoints to add,edit,delete and update political parties and officess.

## Getting Started

1) Clone the repository by doing: `git clone https://github.com/kiariepeter/politicov1.git`

2) Git checkout develop

3) Create a virtual environment: `virtualenv -p python3 env`

4) Activate the virtual environment: `source env/bin/activate` on Linux/Mac  or `source venv/Scripts/activate` on windows.

5) Install the requirements : `pip install -r requirements.txt`




### Prerequisites
-   python 3.6
-   virtual environment


## Running it on machine
- Create a .env file to store your environment variables: `touch .venv`
- In the `.venv` file add this line: `export SECRET=<your-secret-key-here`
- On terminal do: `source .venv`
- Run the application: `python run`
- The api endpoints can be consumed using postman.

## Endpoints
| Endpoint                                   | FUNCTIONALITY                      |
| ----------------------------------------   |:----------------------------------:|
| POST  /api/v1/parties                        | CREATE political party             |
| GET  /api/v1/parties                         | GET ALL political parties          |
| GET  /api/v1/parties/<int:party_id>          | GET ONE political party            |
| DELETE  /api/v1/parties                      | DELETE ONE political party         |
| PATCH  /api/v1/parties/<int:party_id>          | UPDATE ONE political party         |
| POST  /api/v1/offices                       | CREATE government office           |
| GET  /api/v1/offices/<int:office_id>        | GET ONE government office          |
| GET  /api/v1/offices                        | GET ALL government offices          |


## Built With
* [Flask-Api](http://flask.pocoo.org/docs/1.0/api/) -  The web framework used
* [Pip](https://pypi.python.org/pypi/pip) -  Dependency Management

## Authors
* **Peter Kiarie** 

## License

This project is licensed under the MIT License