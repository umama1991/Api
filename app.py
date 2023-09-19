from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!<h1>"
@app.route("/evenOdd<int:num>")
def evenOdd(num):
    status=None
    if num%2==0:
        status="Even"
    else:
        status="Odd"
    return jsonify ({'status':status})
if __name__=="__main__":
    app.run(debug=True)
