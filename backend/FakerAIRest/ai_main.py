from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import facerecognition
import base64
import json


#flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)


@app.route("/findface", methods = ['post'])
def findFace():
    try:
        data = request.get_json(force=True)
        base64img = data['image']
        a = facerecognition.find_location(base64img)
        print(type(a))
        # print('a', a)
        d = {'code': '00', 'images': a}
        print(d)
        data = json.dumps(d)
        return data
        

    except Exception as e:
        print('Exception message : ', str(e))
        data = json.dumps({'code': '03'})
        return data

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)