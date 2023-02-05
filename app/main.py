from flask import Flask, request

app = Flask(__name__)

body_temp_data = []
heart_rate_data = []
blood_pressure_data = []

datapoints_sent = 60

normal_body_temp = 37
normal_heart_rate = 80


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/set_data", methods=['POST'])
def set_data():
    new_body_temp_data = request.args.get('body_temp_data')
    new_heart_rate_data = request.args.get('heart_rate_data')
    new_blood_pressure_data = request.args.get('blood_pressure_data')

    if new_body_temp_data:
        body_temp_data = new_body_temp_data
    if new_heart_rate_data:
        heart_rate_data = new_heart_rate_data
    if new_blood_pressure_data:
        blood_pressure_data = new_blood_pressure_data

@app.route("get_data")
def get_data():
    body_temp_data_to_send = body_temp_data[0:datapoints_sent]
    heart_rate_data_to_send = heart_rate_data[0:datapoints_sent]
    blood_pressure_data_to_send = blood_pressure_data[0:datapoints_sent]

    body_temp_data = body_temp_data[1:]
    heart_rate_data = heart_rate_data[1:]
    blood_pressure_data = blood_pressure_data[1:]

    if (len(body_temp_data_to_send) >= datapoints_sent and
        len(heart_rate_data_to_send) >= datapoints_sent and
        len(blood_pressure_data_to_send) >= datapoints_sent):
        return 