#NEEDS WORK IN IT
import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'


while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print ('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print ('Retrieved',len(data),'characters')

    try: js = json.loads(str(data))
    except: js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    print (json.dumps(js, indent=4))

    placeid = js["results"][0]["place_id"]
    print ('The place ID is:',placeid)