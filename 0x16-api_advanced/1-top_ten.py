#!/usr/bin/python3
"""
the Reddit API and prints the titles of subreddit.
"""
import requests


def top_ten(subreddit):
    """
    prints the titles
    """
    url_web = ("https://reddit.com/r/{}?sort=hot&limit=10".format(subreddit))
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    respons = requests.get(url_web, headers=head, allow_redirects=False)

    if respons.status_code != 200:
        print(None)
        return
    respons = respons.json()
    if 'data' in respons:
        for posts in respons.get('data').get('children'):
            print(posts.get('data').get('title'))

    else:
        print(None)
