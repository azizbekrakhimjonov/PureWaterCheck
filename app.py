from flask import Flask, request, jsonify
import flask_cors

app = Flask(__name__)
flask_cors.CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze_water():
    data = request.json
    ph = float(data.get("ph_level", 7))
    lead = float(data.get("lead_level", 0))
    mercury = float(data.get("mercury_level", 0))

    if ph < 6.5 or ph > 8.5 or lead > 0.015 or mercury > 0.002:
        result = "Suv ifloslangan!"
    else:
        result = "Suv toza."

    return jsonify({"assessment": result})

if __name__ == "__main__":
    app.run(debug=True)

