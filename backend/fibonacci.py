import time
from pymongo import MongoClient
from flask import Flask, request, make_response
from flask_cors import CORS
import os
from loguru import logger


app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.debug = True  # Enable debug mode

# Set up logger
#logger.add("app.log", rotation="500 MB", level="INFO")


# Set up database connection
client = MongoClient("mongodb://root:pass@:27017/")
db = client["fibonacci_db"]
collection = db["logs"]
handler = logger.handlers.MongoDBHandler(collection)
logger.add(handler)

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

    # Store result in database
    response = make_response(str(fibonacci(n)))

    response.headers.set('Access-Control-Allow-Origin', '*')

    collection.insert_one({"n": n, "result": response})
    # Log how long the request took
    end_time = time.time()
    elapsed_time = end_time - start_time
    logger.info(f'Time taken: {elapsed_time}')

    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
