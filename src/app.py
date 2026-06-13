from flask import Flask , jsonify
from datetime import datetime
import socket

app = Flask(__name__)


@app.route("/myflaskapp/v1/details")
#def hello_world():
#    return "<h1>Hello, World!</h1>"
def hello_details():
    return jsonify({
        "message": "Hello, World!",
        "hostname": socket.gethostname(),
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })



@app.route("/myflaskapp/v1/health")
def health_check():
    return jsonify({"status": "up"}), 200


if __name__ == "__main__":
    #app.run() 
    app.run(host='0.0.0.0', port=5000)
