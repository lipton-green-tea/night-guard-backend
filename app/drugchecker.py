# %%
import generator
import bpmgenerator
import matplotlib.pyplot as plt
#std devs of the parameters
Parameters= {"Diastolic BP":14,"Systolic BP":19.6,"Body Temp":0.5,"Heart rate":7}
#%%
n=12
bpm=bpmgenerator.getbpm(n)
tempandbp=generator.temp_and_pressure_generator(n)

Alcohol=True
Drugs= False
#list of all bpm values
bpm_values = [d['bpm'] for d in bpm['data'][0]['heart_rate_data']['detailed']['hr_samples']]
plt.plot(bpm_values)

#list of all diastolic bp values
#bpdiastolic_values = [d['diastolic_bp'] for d in tempandbp['data'][0]['blood_pressure_data']['blood_pressure_samples']]
diastolic_bp_values = [
    sample['diastolic_bp'] for data in tempandbp['data'] 
    for sample in data.get('blood_pressure_samples', [])
]
#list of all systolic bp values
systolic_bp_values = [
    sample['diastolic_bp'] for data in tempandbp['data'] 
    for sample in data.get('blood_pressure_samples', [])
]
#%%
#list of all temp values
temp_values = [
    sample['temperature_celsius'] for data in tempandbp['data'] 
    for sample in data.get('body_temperature_samples', [])
]
# %%

def Spiked(Alcohol,Drugs,n):
    bpmstddev= Parameters.get("Heart rate")
    tempstddev= Parameters.get("Body Temp")
    diastddev= Parameters.get("Diastolic BP")
    sysstddev= Parameters.get("Systolic BP")
    count=0
    basevals=[diastolic_bp_values[0],systolic_bp_values[0],bpm_values[0],temp_values[0]]
    if Alcohol is True:
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
            if abs(temp_values[i]- (basevals[0])) > tempstddev:
                count+=0.5
    elif Alcohol is False and Drugs is True:
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
            if abs(temp_values[i]- (basevals[0])) > tempstddev:
                count+=0.5
    if count>=2:
        return True
    else:
        return False

Spiked(Alcohol,Drugs,n)

