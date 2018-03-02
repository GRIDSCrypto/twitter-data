from twitterscraper import query_tweets
import csv

if __name__ == '__main__':

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Bitcoin", 1):
        print(tweet.text)
