import urllib.request, urllib.parse
import json,ssl

serviceurl="http://py4e-data.dr-chuck.net/opengeo?"

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

while True:
    address=input("Enter address: ")
    if len(address)<1:
        break
    address=address.strip()
    parms=dict()
    parms['q']=address

    url=serviceurl+urllib.parse.urlencode(parms)

    print("Retrieving",url)
    uh=urllib.request.urlopen(url, context=ctx)
    data=uh.read().decode()
    print('Retrieved',len(data),'characters')

    try:
        js=json.loads(data)
    #using exceot json.JSONDecodeError is much more specifict compared to a  normal except
    except json.JSONDecodeError:
        js=None 
    
    if not js or 'features' not in js:
        print("====Download error====")
        print(data)
        break

    if len((js['features'])) ==0:
        print('====Object not found====')
        print(data)
        break

    lat=js['features'][0]['properties']['lat']
    lon=js['features'][0]['properties']['lon']
    print('lat',lat,'lon',lon)
    plus_code=js['features'][0]['properties']['plus_code']
    print('Plus_code: ',plus_code)
    location=js['features'][0]['properties']['formatted']
    print(location)

