from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin

from main import DATA, row_to_dict

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Data(Resource):
    @cross_origin()
    def get(self):
        return DATA

    @cross_origin()
    def post(self):
        # print(request.data.decode('utf-8'))
        DATA.clear()
        for row in request.data.decode('utf-8').split('\n'):
            row_to_dict(*row.split(','))
        # DATA.update(request.json)
        # print(DATA)
        return DATA, 201


api.add_resource(Data, '/data')


if __name__ == '__main__':
    app.run(debug=True)
