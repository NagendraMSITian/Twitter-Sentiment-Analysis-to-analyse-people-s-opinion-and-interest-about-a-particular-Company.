import urllib 
import json 
import oauth2 as oauth

ACCESS_KEY = "783888146-lqvTt8dZCxZ00QeJM3MDdDZqEZYmzCgDh3indVDi" # change the tokens PJ
ACCESS_SECRET = "aT4j0IW47GInFhFl5GUeqjifYAXLrqENiGIfWQdLJlnlD"

CONSUMER_KEY = "IZQFcr43nAf5QF689tO2Z9jh2"
CONSUMER_SECRET = "N46XQGXIwsq2q3faAK1XZ3usXeP65fr10k58vCaSsoAvpRnP8r"

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)


timeline_endpoint = "https://stream.twitter.com/1.1/statuses/sample.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for i in range(len(tweets)):
	print "tweet number "+ str(i) +" : "
	print tweets[i]["text"]