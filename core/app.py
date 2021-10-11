import time
# import bottle
from bottle import hook, response, route, run, app, static_file, HTTPResponse, request
import cv2
import json
 

# app = bottle.Bottle()
def gen():
    
    cam = cv2.VideoCapture(0)
    while True:
        # 動画から1フレーム分の画像を読み込み
        ret_val, image = cam.read()
        if not ret_val:
            break
        # jpg形式に変換
        flag, frame = cv2.imencode('.jpg', image)
        yield b'--frame\r\n' + b'Content-Type: image/jpeg\r\n\r\n' + bytearray(frame) + b'\r\n\r\n'
        # 連続再生されるのでwaitを入れる
        time.sleep(1/60)

@route('/')
def main():
    return static_file('index.html', root='./')

@route('/video_feed')
def video_feed():
    response.content_type = 'multipart/x-mixed-replace;boundary=frame'
    return gen()

@route('/get', method='OPTIONS')
def support_cors():
    res = HTTPResponse(status=200, body=None)
    res.set_header('Access-Control-Allow-Origin', 'http://localhost:3000/')
    return res

@route('/get', method='GET') 
def get():
    print(request.headers)
    res = HTTPResponse(status=200, body=json.dumps("get ok"))
    res.set_header('Content-Type', 'application/json')
    res.set_header('Access-Control-Allow-Origin', 'http://localhost:3000/')
    return res

@route('/post', method='OPTIONS')
def support_cors():
    res = HTTPResponse(status=200, body=None)
    res.set_header('Access-Control-Allow-Origin', 'http://localhost:3000/')
    return res          
@route('/post',method="POST")
def post():
    data = { "post ok" }
    res = HTTPResponse(status=200, body=json.dumps(data))
    res.set_header('Content-Type', 'application/json')
    res.set_header('Access-Control-Allow-Origin', '*')
    return res

run(host='localhost', port=8080, reloader=True, debug=True)
