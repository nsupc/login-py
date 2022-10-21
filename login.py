import json
import time

from datetime import date
from urllib.error import HTTPError
from urllib.request import urlopen, Request

headers = {}
errors = []

try:
    with open("config.json", "r") as in_file:
        headers["User-Agent"] = f"UPC's login script, being used by {json.load(in_file)['main_nation']}"

except FileNotFoundError:
    main_input = str(input("What is your main nation/NS email? "))

    data = {
        "main_nation": main_input
    }

    with open("config.json", "w") as out_file:
        json.dump(data, out_file, indent=4)

    headers["User-Agent"] = f"UPC's login script, being used by {main_input}"

def login_request(nation, password):
    try:
        headers["X-Password"] = password
        request = Request(f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation.lower().replace(' ', '_')}&q=ping", headers=headers)
        urlopen(request)
        print(f"Successfully logged into {nation}")
    except HTTPError as error:
        if error.status == 403:
            print(f"Could not log into {nation} - wrong password")
            errors.append(f"{nation} - bad password")
        elif error.status == 404:
            print(f"Could not log into {nation} - nation does not exist")
            errors.append(f"{nation} - does not exist")
    finally:
        time.sleep(0.6)

try:
    with open("nations.txt", "r") as in_file:
        nation_list = in_file.read().split("\n")
except FileNotFoundError:
    print("Please create a file called nations.txt formatted like this:\nnation1,password\nnation2,password\netc...")
else:
    for item in nation_list:
        nation, password = item.split(',')
        login_request(nation, password)

if errors:
    with open("error.txt", "w") as out_file:
        out_file.write("{0}\n{1}".format(date.today().strftime('%d/%m/%Y'), '\n'.join(errors)))
