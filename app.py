from flask import Flask ,render_template ,url_for,request,redirect,session
from flask.views import MethodView
import webbrowser

app=Flask(__name__)

@app.route('/',methods=["GET"])
def hello_world5():
    return render_template('index8.html',title="Multi search engines",message="↓ Select your search engine")

@app.route('/',methods=["POST"])
def form6():
    return render_template('index8.html',title2="Multi search engines",message="↓ search again ?")

@app.route('/secondpage',methods=["GET"])
def hello_world6():
    return render_template('index9.html',title="Multi search engines",message="↓ Select your SNS")

@app.route('/secondpage',methods=["POST"])
def form7():
    return render_template('index9.html',title2="Multi search engines",message="↓ search again ?")


@app.route('/thirdpage',methods=["GET"])
def hello_world7():
    return render_template('index10.html',title="Multi search engines",message="↓ Select your Web Service")

@app.route('/thirdpage',methods=["POST"])
def form8():
    return render_template('index10.html',title2="Multi search engines",message="↓ search again ?")







if __name__=="__main__":
    app.debug=True
    app.run(host='localhost')
