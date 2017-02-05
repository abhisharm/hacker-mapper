from geopy.geocoders import Nominatim
def addToLatLng(address): 
	geolocator = Nominatim()
	location = geolocator.geocode(address)
return (location.latitude, location.longitude)