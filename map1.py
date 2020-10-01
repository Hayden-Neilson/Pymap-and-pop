import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data("LAT"))
lon = list(data("LON"))

for lt in in zip(lat, lon)

map = folium.Map(location=[74, -123], tiles="Stamen Terrain")
map.save("Map.html")
