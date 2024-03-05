#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    returns a list containing the titles
    """
    if isinstance(subreddit, list):
        url = "https://reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
              AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/122.0.0.0 Safari/537.36'}
    respons = requests.get(url, headers=head, allow_redirects=False)
    if respons.status_code != 200:
        return (None)
    respons = respons.json()
    if "data" in respons:
        data = respons.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)
