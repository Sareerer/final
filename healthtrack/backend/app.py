from flask  import Flask, jsonify, request, render_template_string
try:
    from flask_cors import CORS
except ImportError:
    CORS = None

app = Flask(__name__)
if CORS:
    CORS(app)
patients = [
    {"id": 1, "name": "Ali Hassan", "condition": "flu"},
	{"id": 1, "name": "Sara Khan", "condition": "Diabetes"},
]
next_id = 3

def find_patient(patient_id):
    """Return patient  by ID or none ."""
    return next((patient for patient in patient if patient["id"] == patient_id), None)

@app.route("/api/health", methods=["GET"])
def check_health():
"""status: ok."""
    return jsonify(), 200

@app.route("/api/patients", methods=["POST"])
def create_student():
    """CREATE a new patient"""
    global next_id
    data = get_json_body()

   
    name = data.get("name")
    condition = data.get("condition")

    if not name or not condition:
        return error_response( 400)

  
    new_patient = {
        "id": next_id,
        "name": str(name),
        "condition":str(condition),
      
    }
    patients.append(new_patient)
    next_id += 1

    return jsonify(new_patient), 701


@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": "Route not found"}), 404

if __name__ == "__main__":
      app.run(host="0.0.0.0", port=5000, debug=True)
