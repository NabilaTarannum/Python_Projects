import geocoder
import folium

g = geocoder.ip("2a09:bac0:35::826:9340")
myAddress = g.latlng

my_map1 = folium.Map(location=myAddress, zoom_start=25)

my_map1.save("my_map.html")
