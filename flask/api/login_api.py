from flask import Flask
import flask

app = Flask(__name__, static_folder='.', static_url_path='')


@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route("/mypage")
def mypage():
    login = False
    # login = True
    if login is False:
        return flask.jsonify({"code": 400, "msg": "Bad Request"})

    user_data = {"user_name": "ai_academy"}
    return flask.jsonify({"code": 200, "msg": "OK", "result": user_data})


if __name__ == "__main__":
    app.run(port=8000, debug=True)