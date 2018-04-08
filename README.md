# twitter-data
Grids Crypto twitter 

# Scrape: Update: April 8, 2018 
Terry and Chetan both scraped twitter tweets for information about bitcoin. 
We used a twitter api here: https://github.com/taspinar/twitterscraper
Unfortantely the scraper sometimes gets a JSONdecode error and then returns 
the tweets that have been gathered so far. We would always get incomplete data.
However we still have some data. 

Data is located in google drive. Contact Adam from Grids for the data. 

# Sentiment Analysis 
Sentiment analysis was done on some of the existing data that we have
in order to get some sort of score to feed into our LSTM model created
by George and Adam. 

Terry used Google Cloud Natural Language API for sentiment analysis. 
This required setting up google cloud on his local machine. Steps
can be found on google. The sentiment analysis was quick but there were 
limits on how many API calls we could make and ultimately led to incomplete 
sentiment analysis data. Pricing constraints as well as daily usage constraints. 

Chetan used IBM Watsons sentiment anaylsis. He could only get a lite version to work, 
which limit the speed to about 1/sec. 

We both got experience using different sentiment analysis programs out there 
and that was the best takeaway of the project. 

Ultimately we decided not to feed in any tweet sentiments to our model. 
Something we can do for the future is to create a our own sentiment analysis
so that things could be done much faster. However with finals coming up
we have decided to stop here. 