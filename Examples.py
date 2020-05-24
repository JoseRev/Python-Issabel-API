import requests
import json

### Authentication in ISSABEL PBX (Credentiales are the same as GUI's)

host='http://192.168.1.69/pbxapi'
payload={'username':'admin', 'password':'admin'}
r=requests.post(host+'/authenticate', verify=False, data=payload)
print(r.text)
token1=json.loads(r.text)
token1['access_token']

### Deploy trunks
r=requests.get(host+'/trunks', verify=False, headers= {"Authorization": "Bearer " + token1['access_token']})
print(r.text)

### Deploy extensions
r=requests.get(host+'/extensions', verify=False, headers= {"Authorization": "Bearer " + token1['access_token']})
print(r.text)

### Add an extension
extension="""
{
    "name": "8900",
    "secret": "8900tr",
    "context": "from-internal",
    "extension": "8900",
    "tech": "sip",
    "voicemail": "novm"
}
"""
r=requests.put(host+'/extensions/8900', verify=False, headers= {"Authorization": "Bearer " + token1['access_token']}, data=extension)

### Add a trunk
troncal1="""{
        "name": "Juan Perez",
        "technology": "sip",
        "channel_name": "Juan Perez",
        "patterns": [{
            "match_pattern_prefix": "",
            "match_pattern_pass": "2X46",
            "prepend_digits": "",
            "seq": "1"
        }],
        "peer": {
            "host": "192.168.1.51",
            "secret": "12345",
            "type": "peer",
            "username": "Juan Perez"
        },
        "user": [],
        "register": ""
}
"""
r=requests.post(host+'/trunks/', verify=False, headers= {"content-type": "application/json", "Authorization": "Bearer " + token1['access_token']}, data=troncal1)
