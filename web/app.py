from flask import Flask, jsonify, request
from flask_restful import Api, Resource

# initiate flask
app = Flask(__name__)

# initiate restful api
api = Api(app)


# checks incoming data and determines status code
def checkPostedData(data, funcName):
    if funcName == 'add' or funcName == 'subtract' or funcName == 'multiply':
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


# you call add resource on your api to match path with class
api.add_resource(Add, '/add')


# a route out of resources
@app.route('/')
def root():
    resJ = {
        'msg': 'Coming soon.'
    }
    return jsonify(resJ)


# start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0')
