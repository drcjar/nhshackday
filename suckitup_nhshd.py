"""
Sucks up the Twitter API in real-time for Tweets matching certain criteria.

e.g python suckitup_nhshd.py > nhshd.txt
"""

from tweetstream import FilterStream

with FilterStream("user_name", "password", track=["#nhshd"]) as stream:
    for tweet in stream:
                print tweet 
