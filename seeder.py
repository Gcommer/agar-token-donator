#!/usr/bin/env python2

import requests, json, time, random

DONATE_URL = 'http://at.gcommer.com/donate?server={}&token={}'
DELAY_SECS = 20
AGARIO_HEADERS = {
    'Origin': 'http://agar.io',
    'Referer': 'http://agar.io'
}

regions_modes = json.loads(requests.get('http://m.agar.io/info').text)["regions"]
regions = filter(lambda r: ':' not in r, regions_modes.keys())

print regions

while True:
    print "Try: ",

    resp = requests.post('http://m.agar.io/',
                         headers=AGARIO_HEADERS,
                         data=random.choice(regions)).text
    server, token = resp.strip().split('\n')

    print "connect(\"ws://{}\", \"{}\")".format(server, token)

    requests.get(DONATE_URL.format(server, token))

    time.sleep(DELAY_SECS)
