import folium
import pandas as pd

data = pd.read_csv("datafile.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])

map = folium.Map(location=[20.5937, 78.9629],zoom_start = 5, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map 2")

fg.add_child(folium.Marker(location=[16.36666667, 76.78333333], popup="There's Gold Here", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("India_Map2.html")