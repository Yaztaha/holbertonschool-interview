#!/usr/bin/python3
""" Reddit hot article word counter """
import requests


def count_words(subreddit, word_list, hot_art=[], after=''):
    """  Reddit hot_art word counter"""
    try:
        req = requests.get('https://www.reddit.com/r/{}/hot.json?after={}'.
                           format(subreddit, after),
                           headers={'User-Agent': 'default'},
                           allow_redirects=False)
        if after is None:
            dict = {}
            for w in word_list:
                for h_w in hot_art:
                    if w == h_w:
                        if w not in dict:
                            dict[w] = 1
                        else:
                            dict[w] += 1
            for w in sorted(dict, key=dict.get, reverse=True):
                if dict[w]:
                    print('{}: {}'.format(w, dict[w]))
            return hot_art
        for at in req.json().get('data').get('children'):
            hot_art += at.get('data').get('title').lower().split()
        after = req.json().get('data').get('after')
        count_words(subreddit, word_list, hot_art, after)
        return hot_art
    except ValueError:
        return None
