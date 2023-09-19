from flask import Flask,request,jsonify


app = Flask(__name__)
nums=[10,20,30]
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

@app.route("/addnum",methods=['POST']) #post
def addnum():
    request_data=request.get_json()
    print(request_data['num'])
    nums.append(request_data['num'])


@app.route("/showlist") #get
def show():
    return jsonify ({'list':nums})


if __name__=="__main__":
    app.run(debug=True)
