import argparse
import gzip
import json
import numpy as np
import subprocess
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

"""
    Campi di interesse:
        favorite_count: indica quante volte il tweet e' stato likato
        is_quote_status: false se non e' un quote altrimenti true DA
        CONTROLLARE
        lang: il linguaggio del tweet
        retweeted: indica se il tweet e' stato retwettato oppure no
        retweet_count : indica quante volte il tweet e' stato retwettato
        entities.hashtags: la lista dei tag utilizzati dal tweet
        user.created_at
        user.favourites_count: numero di tweet che l'utente ha likato
        user.followers_count: numero di utenti che seguono l'utente
        user.friends_count: numero di utenti che l'utente segue
        user.id: id dell'utente
        user.name: nome utente
        user.screen_name
        user.statuses_count: numero di stati pubblicati dall'utente

"""

CLIENT = MongoClient()
DB = CLIENT['social_database_test']
KENTITIES = ["hashtags"]
KUSER = ['created_at', 'favourites_count', 'followers_count', 'friends_count',
         'id', 'name', 'screen_name', 'statuses_count']
TAGS = ['cambridgeanalytica', 'deletefacebook', 'facebook', 'facebookgate',
        'privacy', 'zuckerberg']


def fill_database(path):
    cname = path.split('/')[-1].split('.')[0]
    try:
        DB.create_collection(cname)
    except CollectionInvalid as e:
        DB.drop_collection(cname)
        DB.create_collection(cname)

    table = DB[cname]
    counter = 0

    with gzip.open(path) as f:
        tweets = json.load(f)

        for tweet in tweets['tweets']:
            if tweet['is_quote_status'] is False:
                if 'retweeted_status' not in tweet:
                    u = tweet['user']
                    e = tweet['entities']
                    tags = [tag['text'] for tag in e['hashtags']]

                    if len(tags) == 0:
                        continue
                    else:
                        tw_cursor = table.find({'id': u['id']})

                        if tw_cursor.count() == 0:
                            t = dict()
                            tags = [tg.lower() for tg in tags]
                            t['hashtags'] = np.intersect1d(tags, TAGS).tolist()

                            if len(t['hashtags']) == 0:
                                continue
                            else:
                                t['tweets'] = 1
                                t['retweets'] = tweet['retweet_count']
                                t['favorite_count'] = tweet['favorite_count']
                                t['lang'] = tweet['lang']
                                ## add date of the tweet
                                t['tweet_created_at']=tweet['created_at']

                                for k in KUSER:
                                    t[k] = u[k]

                                table.insert_one(t)
                                counter += 1

                        else:
                            tags = table.find_one({'id': u['id']})['hashtags']
                            tweet_tags = [tag['text'] for tag in e['hashtags']]
                            tweet_tags = [tg.lower() for tg in tweet_tags]
                            tweet_tags = np.intersect1d(tweet_tags,
                                                        TAGS).tolist()
                            [tags.append(t)
                             for t in tweet_tags if t not in tags]

                            table.find_one_and_update(
                                {'id': u['id']},
                                {'$inc': {'tweets': 1,
                                          'retweets': tweet['retweet_count'],
                                          'favorite_count':
                                              tweet['favorite_count']},
                                 '$set': {'hashtags': tags}})

        print 'Total tweets analyzed: ' + str(len(tweets['tweets']))
        print 'Added ' + str(counter) + ' users'
        print 'Trimmed ' + str(len(tweets['tweets']) - counter) + ' users'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', action='store', help='The path \
                        leading to the directory where the json files \
                        are stored.')
    parser.add_argument('-f', '--format', action='store_true',
                        help="Whether or not to format the directory \
                        specified by the path given by the -p argument.")
    args = parser.parse_args()

    if args.format:
        subprocess.call(['python', 'validate_json.py', args.path])
        print '\n'
        subprocess.call(['python', 'preprocesser.py', args.path])
        print '\n'
        fill_database(path='./' + args.path.split('/')[-1] + '.json.gz')
    else:
        fill_database(path=args.path)
