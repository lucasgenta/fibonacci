
import psycopg2
from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="database",
    database="fibonacci",
    user="postgres",
    password="your_password",
    port=5432
)

cur = conn.cursor()

# Create the results table if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id SERIAL PRIMARY KEY,
        ip TEXT NOT NULL,
        n INTEGER NOT NULL,
        result INTEGER NOT NULL
    );
""")
conn.commit()

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    x = int(request.args.get('n'))
    ip = request.remote_addr
    result = fibonacci(x)
    cur.execute("INSERT INTO results (ip, n, result) VALUES (%s, %s, %s)", (ip, x, result))
    conn.commit()
    response = make_response(str(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
