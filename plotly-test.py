import json
import plotly.express as px

with open('Sample LRS rinnuja.json') as json_file:
    data = json.load(json_file)
# print(data) dont print out its actally a really long file

#lets grab all actors

actors = []

print(type(data))
print(len(data))
print(data[0])
print(data[0]['object']['id'])
print(len(data))

data_length = len(data)



