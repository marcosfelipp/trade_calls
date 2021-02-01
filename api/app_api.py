import logging
import os

from flask_cors import CORS
from api import app


# logging
logging.getLogger('trade_api').setLevel(logging.INFO)

if __name__ == '__main__':

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.run(host='0.0.0.0', port=5000, debug=False)
