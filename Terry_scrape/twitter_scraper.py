from twitterscraper import query_tweets
import csv
import datetime as dt 

if __name__ == '__main__':

	#opening csv file to write 
	with open('btc_2012.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(["url", "timestamp", "owner_name", "owner_link", "type", "body", "parent"])

		#grabbing twitter data for specified year 
		for tweet in query_tweets("Bitcoin OR BTC OR btc OR bitcoin", None, dt.date(2012,1,1), dt.date(2012,12,31), lang='en'):
			url = "https://twitter.com" + tweet.url.encode('utf-8')
	    	timestamp = tweet.timestamp
	    	owner_name = tweet.user.encode('utf-8')
	    	owner_link = "https://twitter.com/" + tweet.user.encode('utf-8')
	    	tweet_type = "post"
	    	body = tweet.text.replace(u'\xa0', u' ')
	    	parent = tweet.user.encode('utf-8')
	    	tempArr = [url, timestamp, owner_name, owner_link, tweet_type, body, parent]
	    	writer.writerow(tempArr)
