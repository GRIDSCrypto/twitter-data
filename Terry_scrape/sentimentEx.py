# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import time
import csv

# Instantiates a client
client = language.LanguageServiceClient()

tweets_body = [] # array for storing the body of the tweets
tweets_timestamp = [] #array for storing timestamps of the tweets

#open csv file to gather the tweet and timestamp into arrays
with open('btc_7_2017.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		body = row[5]
		timestamp = row[1]
		if body != "body":
			tweets_body.append(body)
		if timestamp != "timestamp":
			tweets_timestamp.append(timestamp)

#writing everything into a new file to write with sentiment score 
#columns will be timestamp, text, sentiment score
#sentiment score ranges from -1 to 1 
with open('btc_7_2017_gcp_sentiment.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(["timestamp", "tweet_text", "sentiment score"])
	counter = 0
	for i in range(0, len(tweets_body)):
		# The text to analyze
		text = tweets_body[i]
		timestamp = tweets_timestamp[i]
		try:
			document = types.Document(content=text,type=enums.Document.Type.PLAIN_TEXT)

			# Detects the sentiment of the text
			sentiment = client.analyze_sentiment(document=document).document_sentiment
		except Exception:
			pass

		#writing to csv now
		writer.writerow([timestamp, text, sentiment.score])
		counter += 1

		#sleeping due to 600 request per minute quota by google
		if counter % 550 == 0:
			print("sleeping")
			time.sleep(60)