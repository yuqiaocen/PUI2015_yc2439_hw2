import json
import sys
import urllib2

if __name__=='__main__':
    key = sys.argv[1]  
    # myAPIKey=fd8fd5d0-7df9-4a31-bff4-22ed3beb11a1
    busline = sys.argv[2]  
    print "Bus Line : %s" % busline    
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, busline)
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    print "Number of Active Buses: %d" %len(buses)
    for i in range(len(buses)):
        locations = buses[i]['MonitoredVehicleJourney']["VehicleLocation"]
        lat = locations['Latitude']
        lon = locations['Longitude']
        print "Bus %d is at latitude %f and longitude %f" % (i, lat, lon)
        