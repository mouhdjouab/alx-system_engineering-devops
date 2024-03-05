#!/usr/bin/python3
"""Function to count words """
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Prints counts of given words
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    head = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    param = {
        "after": after,
        "count": count,
        "limit": 100
    }
    respons = requests.get(url, headers=head, params=param,
                           allow_redirects=False)
    try:
        results = respons.json()
        if respons.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)