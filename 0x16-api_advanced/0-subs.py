#!/usr/bin/python3
"""
the Reddit API and returns the number
of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """returns  total subscribers"""
    url_web = ("https://api.reddit.com/r/{}/about".format(subreddit))
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    respons = requests.get(url_web, headers=header, allow_redirects=False)

    if respons.status_code != 200:
        return (0)
    respons = respons.json()
    if 'data' in respons:
        return (respons.get('data').get('subscribers'))

    else:
        return (0)
