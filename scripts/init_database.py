import argparse
import gzip
import json
import subprocess
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

CLIENT = MongoClient()
DB = CLIENT['social_database_test']
path = './tweets_04_06_07.json'
KGENERAL = ["is_quote_status", "in_reply_to_status_id",
            "in_reply_to_user_id", "id", "favorite_count", "retweeted",
            "retweet_count", "lang", "created_at"]
KENTITIES = ["hashtags"]
KUSER = ["id", "followers_count", "statuses_count",
         "friends_count", "screen_name", "favourites_count", "name",
         "created_at"]


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
            counter += 1
            t = dict()
            t['general'] = {}
            t['user'] = {}

            for k in KGENERAL:
                t['general'][k] = tweet[k]

            e = tweet['entities']
            tags = [tag['text'] for tag in e['hashtags']]
            t['hashtags'] = tags

            u = tweet['user']
            for k in KUSER:
                t['user'][k] = u[k]

            table.insert_one(t)

            if counter % 1000 == 0:
                print 'Inserted ' + str(counter) + ' records'

        print 'Total records inserted: ' + str(counter)


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
        subprocess.call(['python', 'preprocesser.py', args.path])
        fill_database(path='./' + args.path.split('/')[-1] + '.json.gz')
    else:
        fill_database(path=args.path)
