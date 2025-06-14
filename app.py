# app.py
from flask import Flask, jsonify

# Create a Flask application instance
app = Flask(__name__)

@app.route("/")
def hello():
    """Returns a simple JSON response."""
    return jsonify({"message": "Hello, World! This is a Python CI/CD demo."})

@app.route("/health")
def health_check():
    """Health check endpoint to verify the app is running."""
    return jsonify({"status": "ok"}), 200

# This block allows you to run the app directly with `python app.py`
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)