import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LON"])
lon = list(data["LAT"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

map = folium.Map(location=[74, -123], tiles="Stamen Terrain")

theg = folium.FeatureGroup(name="my Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    theg.add_child(folium.Marker(
        location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(color='red')))

map.add_child(theg)
map.save("Map.html")
