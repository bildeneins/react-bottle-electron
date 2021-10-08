import time
import bottle
import cv2
app = bottle.Bottle()
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
        
@app.route('/')
def main():
    return bottle.static_file('index.html', root='./')

@app.route('/video_feed')
def video_feed():
    bottle.response.content_type = 'multipart/x-mixed-replace;boundary=frame'
    return gen()
app.run(host='localhost', port=8080, reloader=True, debug=True)
