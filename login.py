import argparse
import os
import time

from typing import List
from urllib.error import HTTPError
from urllib.request import urlopen, Request


class ArgList:
    user: str
    ratelimit: int


def parse_args() -> ArgList:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--user", help="Your main nation or ns email address", required=True)
    parser.add_argument(
        "-r", "--ratelimit", type=int, help="Requests per 30 second period (max 45)", default=30)

    args = ArgList()

    parser.parse_args(namespace=args)

    if args.ratelimit > 45 or args.ratelimit < 0:
        args.ratelimit = 30

    return args


def read_nations() -> List[str] | None:
    try:
        with open(f"{os.path.dirname(os.path.realpath(__file__))}/nations.txt", "r") as in_file:
            return in_file.readlines()
    except FileNotFoundError:
        print("nations.txt not found, terminating program")
        return


def login_request(user: str, nation: str, password: str):
    headers = {
        "User-Agent": f"UPC's login-py, used by {user}",
        "X-Password": password
    }

    try:
        request = Request(
            f"https://www.nationstates.net/cgi-bin/api.cgi?nation={nation.lower().replace(' ', '_')}&q=ping", headers=headers)
        urlopen(request)
    except HTTPError as error:
        if error.status == 403:
            print(f"Could not log into {nation} - incorrect password")
        elif error.status == 404:
            print(f"Could not log into {nation} - nation does not exist")
        else:
            print(
                f"Could not log into {nation} - unspecified error with code {error.status}")
    else:
        print(f"Successfully logged into {nation}")


def main():
    args = parse_args()

    data = read_nations()

    if not data:
        return

    for idx, entry in enumerate(data):
        try:
            nation, password = entry.strip().split(",")
        except ValueError:
            print(
                f"Incorrect syntax on line {idx + 1} of nations.txt: {entry}")
        else:
            login_request(args.user, nation, password)

            time.sleep(30 / args.ratelimit)


if __name__ == "__main__":
    main()
