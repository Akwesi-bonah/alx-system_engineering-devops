#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers """

import requests


def number_of_subscribers(subreddit):
    """Function to return the number of subscribers"""

    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)\
    Gecko/20100101 Firefox/72.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    else:
        return response.json().get('data').get('subscribers')


if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    print(number_of_subscribers(subreddit))
