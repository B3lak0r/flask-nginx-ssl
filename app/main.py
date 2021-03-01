from flask import Flask
from flask_logs import LogSetup

app = Flask(__name__)

app.config["LOG_TYPE"] = os.environ.get("LOG_TYPE", "watched")
app.config["LOG_LEVEL"] = os.environ.get("LOG_LEVEL", "INFO")

# File Logging Setup
app.config['LOG_DIR'] = os.environ.get("LOG_DIR", "/var/log)
app.config['APP_LOG_NAME'] = os.environ.get("APP_LOG_NAME", "app.log")
app.config['WWW_LOG_NAME'] = os.environ.get("WWW_LOG_NAME", "www.log")
logs = LogSetup()
logs.init_app(app)

@app.route("/")
def hello():
    current_app.logger.info("Functional")
    current_app.logger.error("ERROR!!!")
    current_app.logger.warning("WARNING!!!")
    return "Hello, World! - Bitwala challenge"

if __name__ == "__main__":
    # Only while testing
    app.run(host='0.0.0.0', debug=True, port=443
    )