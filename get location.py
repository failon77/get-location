import geocoder
import folium

ip = geocoder.ip("me")
location = ip.latlng
map = folium.Map(location=location, zoom_start=10)
folium.Marker(location).add_to(map)
map.save("map.html")
print(location)
