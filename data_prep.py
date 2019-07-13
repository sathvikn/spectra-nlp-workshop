import numpy as np
import pandas as pd 
import os
from nltk import TweetTokenizer
import re

def get_twint_data(df):
    tweet_col = df['tweet']
    processed_tweets = [process_tweet(t) for t in tweet_col]
    return pd.DataFrame({'tweet': processed_tweets, 'score': np.ones(len(processed_tweets))})


def get_sent140_data(df):
    pos_tweets = df[df['score'] == 4][['tweet', 'score']]
    pos_tweets['score'] = np.zeros(len(pos_tweets.index))
    pos_tweets['tweet'] = [process_tweet(t) for t in pos_tweets['tweet']]
    return pos_tweets

def process_tweet(t):
    tokens = tknzr.tokenize(t)
    tokens = [remove_emoji(t) for t in tokens]
    tweet = ' '.join(tokens)
    return tweet

def remove_emoji(word):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    word = RE_EMOJI.sub(r'', word)
    return word

if __name__ == "__main__":
    depress = 'twint -s depression --since 2019-07-07 -o depression.csv --csv'
    anxiety = 'twint -s anxiety --since 2019-07-07 -o anxiety.csv --csv'
    os.system(depress)
    os.system(anxiety)

    dep = pd.read_csv('depression.csv')
    anx = pd.read_csv('anxiety.csv')
    tknzr = TweetTokenizer(preserve_case=False, reduce_len=True, strip_handles=True)
    dep_df = get_twint_data(dep)
    anx_df = get_twint_data(anx)
    s140 = pd.read_csv('trainingandtestdata/training.1600000.processed.noemoticon.csv', 
                    names = ['score', 'UID', 'timestamp', 'query', 'username', 'tweet'],
                    encoding = 'latin-1')
    pos_df = get_sent140_data(s140)
    train = pd.concat([pos_df, dep_df, anx_df])
    train.to_csv('data.csv')