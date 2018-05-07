import argparse
from pymongo import MongoClient
from pymongo.errors import CollectionInvalid

# USAGE:
#   python merge_collection.py -c col1 col2 col3 ... colN
#   MERGES ALL COLi WITH 2 <= i <= N IN COL1 AND SAVES THE FINAL COLLECTION
#   WITH A NAME GIVE BY THE USER.


def merge_tags(l1, l2):
    for t1 in l1:
        if t1 not in l2:
            l2.append(t1)

    return l2


def merge_collections(col_list, drop):
    client = MongoClient()
    db = client['social_database_test']
    base_table = db[col_list[0]]
    cursor = base_table.find()

    new_collection_name = raw_input('FINAL COLLECTION NAME: ')

    try:
        db.create_collection(new_collection_name)
    except CollectionInvalid:
        db.drop_collection(new_collection_name)
        db.create_collection(new_collection_name)

    new_collection = db[new_collection_name]

    print 'USING ' + col_list[0] + ' AS BASE COLLECTION (' + \
        str(base_table.find().count()) + ' records)'

    # HERE WE FILL THE NEW COLLECTION WITH ALL THE RECORDS FROM THE BASE
    # COLLECTION

    for tweet in cursor:
        new_collection.insert_one(tweet)

    while len(col_list) != 1:
        new_users, found_users = 0, 0
        to_merge = col_list.pop()
        cursor = db[to_merge].find()

        print 'MERGING COLLECTION ' + to_merge + ', ' + str(cursor.count()) + \
            ' RECORDS'

        for tweet in cursor:
            u = new_collection.find({'id': tweet['id']})
            if u.count() == 0:

                # THIS STEP IS NECESSARY IN ORDER TO AVOID CONFILITS RELATED
                # TO DUPLICATE ObjectIds BETWEEN RECORDS

                new_u = dict()

                for k in tweet.keys():
                    if k == '_id':
                        continue
                    else:
                        new_u[k] = tweet[k]

                new_collection.insert_one(new_u)
                new_users += 1
            else:
                new_collection.find_one_and_update(
                    {'id': u[0]['id']},
                    {'$inc': {
                        'tweets': u[0]['tweets'],
                        'retweets': u[0]['retweets'],
                        'favorite_count': u[0]['favorite_count']
                    },
                        '$set': {
                        'hashtags': merge_tags(u[0]['hashtags'],
                                               tweet['hashtags'])
                    }
                    }
                )

                found_users += 1

        print 'NEW USERS: ' + str(new_users) + ', FOUND USERS ' + \
            str(found_users)

        if drop:
            db.drop_collection(to_merge)

    print 'FINAL COLLECTION HAS ' + str(new_collection.find().count()) + \
        ' RECORDS'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--collections', action='store', nargs='+',
                        help='The collections that have to be merged.')
    parser.add_argument('-d', '--drop', action='store_true',
                        help='If flagged states that all the collection given \
                        in input have to be dropped at the end of the merging \
                        procedure.')
    args = parser.parse_args()

    merge_collections(col_list=args.collections, drop=args.drop)
