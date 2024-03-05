#!/usr/bin/python3
"""reddit api"""


def number_of_subscribers(subreddit):
    """Querie Reddit API and returns  subscribers
"""
    import requests

    respon = requests.get("https://www.reddit.com/r/{}/about.json"
                          .format(subreddit),
                          headers={"User-Agent": "My-User-Agent"},
                          allow_redirects=False)
    if respon.status_code >= 300:
        return 0

    return respon.json().get("data").get("subscribers")
