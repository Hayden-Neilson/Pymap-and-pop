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


map = folium.Map(location=[13.067439, 80.237617],
                 Zoom_start=6, titles="Stamen Terrain")

theg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    theg.add_child(folium.CircleMarker(
        location=[lt, ln], popup=str(el) + "m", fill_color=color_producer(el), radius=8,
        color="grey", fill_opacity=0.7))

theggg = folium.FeatureGroup(name="Population")

theg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                              style_function=lambda x: {'fillColor': 'yellow'
                                                        if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(theg)
map.add_child(theggg)
map.add_child(folium.LayerControl())
map.save("Map1.html")
