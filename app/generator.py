import random
import datetime
from datetime import datetime, timedelta
import uuid
import numpy.random

def generate_random_body_temperature_sample(start_time, end_time,var):
    sample = {}
    sample["timestamp"] = datetime.datetime.strftime(
        random.uniform(start_time, end_time),
        '%Y-%m-%dT%H:%M:%S.%f+00:00'
    )
    sample["temperature_celsius"] = numpy.random.normal(37.0, var)
    return sample

def generate_random_blood_pressure_sample(start_time, end_time,systolicvar,diastolicvar):
    sample = {}
    sample["timestamp"] = datetime.datetime.strftime(
        random.uniform(start_time, end_time),
        '%Y-%m-%dT%H:%M:%S.%f+00:00'
    )
    #Normally distributed bp
    sample["systolic_bp"] = numpy.random.normal(128.4, systolicvar)
    sample["diastolic_bp"] = numpy.random.normal(90, diastolicvar)
    return sample

def generate_body_temperature_data(start_time, end_time, num_samples,tempvar):
    body_temperature_samples = [generate_random_body_temperature_sample(start_time, end_time,tempvar) for i in range(num_samples)]
    return {"skin_temperature_samples": [],"body_temperature_samples": body_temperature_samples, "ambient_temperature_samples": [] }

def generate_blood_pressure_data(start_time, end_time, num_samples):
    blood_pressure_samples = [generate_random_blood_pressure_sample(start_time, end_time) for i in range(num_samples)]
    return {"blood_pressure_samples": blood_pressure_samples}
    
def generate_random_body_temperature_data(start_time, end_time, num_samples,tempvar):
    data = {}
    data["temperature_data"] = generate_body_temperature_data(start_time, end_time, num_samples,tempvar)
    data["device_data"] = {"hardware_version": None, "software_version": None, "name": None, "serial_number": None, "other_devices": [], "manufacturer": None, "activation_timestamp": None}
    data["metadata"] = {"start_time": start_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00'), "end_time": end_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')}
    return data

def temp_and_pressure_generator(num_samples,systolicvar,diastolicvar,tempvar):

  #year month day hour minute second microsecond
  start_time = datetime.now()
  end_time = start_time + timedelta(minutes=10)
  body_temperature_data = generate_random_body_temperature_data(start_time, end_time, num_samples,tempvar)
  bloodpressure= generate_blood_pressure_data(start_time, end_time, num_samples,systolicvar,diastolicvar)
  result = {
    "type": "body",
    "user": {
      "scopes": None,
      "last_webhook_update": None,
      "provider": "GOOGLE",
      "reference_id": None,
      "user_id": str(uuid.uuid1())
    },
    "data": [body_temperature_data,bloodpressure],
    "version": "2022-03-16"
  }

  return (result)