import geocoder
import folium

ip = geocoder.ip("36.175, -115.1372")
location = ip.latlng
map = folium.Map(location=location, zoom_start=10)
folium.Marker(location).add_to(map)
map.save("map.html")
print(location)