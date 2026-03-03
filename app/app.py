from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Devops World"

@app.route('/health')
def health():
    return {"status":"healthy"}, 200

@app.route('/version')
def version():
    return {"version":"1.0.0"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)