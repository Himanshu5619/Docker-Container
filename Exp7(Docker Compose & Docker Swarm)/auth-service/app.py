from flask import Flask
app = Flask(__name__)

@app.route('/auth')
def auth():
    return "Authentication Service is running!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
