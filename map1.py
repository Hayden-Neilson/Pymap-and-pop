import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LON"])
lon = list(data["LAT"])

map = folium.Map(location=[74, -123], tiles="Stamen Terrain")

theg = folium.FeatureGroup(name="my Map")

for lt, ln in zip(lat, lon):
    theg.add_child(folium.Marker(
        location=[lt, ln], popup="hi iam  Marker", icon=folium.Icon(color='red')))

map.add_child(theg)
map.save("Map.html")
