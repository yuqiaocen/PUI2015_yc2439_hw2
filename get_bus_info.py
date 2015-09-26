import json
import sys
import urllib2
import csv

if __name__=='__main__':
    key = sys.argv[1]  
    # myAPIKey=fd8fd5d0-7df9-4a31-bff4-22ed3beb11a1
    busline = sys.argv[2]    
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, busline)
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude','Longitude','Stop Name','Stop Status']
        writer.writerow(headers)
        
        for i in buses:
            lat  = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            lon  = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if i['MonitoredVehicleJourney']['OnwardCalls'] == {}:
                StopName = 'N/A'
                StopStatus = 'N/A'
            else:
                StopName = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
                StopStatus = i['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            writer.writerow([lat,lon,StopName,StopStatus])