| Attribute Name   | Description   |
|------------------|---------------|
| _json | This is a dictionary with the JSON response of the status |
| author | This is the tweepy.models.User instance of the tweet author
| contributors | This is a list of contributors, if the feature is enabled 
| coordinates | This is the dictionary of coordinates in the GeoJSON format
| created_at | This is the datetime.datetime instance of the tweet creation time
| entities | This is a dictionary of URLs, hashtags, and mentions in the tweets
| favorite_count | This is the number of times the tweet has been favorited
| favorited | This flags whether the authenticated user has favorited the tweet
| geo | These are the coordinates (deprecated, use coordinates instead)
| id | This is the unique ID of the tweets as big integer
| id_str | This is the unique ID of the tweet as string
| in_reply_to_screen_name | This is the username of the status the tweet is replying to
| in_reply_to_status_id | This is the status ID of the status the tweet is replying to, as big integer
| in_reply_to_status_id_str | This is the status ID of the status the tweet is replying to, as string
| in_reply_to_user_id | This is the user ID of the status the tweet is replying to, as big integer
| in_reply_to_user_id_str | This is the user ID of the status the tweet is replying to, as string
| is_quote_status | This flags whether the tweet is a quote (that is, contains another tweet)
| lang | This is the string with the language code of the tweet
| place | This is the tweepy.models.Place instance of the place attached to 
the tweet
| possibly_sensitive | This flags whether the tweet contains URL with possibly sensitive material
|retweet_count | This is the number of times the status has been retweeted
| retweeted | This flags whether the status is a retweet
| source | This is the string describing the tool used to post the status
| text | This is the string with the content of the status
| truncated | This flags whether the status was truncated (for example, retweet exceeding 140 chars)
| user | This is the tweepy.models.User instance of the tweet author (deprecated, use author instead)
