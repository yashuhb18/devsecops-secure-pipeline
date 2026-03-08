from flask import Flask
import os

app = Flask(__name__)

# ❌ Hardcoded secret vulnerability
API_KEY = "sk_live_SECRET_KEY_123456"

@app.route("/")
def home():
    return "DevSecOps Secure Pipeline Running!"

@app.route("/secret")
def secret():
    return f"API KEY: {API_KEY}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)