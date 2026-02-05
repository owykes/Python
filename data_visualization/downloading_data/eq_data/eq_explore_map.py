from pathlib import Path
import json

import plotly.express as px
#pi work around
import plotly.io as pio
pio.renderers.default = "png"

# Read data as atring and convert to a python object.
path = Path('/home/owykes/Documents/Python/data_visualization/downloading_data/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]  

title = 'Global Earthquakes'
# hoover will not show on png, leave in for render via html when possible
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color':'Magnitude'}, projection='natural earth', hover_name=eq_titles,)
fig.write_image('global_earthquakes.png') 



































