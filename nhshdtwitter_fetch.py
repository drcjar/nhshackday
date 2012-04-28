import twitter
import json
import os

twitter_search = twitter.Twitter(domain="api.twitter.com")


for x in range(1,101):
	print "Processing page ", x
	results = twitter_search.search(q="nhshd", page = x)
	tweets = results.get("results")
	if not tweets:
		break

	with open("data.dat", "ab") as f:
		for tweet in tweets:
			f.write(tweet['id_str']) 
			f.write(tweet["text"].encode('utf-8'))



