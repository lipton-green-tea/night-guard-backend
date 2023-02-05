from flask import Flask, request
from tinydb import TinyDB, Query

# import drugchecker

app = Flask(__name__)
db = TinyDB('db.json')

def set_body_temp_data(data):
    Q = Query()
    db.remove(Q.type == '1')
    db.insert({ 'type': '1', 'data': ",".join(data) })

def get_body_temp_data():
    Q = Query()
    docs = db.search(Q.type == '1')
    if len(docs) > 0:
        return docs[0]['data'].split(",")
    return []

def set_heart_rate_data(data):
    Q = Query()
    db.remove(Q.type == '2')
    db.insert({ 'type': '2', 'data': ",".join(data) })

def get_heart_rate_data():
    Q = Query()
    docs = db.search(Q.type == '2')
    if len(docs) > 0:
        return docs[0]['data'].split(",")
    return []

def set_systol_blood_pressure_data(data):
    Q = Query()
    db.remove(Q.type == '3')
    db.insert({ 'type': '3', 'data': ",".join(data) })

def get_systol_blood_pressure_data():
    Q = Query()
    docs = db.search(Q.type == '3')
    if len(docs) > 0:
        return docs[0]['data'].split(",")
    return []

def set_distol_blood_pressure_data(data):
    Q = Query()
    db.remove(Q.type == '4')
    db.insert({ 'type': '4', 'data': ",".join(data) })

def get_distol_blood_pressure_data():
    Q = Query()
    docs = db.search(Q.type == '4')
    if len(docs) > 0:
        return docs[0]['data'].split(",")
    return []

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/set_data", methods=['POST'])
def set_data():
    new_body_temp_data = request.args.get('body_temp_data').split(',')
    new_heart_rate_data = request.args.get('heart_rate_data').split(',')
    new_systol_blood_pressure_data = request.args.get('systol_blood_pressure_data').split(',')
    new_distol_blood_pressure_data = request.args.get('distol_blood_pressure_data').split(',')

    if new_body_temp_data:
        set_body_temp_data(new_body_temp_data)
    if new_heart_rate_data:
        set_heart_rate_data(new_heart_rate_data)
    if new_systol_blood_pressure_data:
        set_systol_blood_pressure_data(new_systol_blood_pressure_data)
    if new_distol_blood_pressure_data:
        set_distol_blood_pressure_data(new_distol_blood_pressure_data)

    return "Success"

@app.route("/get_data")
def get_data():
    def detect(diastolic_bp_values, systolic_bp_values, bpm_values, temp_values):
        #std devs of the parameters
        Parameters= {"Diastolic BP":14,"Systolic BP":19.6,"Body Temp":0.5,"Heart rate":7}
        n=12
        # bpm=bpmgenerator.getbpm(n,0.2)
        # tempandbp=generator.temp_and_pressure_generator(n,10,7,0.25)

        Alcohol=True
        Drugs= False
        #list of all bpm values
        # TODO bpm_values = [d['bpm'] for d in bpm['data'][0]['heart_rate_data']['detailed']['hr_samples']]
        # plt.plot(bpm_values)

        #list of all diastolic bp values
        #bpdiastolic_values = [d['diastolic_bp'] for d in tempandbp['data'][0]['blood_pressure_data']['blood_pressure_samples']]
        # TODO diastolic_bp_values = [
        #     sample['diastolic_bp'] for data in tempandbp['data'] 
        #     for sample in data.get('blood_pressure_samples', [])
        # ]
        #list of all systolic bp values
        # TODO systolic_bp_values = [
        #     sample['systolic_bp'] for data in tempandbp['data'] 
        #     for sample in data.get('blood_pressure_samples', [])
        # ]
        # plt.plot(temp)
        #list of all temp values
        
        # TODO temp_values = [x['temperature_celsius'] for x in tempandbp['data'][0]['temperature_data']['body_temperature_samples']]

        def Spiked(Alcohol,Drugs,n):
            bpmstddev= Parameters.get("Heart rate")
            tempstddev= Parameters.get("Body Temp")
            diastddev= Parameters.get("Diastolic BP")
            sysstddev= Parameters.get("Systolic BP")
            count=0
            basevals=[diastolic_bp_values[0],systolic_bp_values[0],bpm_values[0],temp_values[0]]
            if Alcohol is True or Drugs is True:
                for i in range(1,n):
                    if abs(diastolic_bp_values[i]- (basevals[0])) > diastddev:
                        count+=1
                        break
                for i in range(1,n):
                    if abs(systolic_bp_values[i]- (basevals[0])) > sysstddev:
                        count+=1
                        break
                for i in range(1,n):
                    if abs(bpm_values[i]- (basevals[0])) > 2*bpmstddev:
                        count+=0.5
                        break
                for i in range(1,n):
                    if abs(temp_values[i]- (basevals[0])) > 2*tempstddev:
                        count+=0.5
            else:
                for i in range(1,n):
                    if abs(diastolic_bp_values[i]- (basevals[0])) > diastddev:
                        count+=1
                        break
                for i in range(1,n):
                    if abs(systolic_bp_values[i]- (basevals[0])) > sysstddev:
                        count+=1
                        break
                for i in range(1,n):
                    if abs(bpm_values[i]- (basevals[0])) > bpmstddev:
                        count+=0.5
                        break
                for i in range(1,n):
                    if abs(temp_values[i]- (basevals[0])) > 2*tempstddev:
                        count+=0.5
            if count>=2:
                return True
            else:
                return False

        return Spiked(Alcohol,Drugs,n)

    drink = request.args.get("drink")
    drugs = request.args.get("drugs")

    datapoints_sent = 12

    body_temp_data = get_body_temp_data()
    heart_rate_data = get_body_temp_data()
    distol_blood_pressure_data = get_distol_blood_pressure_data()
    systol_blood_pressure_data = get_systol_blood_pressure_data()

    body_temp_data_to_send = body_temp_data[0:datapoints_sent]
    heart_rate_data_to_send = heart_rate_data[0:datapoints_sent]
    systol_blood_pressure_data_to_send = systol_blood_pressure_data[0:datapoints_sent]
    distol_blood_pressure_data_to_send = distol_blood_pressure_data[0:datapoints_sent]

    set_body_temp_data(body_temp_data[1:])
    set_heart_rate_data(heart_rate_data[1:])
    set_distol_blood_pressure_data(distol_blood_pressure_data[1:])
    set_systol_blood_pressure_data(systol_blood_pressure_data[1:])

    if (len(body_temp_data_to_send) >= datapoints_sent and
        len(heart_rate_data_to_send) >= datapoints_sent and
        len(distol_blood_pressure_data_to_send) >= datapoints_sent and
        len(systol_blood_pressure_data_to_send) >= datapoints_sent):

        body_temp = body_temp_data_to_send[0]
        heart_rate = heart_rate_data_to_send[0]
        systol_blood_pressure = distol_blood_pressure_data_to_send[0]
        distol_blood_pressure = systol_blood_pressure_data_to_send[0]

        detected = detect(
            distol_blood_pressure,
            systol_blood_pressure,
            heart_rate_data_to_send,
            body_temp_data_to_send,
        )

        # use body_temp_data_to_send
        # use heart_rate_data_to_send
        # use blood_pressure_data_to_send

        return f"{body_temp},{heart_rate},{systol_blood_pressure},{detected}"

    default_body_temp = 36.619758391275916
    default_heart_rate = 82
    default_blood_pressure = 114.4312786866055

    return f"{default_body_temp},{default_heart_rate},{default_blood_pressure},{0}"