import simplejson, urllib.request
""" 
Inputs: orig_coord - tuple of latitude and longitude
        dest_corod - tuple of latitude and longitude
"""
def getDriveTime(orig_coord, dest_coord):
	url = "http://maps.googleapis.com/maps/api/distancematrix/json?origins={0}&destinations={1}&mode=driving&language=en-EN&sensor=false".format(str(orig_coord[0]+','+str(orig_coord[1])),str(str(dest_coord[0])+','+str(dest_coord[1])))
	result= simplejson.load(urllib.request.urlopen(url))
	driving_time = result['rows'][0]['elements'][0]['duration']['value']
	return driving_time 
