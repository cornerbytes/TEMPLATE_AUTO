#!/usr/bin/env python3
import requests
import sys
# script for automation submit flag

URL = "https://ctf-gemastik.ub.ac.id/api/flag"
TOKEN = "XXXXX"
HEADERS = {
    'Authorization': '{}'.format(TOKEN),
    'Content-Type': 'application/json',
}

def submit_flag(data):
    res = requests.post(URL, json=data)

    if res.status_code == 401:
        print("unathorized : token salah :", res.json())
    elif res.status_code == 200:
        print("succes submit flag")
    else:
        print('error code', res.json())

if __name__ == "__main__":
    try:random_hex = sys.argv[1]
    except: print('usage ./list_player.py {random_hex}');exit()
    data = {
        "flags": [f"GEMASTIK{{{random_hex}}}", f"GEMASTIK{{{random_hex}}}"]
    }
    print(f"random-hex : {sys.argv[1]}")
    submit_flag(data)
