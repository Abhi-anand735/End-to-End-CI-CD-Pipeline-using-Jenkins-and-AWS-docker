import os
import socket
import logging
from datetime import datetime
from flask import Flask, jsonify, render_template

# --------------------------------------------------
# Flask Configuration
# --------------------------------------------------

app = Flask(__name__)

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# --------------------------------------------------
# Environment Variables
# --------------------------------------------------

APP_NAME = os.getenv("APP_NAME", "CI/CD Demo Application")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
BUILD_NUMBER = os.getenv("BUILD_NUMBER", "Local")
GIT_COMMIT = os.getenv("GIT_COMMIT", "Unknown")
DEPLOY_ENV = os.getenv("DEPLOY_ENV", "Development")
PORT = int(os.getenv("PORT", 5000))

HOSTNAME = socket.gethostname()

START_TIME = datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.route("/")
def home():

    logger.info("Home page accessed")

    return render_template(
        "index.html",
        app_name=APP_NAME,
        version=APP_VERSION,
        build=BUILD_NUMBER,
        commit=GIT_COMMIT,
        hostname=HOSTNAME,
        environment=DEPLOY_ENV,
        deployed=START_TIME,
        current=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    )


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.route("/health")
def health():

    logger.info("Health endpoint called")

    return jsonify(
        status="UP",
        application=APP_NAME,
        version=APP_VERSION,
        hostname=HOSTNAME,
        time=datetime.now().isoformat()
    ), 200


# --------------------------------------------------
# Application Information
# --------------------------------------------------

@app.route("/info")
def info():

    logger.info("Application information requested")

    return jsonify(
        {
            "application": APP_NAME,
            "version": APP_VERSION,
            "build_number": BUILD_NUMBER,
            "git_commit": GIT_COMMIT,
            "environment": DEPLOY_ENV,
            "hostname": HOSTNAME,
            "startup_time": START_TIME,
            "current_time": datetime.now().isoformat()
        }
    )


# --------------------------------------------------
# Environment Variables
# --------------------------------------------------

@app.route("/env")
def env():

    safe_env = {
        key: value
        for key, value in os.environ.items()
        if "PASSWORD" not in key
        and "SECRET" not in key
        and "TOKEN" not in key
    }

    return jsonify(safe_env)


# --------------------------------------------------
# Container Details
# --------------------------------------------------

@app.route("/container")
def container():

    return jsonify(
        {
            "hostname": HOSTNAME,
            "python_version": os.sys.version,
            "operating_system": os.name,
            "working_directory": os.getcwd(),
            "deployment_environment": DEPLOY_ENV
        }
    )


# --------------------------------------------------
# Jenkins Build Details
# --------------------------------------------------

@app.route("/build")
def build():

    return jsonify(
        {
            "build_number": BUILD_NUMBER,
            "git_commit": GIT_COMMIT,
            "version": APP_VERSION,
            "deployment_time": START_TIME
        }
    )


# --------------------------------------------------
# Readiness Probe
# --------------------------------------------------

@app.route("/ready")
def ready():

    return jsonify(
        {
            "ready": True
        }
    )


# --------------------------------------------------
# Liveness Probe
# --------------------------------------------------

@app.route("/live")
def live():

    return jsonify(
        {
            "alive": True
        }
    )


# --------------------------------------------------
# Error Handling
# --------------------------------------------------

@app.errorhandler(404)
def not_found(error):

    return jsonify(
        {
            "error": "Page Not Found"
        }
    ), 404


@app.errorhandler(500)
def internal(error):

    logger.error(error)

    return jsonify(
        {
            "error": "Internal Server Error"
        }
    ), 500


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":

    logger.info("--------------------------------------")
    logger.info(APP_NAME)
    logger.info(f"Version      : {APP_VERSION}")
    logger.info(f"Build Number : {BUILD_NUMBER}")
    logger.info(f"Environment  : {DEPLOY_ENV}")
    logger.info(f"Hostname     : {HOSTNAME}")
    logger.info("--------------------------------------")

    app.run(
        host="0.0.0.0",
        port=PORT,
        debug=False
    )
