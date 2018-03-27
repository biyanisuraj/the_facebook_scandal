# What are the nodes and edges of our network(s)?

The entities contained in Twitter are users and tweets, which can have various relations.

The set of entities selected to be analysed has been chosen with a topic approach based on a set of hashtags.

H = Set of hashtags = {\#facebookgate \#CambridgeAnalytica \#Zuckerberg \#deletefacebook , ...}

* Other hashtags to include? How to well-choosing this set? 

* we collect all (how many? which percentage?) of the tweets about H ?

Set of entities upon which builting the network:

TA = {all the tweets containing an h in H and the tweet authors, in a period of time T}
(A indicates authors)

The interaction between people, which permits the spreading of ideas, 
is based on the following possible reactions:

R = Set of reactions = { retweet, reply, like, share }

Other possible reactions may comprehend also unfollowing, start following or blocking a user, or segnalating a tweet.

TR = Set of people reacting 

So in general we have various possibilities, but we have to start retrieving

W = TA + UR

So, besides TA we have also to retrieve UR,  choosing the type of reaction.

* How to retrieve all the people reacting to a tweet?

* Can we combine the different reactions? Which is the difference between the reactions?

* Which is the period of time to consider?

The possible networks links/nodes of the network

- follow a user / users
- be followed by a user / users
- write a tweet about some topic(hashtag) / only the authors of the tweets 
- retweet a tweet / users or tweets 
- hashtags co-occurrence in a tweet / nodes are hashtags
- reply to a tweet / users
- ego-centric network: all people who follow a person
- ...


## Retweets (or other reactions)
If an user A retweets a tweet of an user B there is a directed link:

A -- retweets --> B (or the other side <-- is retweeted --)

The real connection is user--> tweet, because the user "agrees" with the tweet,
but maybe he don't have a strong tie with the user B. 
For example is quite possible he doesn't follow the "author". 
But to have homogenous nodes we can consider the relation user A --> user B

* Each user may write more than one tweet.
We shoul consider this fact in counting  the number of retweets?, 
or better:
we have to count the retweets per user or the retweets per tweet?

* Technical: how to retrieve who retweeted a tweet?

## Following/Followers

We can also consider only the set TA of the tweets and authors about our topic, 
and consider the network of the authors, linked by the following relation

Nodes: authors of the tweets about H
Edges: following/followed relation

## Hashtags network

We can built also a network of hashtags:

nodes: hashtags
edges: co-occurrence in a tweet
This is an undirected network.





