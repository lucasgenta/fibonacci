import logging
import time
import pymongo
from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Set up database connection
client = pymongo.MongoClient("mongodb://database_user:database_password@database_host:27017/")
db = client["database_name"]
collection = db["fibonacci"]

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
    logging.info(f'{ip_address} - {http_method} {url}')

    # Calculate how long the request takes
    start_time = time.time()

    n = int(request.args.get('n'))
    result = fibonacci(n)

    # Store result in database
    collection.insert_one({"n": n, "result": result})

    response = make_response(str(result))

    # Log how long the request took
    end_time = time.time()
    elapsed_time = end_time - start_time
    logging.info(f'Time taken: {elapsed_time}')

    response.headers.set('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
