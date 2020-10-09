import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LON"])
lon = list(data["LAT"])
elev = list(data["ELEV"])


def color_producer(elevation):

    if elevation <= 1000:
        return "green",
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return "red"


map = folium.Map(location=[74, -123], tiles="Stamen Terrain")

theg = folium.FeatureGroup(name="my Map")

for lt, ln, el in zip(lat, lon, elev):
    theg.add_child(folium.CircleMarker(
        location=[lt, ln], popup=str(el) + "m", fill_color=color_producer(el), radius=8,
        color="grey", fill_opacity=0.7))

theg.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding=('utf-8-sig').read()))))

map.add_child(theg)
map.save("Map1.html")
