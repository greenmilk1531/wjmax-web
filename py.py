from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")

# 서버가 실행될 때 알림 전송
@socketio.on('connect')
def notify_clients():
    try:
        with open("a.txt", "r") as file:
            content = file.read().strip()
        if content == "1":
            # 클라이언트에 알림 전송
            socketio.emit("sendNotification", {"message": "a.txt 파일 값이 1입니다!"})
    except FileNotFoundError:
        print("a.txt 파일이 존재하지 않습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
