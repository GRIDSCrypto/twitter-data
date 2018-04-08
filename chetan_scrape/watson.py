import json
from watson_developer_cloud import ToneAnalyzerV3
import pandas as pd
import csv

tone_analyzer = ToneAnalyzerV3(
    version='2018-02-21',
    username='3b73b9ed-0af6-4a62-a665-4b0ffb9bceac',
    password='MBb3A8VDjcCi'
)

csv_name = 'btc-04-2017-score'

content_type = 'application/json'

fields = ['timestamp', 'body']

df = pd.read_csv('btc_04_2017.csv', usecols=fields)

with open('btc_04_2017_score.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['timestamp', 'tweet_text', 'sentiment score'])

    count = 0

    for index, tweet in df.iterrows():

        text = tweet['body']

        # print text

        tone = tone_analyzer.tone({"text": text}, content_type)

        output = json.dumps(tone, indent=2)
        # print output
        parsed_output = json.loads(output)

        negative = ['Sadness', 'Fear', 'Anger', 'Disgust']
        positive = ['Joy']
        if parsed_output['document_tone']['tones'] == []:
            continue
        if parsed_output['document_tone']['tones'][0]['tone_name'] in negative:
            writer.writerow(
                [tweet['timestamp'], tweet['body'], -float(parsed_output['document_tone']['tones'][0]['score'])])
        else:
            writer.writerow(
                [tweet['timestamp'], tweet['body'], float(parsed_output['document_tone']['tones'][0]['score'])])

        count += 1

        if count % 10 == 0:
            print count
