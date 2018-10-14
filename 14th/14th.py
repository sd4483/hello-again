import folium
map = folium.Map(location=[1.3164, 103.8828],zoom_start = 9, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[1.329733, 103.879865], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)
map.save("SG_Map.html")

