import time
import bottle
from bottle import hook, response, route, run, app, static_file, HTTPResponse, request, default_app
import cv2
import json


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
    return HTTPResponse(status=200, body=json.dumps("ThisIsResponseText"))


@route('/video_feed')
def video_feed():
    response.content_type = 'multipart/x-mixed-replace;boundary=frame'
    return gen()


@route('/get', method='GET')
def get():
    res = HTTPResponse(status=200, body=json.dumps("get ok"))
    res.set_header('Content-Type', 'application/json')
    res.set_header('Access-Control-Allow-Origin', 'http://localhost:3000/')
    return res

app = bottle.default_app()

if __name__ == '__main__':
    run(host='localhost', port=8080, server='gunicorn', workers=4, reloader=True, debug=True)
