from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"projeto": "Pratica 10", "status": "ok"})

@app.get("/health-check")
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":  # pragma: no cover
    app.run(host="0.0.0.0")
