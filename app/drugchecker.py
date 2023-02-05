import generator
import bpmgenerator
#for blood pressure and bpm the parameters are std deviations
#for temp that is the max variation from mean generslly
Parameters= {"Diastolic BP":14,"Systolic BP":19.6,"Body Temp":0.9,"Heart rate":7}
bpm=bpmgenerator.getbpm(420)
tempandbp=generator.temp_and_pressure_generator(420)



