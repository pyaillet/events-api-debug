#!/usr/bin/env python3

import base64
import requests
from requests.auth import HTTPBasicAuth
import json

class AkeneoClient:
    def __init__(self, client_id, secret, username, password, host):
        self.client_id = client_id
        self.secret = secret
        self.username = username
        self.password = password
        self.host = host

    def get_token(self):
        headers = {
            "Content-Type": "application/json",
        }
        
        payload = {
            "grant_type": "password",
            "username": username,
            "password": password
        }
        res = requests.post(
                "https://{}/api/oauth/v1/token".format(host),
                data=json.dumps(payload),
                headers=headers,
                auth=HTTPBasicAuth(client_id, secret))
        
        self.token = res.json()['access_token']

    def get_products(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(self.token)
        }

        res = requests.get(
                "https://{}/api/rest/v1/products".format(host),
                params={"limit":"100","attributes":"name"},
                headers=headers)
        self.product_identifiers = [p['identifier'] for p in res.json()['_embedded']['items']]

    def toggle_product_enabled(self, enabled):
        patch_list = [json.dumps({
                "identifier": identifier, 
                "enabled": enabled
            }) for identifier in self.product_identifiers]
        payload = "\n".join(patch_list)
    
        headers = {
            "Content-Type": "application/vnd.akeneo.collection+json",
            "Authorization": "Bearer {}".format(self.token)
        }
    
        requests.patch(
                "https://{}/api/rest/v1/products".format(host),
                data=payload,
                headers=headers)

# the values are fake but representatives to give some insight
client_id = '6_4h58cz2rfsao0kosowwo4ccccs4koo0484ogc448wsw044sg4g'
secret = '3u6ov39op728048sc4k00gkg4s84w44kwo8w80k8os8cog0oss'
username = 'inject_1143'
password = '6469b1440'
host = 'your-pim.platform.url'

client = AkeneoClient(client_id, secret, username, password, host)

client.get_token()
client.get_products()

for i in range(0, 100):
    client.toggle_product_enabled(True)
    client.toggle_product_enabled(False)
