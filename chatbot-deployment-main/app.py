from flask import Flask ,render_template,request,jsonify
from flask_cors import CORS
from chat import get_response

app=Flask(__name__)
CORS(app)

@app.route("/",methods='GET')
def home():
    return render_template("base.html")

def home():
    text=request.get_json().get("message")
    response=get_response(text)
    message={"answer":response}
    return jsonify(message)
    
if __name__=="__main__":
    app.run(debug=True)
