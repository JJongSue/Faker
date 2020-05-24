from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

import base64
import json


class Plus(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('x', required=True, type=int, help='x cannot be blank')
            parser.add_argument('y', required=True, type=int, help='y cannot be blank')
            args = parser.parse_args()
            result = args['x']+ args['y']
            return {'result': result, 'code': '00'}
        except:
            return {'code': '01'}

#flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)
api.add_resource(Plus, '/plus')

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


@app.route("/findface", methods = ['post'])
def findFace():
    try:
        data = request.get_json(force=True)

    except Exception as e:
        print('Exception message : ', str(e))
        data = json.dumps({'code': '03'})
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)