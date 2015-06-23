#!/usr/bin/env python2

import requests, json, time, random

DONATE_URL = 'http://at.gcommer.com/donate?server={}&token={}'
DELAY_SECS = 10
AGARIO_HEADERS = {
    'Origin': 'http://agar.io',
    'Referer': 'http://agar.io',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0'
}

regions_modes = json.loads(requests.get('http://m.agar.io/info').text)["regions"]
regions = filter(lambda r: ':' not in r, regions_modes.keys())

while True:
#    print "Try: ",
    resp = requests.post('http://m.agar.io/',
                         headers=AGARIO_HEADERS,
                         data=random.choice(regions)).text
    server, token = resp.strip().split('\n')

#    print "connect(\"ws://{}\", \"{}\")\r".format(server, token)

    requests.get(DONATE_URL.format(server, token))

    time.sleep(DELAY_SECS)
