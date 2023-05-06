import time
import pymongo
from flask import Flask, request, make_response
from flask_cors import CORS
import os
from loguru import logger


app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.debug = True  # Enable debug mode

# Set up logger
logger.add("app.log", rotation="500 MB", level="INFO")


# Set up database connection
client = pymongo.MongoClient(os.environ.get('MONGO_URI', 'mongodb://root:pass@fibonacci_db:27019/'))
db = client["fibonacci_db"]
collection = db["fibonacci_db"]


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    # Log IP address and request
    ip_address = request.remote_addr
    http_method = request.method
    url = request.url
    logger.info(f'{ip_address} - {http_method} {url}')

    # Calculate how long the request takes
    start_time = time.time()

    n = int(request.args.get('n'))
    result = fibonacci(n)

    # Store result in database
    collection.insert_one({"n": n, "result": result})

    response = make_response(str(result))
    response.headers['Access-Control-Allow-Origin'] = '*'

    # Log how long the request took
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time}')

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
