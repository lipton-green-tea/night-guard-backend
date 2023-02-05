# %%
import generator
import bpmgenerator
#std devs of the parameters
Parameters= {"Diastolic BP":14,"Systolic BP":19.6,"Body Temp":0.5,"Heart rate":7}
#%%
bpm=bpmgenerator.getbpm(420)
tempandbp=generator.temp_and_pressure_generator(420)

#list of all bpm values
bpm_values = [d['bpm'] for d in bpm['data'][0]['heart_rate_data']['detailed']['hr_samples']]

#list of all diastolic bp values
bpdiastolic_values = [d['diastolic_bp'] for d in tempandbp['data'][0]['blood_pressure_data']['blood_pressure_samples']]

#list of all systolic bp values
bpsystolic_values = [d['systolic_bp'] for d in tempandbp['data'][0]['blood_pressure_data']['blood_pressure_samples']]

#list of all temp values
temp_values = [d['temperature_celsius'] for d in tempandbp['data'][0]['temperature_data']['skin_temperature_samples']['body_temperature_samples']]
# %%
