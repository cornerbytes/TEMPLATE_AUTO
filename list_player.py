#!/usr/bin/env python3

import requests
import sys
URL = "https://ctf-gemastik.ub.ac.id/api/user"


"""
how to usage : 
python3 list_player.py ip 
./list_player.py 
"""
if __name__ == "__main__":
    result = requests.get(URL).json()
    data_player = [i for i in result['data']]

    if len(sys.argv) > 1:
        if sys.argv[1] == 'ip':
            for i in data_player: print(f"{i['ip']}")
    else:
        for i in data_player: print(f"{i['ip']} : {i['username']}")
