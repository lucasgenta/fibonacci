from flask import Flask, request


app = Flask(__name__)
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = int(request.args.get('n'))
    return str(fibonacci(n))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
