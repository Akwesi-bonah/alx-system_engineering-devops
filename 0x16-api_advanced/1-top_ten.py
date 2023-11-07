#!/usr/bin/python3
"""Module to query the Reddit API and returns
the number of hot topics listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Function to return the number of hot
    topics listed for a given subreddit"""

    if subreddit is None or type(subreddit) is not str:
        print("None")
        return
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; '
                                 'Linux x86_64; rv:72.0)\
        Gecko/20100101 Firefox/72.0'}
        params = {'limit': 10}
        response = requests.get(url, params=params,
                                headers=headers,
                                allow_redirects=False)
        if response.status_code == 404:
            print("None")
            return
        else:
            results = response.json().get("data")
            [print(c.get("data").get("title"))
             for c in results.get("children")]


if __name__ == '__main__':

    subreddit = input("Enter a subreddit: ")
    print(top_ten(subreddit))
