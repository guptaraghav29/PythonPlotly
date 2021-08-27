import json
import plotly.express as px

with open('Sample LRS rinnuja.json') as json_file:
    data = json.load(json_file)
# print(data) dont print out its actally a really long file

print(type(data))
print(len(data))
print(data[0])
