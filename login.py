import requests
import time

user = "your_main_nation"

f = open("nations.txt", "r")
nations = f.read().splitlines()
f.close

for x in nations:
    nat = x.split(",")

    headers = {"User-Agent": user, "X-Password": nat[1]}

    ping = requests.get(
        "https://www.nationstates.net/cgi-bin/api.cgi?nation=" + nat[0] + "&q=ping", headers=headers)
    time.sleep(0.6)
    print(ping)
