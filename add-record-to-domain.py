#!/usr/bin/env python3
 
import requests
import json

uri = 'http://127.0.0.1:8081/api/v1/servers/localhost/zones/example.com'
headers = { 'X-API-Key':  'api-secret-authoritative' }
 
payload = {
    "rrsets": [
        {
            "name": "hola.example.com.",
            "type": "TXT",
            "ttl": 3600,
            "changetype": "REPLACE",
            "records": [
                {
                    "content": '"Hello world"',
                    "disabled": False,
                }
            ],
            "comments": []
        }
    ]
}
 
r = requests.patch(uri, data=json.dumps(payload), headers=headers)
print(r.text)
