from twitterscraper import query_tweets
import csv
import datetime as dt 

if __name__ == '__main__':

	#take in input for which year to scrape. no error checking 
	month = raw_input("What month do you want? Enter numeric value\n")
	year = raw_input("What year do you want? The csv file will be named btc_<month_year>.csv \n")
	start_date = dt.date(int(year), int(month), 1,)
	print month
	end_date = dt.date(int(year), int(month), 31)
	csv_name = 'btc_' + month + "_" + year + '.csv'

	#opening csv file to write 
	with open(csv_name, 'wb') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',')
		writer.writerow(["url", "timestamp", "owner_name", "owner_link", "type", "body", "parent", "likes", "retweets"])

		counter = 0
		#looping over query results to write to csv file 
		for tweet in query_tweets("Bitcoin OR BTC OR btc OR bitcoin", None, start_date, end_date, lang='en'):
			#only grab information for bitcoin in the text of the tweet. ignoring the username
			if "bitcoin" in tweet.text.lower() or "btc" in tweet.text.lower(): 
				url = "https://twitter.com" + tweet.url.encode('utf-8')
				timestamp = tweet.timestamp
				owner_name = tweet.user.encode('utf-8')
				owner_link = "https://twitter.com/" + tweet.user.encode('utf-8')
				tweet_type = "post"
				body = tweet.text.replace(u'\xa0', u' ').encode('utf-8')
				parent = tweet.user.encode('utf-8')
				likes = tweet.likes.encode("utf-8")
				retweets = tweet.retweets.encode("utf-8")
				tempArr = [url, timestamp, owner_name, owner_link, tweet_type, body, parent, likes, retweets]
				writer.writerow(tempArr)
				counter += 1
				if counter % 10000 == 0:
					print counter
