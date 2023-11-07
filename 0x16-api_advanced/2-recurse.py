#!/usr/bin/python3
""" Module for storing the recurse function. """

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """ Recursively returns a list of titles of all hot articles. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; '
                             'Ubuntu; Linux x86_64; rv:72.0)\
    Gecko/20100101 Firefox/72.0'}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, params=params,
                            headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list


if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    print(recurse(subreddit))
