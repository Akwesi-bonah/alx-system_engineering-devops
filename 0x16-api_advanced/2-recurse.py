#!/usr/bin/python3
""" Module for storing the recurse function. """

import requests


def recurse(subreddit, hot_list=[]):
    """ Recursively returns a list of titles of all hot articles. """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)\
    Gecko/20100101 Firefox/72.0'}
    params = {'limit': 100}
    response = requests.get(url, params=params, headers=headers,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    else:
        for i in range(100):
            hot_list.append(
                response.json().get('data').get('children')
                [i].get('data').get('title'))
        return len(hot_list)


if __name__ == '__main__':
    subreddit = input("Enter a subreddit: ")
    print(recurse(subreddit))
