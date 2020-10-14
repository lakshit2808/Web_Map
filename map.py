
import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
sta = list(data["STATUS"])
loc = list(data["LOCATION"])


def colour(locations):

    if locations == 'US-Washington':
        return 'black'
    elif locations == 'US-New Mexico':
        return 'orange'
    else:
        return 'red'


map = folium.Map(location = [ 48.776798 , -121.810997] , zoom_start= 7 , tiles= "Stamen Terrain")
fg= folium.FeatureGroup(name= "My Map")

for i , j , e , l in zip(lat , lon , sta , loc) :
    fg.add_child(folium.Marker(location=[i , j] , popup=e + " LOCATIION: " + l, icon= folium.Icon(color=colour(l))))

fg.add_child(folium.GeoJson(data =(open('world.json' , 'r' , encoding='utf-8=sig').read())))


map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map1.html")