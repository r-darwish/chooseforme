#!/usr/bin/env python3

import sys
import requests
from zlib import adler32
from bs4 import BeautifulSoup

def get_tweets(user):
    response = requests.get("http://twitter.com/" + user)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find(class_="js-tweet-text-container").text.strip()


def _choice(tweet, options):
    data = tweet + ",".join(options)
    return (adler32(data.encode("UTF-8")) & 0xffffffff) % len(options)


def main():
    options = sys.argv[1:]
    if not options:
        print("Error: Division by the number of fucks Oren Hazan gives")
        print("Usage: chooseforme.py [option ...]")
        return 1

    options = [s.lower() for s in options]
    options.sort()
    tweet = get_tweets("oren_haz")
    print(options[_choice(tweet, options)])

    return 0


if __name__ == "__main__":
    sys.exit(main())
