import requests
import time

f = open("nations.txt", "r")
nations = f.read().splitlines()
f.close

user = nations.pop(0)

for x in nations:
    nat = x.split(",")

    headers = {"User-Agent": user, "X-Password": nat[1]}

    ping = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi?nation={}&q=ping".format(nat[0]), headers=headers)
    time.sleep(0.6)
    print(ping)
