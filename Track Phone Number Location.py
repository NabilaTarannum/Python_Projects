import phonenumbers
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

key = "f8005f4a8feb432ba7bf3867903c38af"
number = input("Enter a number :")
samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "en")
print(yourLocation)
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
result = geocoder.geocode(query)
# print(result)
lat = result[0]["geometry"]["lat"]
lng = result[0]["geometry"]["lng"]
print(lat, lng)
myMap = folium.Map(location=[lat, lng], zoom_start=10)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)
myMap.save("myLocation.html")
