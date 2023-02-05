import random
import datetime
import uuid
import numpy.random

def generate_random_body_temperature_sample(start_time, end_time):
    sample = {}
    sample["timestamp"] = datetime.datetime.strftime(
        random.uniform(start_time, end_time),
        '%Y-%m-%dT%H:%M:%S.%f+00:00'
    )
    sample["temperature_celsius"] = numpy.random.normal(37.0, .5)
    return sample

def generate_random_blood_pressure_sample(start_time, end_time):
    sample = {}
    sample["timestamp"] = datetime.datetime.strftime(
        random.uniform(start_time, end_time),
        '%Y-%m-%dT%H:%M:%S.%f+00:00'
    )
    #Normally distributed bp
    sample["systolic_bp"] = numpy.random.normal(128.4, 19.6)
    sample["diastolic_bp"] = numpy.random.normal(90, 14)
    return sample

def generate_body_temperature_data(start_time, end_time, num_samples):
    body_temperature_samples = [generate_random_body_temperature_sample(start_time, end_time) for i in range(num_samples)]
    return {"skin_temperature_samples": [],"body_temperature_samples": body_temperature_samples, "ambient_temperature_samples": [] }

def generate_blood_pressure_data(start_time, end_time, num_samples):
    blood_pressure_samples = [generate_random_blood_pressure_sample(start_time, end_time) for i in range(num_samples)]
    return {"blood_pressure_samples": blood_pressure_samples}
    
def generate_random_body_temperature_data(start_time, end_time, num_samples):
    data = {}
    data["temperature_data"] = generate_body_temperature_data(start_time, end_time, num_samples)
    data["device_data"] = {"hardware_version": None, "software_version": None, "name": None, "serial_number": None, "other_devices": [], "manufacturer": None, "activation_timestamp": None}
    data["metadata"] = {"start_time": start_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00'), "end_time": end_time.strftime('%Y-%m-%dT%H:%M:%S.%f+00:00')}
    return data

def temp_and_pressure_generator(num_samples):

  #year month day hour minute second microsecond
  start_time = datetime.datetime(2023, 2, 4, 12, 1, 46, 223625)
  end_time = datetime.datetime(2023, 2, 4, 19, 12, 46, 223625)
  body_temperature_data = generate_random_body_temperature_data(start_time, end_time, num_samples)
  bloodpressure= generate_blood_pressure_data(start_time, end_time, num_samples)
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