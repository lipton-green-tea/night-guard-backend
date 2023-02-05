from flask import Flask, request

app = Flask(__name__)

body_temp_data = []
heart_rate_data = []
blood_oxygen_data = []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/set_data", methods=['POST'])
def set_data():
    new_body_temp_data = request.args.get('body_temp_data')
    new_heart_rate_data = request.args.get('heart_rate_data')
    new_blood_oxygen_data = request.args.get('blood_oxygen_data')

    if new_body_temp_data:
        body_temp_data = new_body_temp_data
    if new_heart_rate_data:
        heart_rate_data = new_heart_rate_data
    if new_blood_oxygen_data:
        blood_oxygen_data = new_blood_oxygen_data