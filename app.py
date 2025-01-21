from flask import Flask, request, jsonify

app = Flask(__name__)

#sample zip codes
service_areas = ["10001", "90210", "30301"]

@app.route("/check-service", methods=["GET"])
def check_service():
    address = request.args.get("address", "")
    #for simplicity, checking if the address/zip is in the service area
    available - address in service_areas
    return jsonify({"available": available})

if __name__ == "__main__":
    app.run(debug=True)
