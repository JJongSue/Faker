from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
from flask_restful import reqparse, abort, Api, Resource
import facerecognition
import base64
import json
import demo
from datetime import datetime
import os

#flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)


@app.route('/upload')
def render_file():
   return render_template('/upload.html')


@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f1 = request.files['file1']
      print(f.filename)
      print(type(f.filename))
      nows = datetime.now()
      nows = nows.microsecond

      #저장할 경로 + 파일명
      f.save(secure_filename(str(nows)+f.filename))
      f1.save(secure_filename(str(nows)+f1.filename))
      demo.ai_demo(source_image=str(nows)+f.filename, driving_video=str(nows)+f1.filename, config="vox-256.yaml", checkpoint='vox-cpk.pth.tar')
      os.remove(str(nows)+f.filename)
      os.remove(str(nows)+f1.filename)
    #   return '<video src="./result.mp4", width="1280px", height="720px"></video>'
      return 'uploads 디렉토리 -> 파일 업로드 성공!'


@app.route("/findface", methods = ['post'])
def findFace():
    try:
        data = request.get_json(force=True)
        base64img = data['image']
        a = facerecognition.find_location(base64img)
        # print(len(a))
        # print('a', a)
        d = {'code': '00', 'images': a}
        # print(d)
        data = json.dumps(d)
        return data
        

    except Exception as e:
        print('Exception message : ', str(e))
        data = json.dumps({'code': '03'})
        return data

@app.route("/changeContents", methods = ['post'])
def changeContest():
    try:
        demo.ai_demo(source_image="YEE.jpg", driving_video='04.mp4', config="vox-256.yaml", checkpoint='vox-cpk.pth.tar')
        # demo.ai_demo(source_image="YEE.jpg", )
        data = request.get_json(force=True)
        base64img = data['image']
        a = facerecognition.find_location(base64img)
        # print(len(a))
        # print('a', a)
        d = {'code': '00', 'images': a}
        # print(d)
        data = json.dumps(d)
        return data
    except Exception as e:
        print('Exception message : ', str(e))
        data = json.dumps({'code': '03'})
        return data



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)