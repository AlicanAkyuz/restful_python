from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_pymongo import pymongo

# initiate flask
app = Flask(__name__)


# get env vars
app.config.from_pyfile('settings.py')


# initiate mongo client
client = pymongo.MongoClient(app.config.get("DB_CLIENT"))


# get db
db = client.get_database('restful-python-db')


# get db's collections
user_collection = pymongo.collection.Collection(db, 'users')


# initiate restful api
api = Api(app)


# checks incoming data and determines status code
def checkPostedData(data, funcName):
    if funcName == 'add' or funcName == 'subtract':
        if 'x' not in data or 'y' not in data:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        # get request body
        postedData = request.get_json()

        # check the body
        status_code = checkPostedData(postedData, 'add')

        # return if status code is not 200
        if status_code != 200:
            ret = {
                'Message': 'Something went wrong!',
                'Status Code': status_code
            }
            return jsonify(ret)

        # if body is as expected and code is 200, do calculation and respond
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = {
            'Message': x + y,
            'Status Code': 200
        }
        return jsonify(ret)


class Subtract(Resource):
    def post(self):
        # get request body
        postedData = request.get_json()

        # check the body
        status_code = checkPostedData(postedData, 'subtract')

        # return if status code is not 200
        if status_code != 200:
            ret = {
                'Message': 'Something went wrong!',
                'Status Code': status_code
            }
            return jsonify(ret)

        # if body is as expected and code is 200, do calculation and respond
        x = postedData['x']
        y = postedData['y']
        x = int(x)
        y = int(y)
        ret = {
            'Message': x - y,
            'Status Code': 200
        }
        return jsonify(ret)


# you call resources on your api to match path with class
api.add_resource(Add, '/add')
api.add_resource(Subtract, '/subtract')


# a route out of resources
@app.route('/')
def root():
    resJ = {
        'msg': 'Coming soon.'
    }
    return jsonify(resJ)


@app.route("/test_db")
def test():
    insertionRes = user_collection.insert_one({"name": "TestUser"})
    if insertionRes:
        return 'User inserted!'
    else:
        return 'DB may not be working properly'


# start the server
if __name__ == '__main__':
    app.run()
