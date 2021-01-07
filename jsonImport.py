import plotly.graph_objects as go
import json
f = open('iris.json',)  
data = json.load(f) 
key = list(data[0].keys())

vals_dict=json.load(data)

fig = go.Figure(data=[go.Table(
    columnwidth = [80,400],
    header=dict(values=list(key),
                fill_color='paleturquoise',
                height=40,
                align='left'),
    cells=dict(values=[vals_dict.UserName,vals_dict.Email,vals_dict.IP,vals_dict.DataDołączenia,vals_dict.LiczbaUrządzeń,vals_dict.CzyAdmin],
               fill_color='lavender',
               height=40,
               align='left'))
])
