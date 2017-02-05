from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.geocode("18019 Sippel Drive, Tinley Park, IL")
print((location.latitude, location.longitude))