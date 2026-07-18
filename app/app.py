from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        service="ai-devops-platform",
        status="running",
        message="Welcome to the AI DevOps Platform"
    )


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    metrics = PrometheusMetrics(app)
    app.run(host="0.0.0.0", port=5000)