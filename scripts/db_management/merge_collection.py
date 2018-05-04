import argparse
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid


def merge_tags(l1, l2):
    for t1 in l1:
        if t1 not in l2:
            l2.append(t1)

    return l2


def merge_collections(col_list):
    client = MongoClient()
    db = client['social_database_test']
    base_table = db[col_list[0]]
    new_users, found_users = 0, 0
    cursor = base_table.find()

    try:
        db.create_collection('merged')
    except CollectionInvalid as e:
        db.drop_collection('merged')
        db.create_collection('merged')

    new_collection = db['merged']

    print 'USING ' + col_list[0] + ' AS BASE COLLECTION (' + \
        str(base_table.find().count()) + ' records)'

    for tweet in cursor:
        new_collection.insert_one(tweet)

    while len(col_list) != 1:
        to_merge = col_list.pop()
        cursor = db[to_merge].find()

        print 'MERGIND COLLECTION ' + to_merge + ', ' + \
            str(cursor.count()) + ' RECORDS'

        for tweet in cursor:
            u = base_table.find({'id': tweet['user']['id']})
            if u.count() == 0:
                new_collection.insert_one(tweet)
                new_users += 1
            else:
                u['general']['tweets'] += tweet['general']['tweets']
                u['general']['retweets'] += tweet['general']['retweet']
                u['general']['favorite_count'] += tweet['general']['favorite_count']
                u['hashtags'] = merge_tags(u['hashtags'], tweet['hashtags'])

                new_collection.insert_one(u)
                found_users += 1
        print 'Merged collection ' + to_merge + ' with collection ' + \
            col_list[0]
        print 'New Users: ' + str(new_users) + ', Found Users ' + \
            str(found_users)

    print 'FINAL COLLECTION HAS ' + str(new_collection.find().count()) + \
        ' RECORDS'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--collections', action='store', nargs='+',
                        help='The collections that have to be merged.')
    args = parser.parse_args()

    merge_collections(col_list=args.collections)
