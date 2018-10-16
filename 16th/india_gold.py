import folium
import pandas as pd

data = pd.read_csv("datafile.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])

map = folium.Map(location=[20.5937, 78.9629], zoom_start=6, tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="India Gold Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup = "Hi, theres Gold Here!", icon = folium.Icon(color="green")))

map.add_child(fg)

map.save("India-Gold.html")
