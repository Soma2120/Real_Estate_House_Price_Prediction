from flask import request,Flask,jsonify
import utils
app = Flask(__name__)


@app.route("/get_location_names", methods = ['GET'])
def get_location_names():
    response =jsonify({
        "locations": utils.get_location_names()
    })
    response.headers.add("Access-Control-Allow_Origin","*")

    return response

@app.route("/predict_home_price",methods=['GET','POST'])
def predict_home_price():
    total__sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = request.form['bhk']
    bath = request.form['bath']

    response = jsonify({
        "estimated_price" : utils.get_estimated_price(location,total__sqft,bhk,bath)
    })
    response.headers.add("Access-Control-Allow_Origin","*")

    return response


if __name__ =="__main__":
    print("Starting Python Flask Server For House Price Prediction")
    app.run()    

