import folium
import pandas as pd

data = pd.read_csv("datafile.csv")

lat = list(data["LATITUDE"])
for i in lat:
    i.replace('N', '')
    print(i)

lon = list(data["LONGITUDE"])

print(lat)
map = folium.Map(location=[20.5937, 78.9629],zoom_start = 5, tiles="Mapbox Bright")

map.save("India_Map.html")