import json
from flask import Flask
from flask_restful import Resource, Api

import ml


app = Flask(__name__)
api = Api(app)

class GetAnn(Resource):
    def get(self, x_data):
        x_data = json.loads(x_data)
        return {'prediction': json.dumps(ml.ann.getPrediction(x_data))}

api.add_resource(GetAnn, '/ann/<string:x_data>')

if __name__ == '__main__':
    app.run(debug=True)
