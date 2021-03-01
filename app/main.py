from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(filename='/var/log/app.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route("/")
def hello():
    return "Hello, World! - Bitwala challenge"

if __name__ == "__main__":
    # Only while testing
    app.run(host='0.0.0.0', debug=True, port=443)