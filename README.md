# Social-Network-Analysis

![Unipi](https://img.shields.io/badge/Unipi-Social%20Network%20Analysis-orange.svg) ![Python Version](https://img.shields.io/badge/python-2.7-brightgreen.svg)

## Books/Articles/Papers/Tools
* Articles
    * [Twitter and social network analysis](http://datadrivenjournalism.net/news_and_analysis/twitter_and_social_network_analysis)
    * [Esempio di utilizzo di gephy e twitter su referendum ed influencer](http://www.misurarelacomunicazione.it/2016/11/24/iovotono-vs-bastaunsi-gli-influencers-twitter/)
    * [Social network analysis of Twitter](http://www.mediative.com/social-network-analysis-twitter/)
	* [Data Mining for Predictive Social Network Analysis](https://www.toptal.com/data-science/social-network-data-mining-for-predictive-analysis)
	* [Network analysis on Clinton Wikileaks data, by MIT](https://clinton.media.mit.edu/clinton#)
    * [A social network analysis of Twitter: Mapping the digital humanities community](https://www.tandfonline.com/doi/full/10.1080/23311983.2016.1171458) 
    * [Articolo analisi su \#deletefacebook in Italia](https://socialrecap.it/2018/03/26/deletefacebook-ci-credono-media-non-gli-italiani/)
	
* Papers 
    * [Classifying Twitter Topic-Networks Using Social Network Analysis](http://journals.sagepub.com/doi/full/10.1177/2056305117691545)
    * [Towards More Systematic Twitter Analysis: Metrics for Tweeting Activities](https://www.researchgate.net/publication/235632738_Towards_More_Systematic_Twitter_Analysis_Metrics_for_Tweeting_Activities)
    * [The Anatomy of a Scientific Rumor (Higgs boson on twitter)](https://www.nature.com/articles/srep02980#methods), qua il [dataset](https://snap.stanford.edu/data/higgs-twitter.html)

* Books
    * [Mastering Social Media Mining with Python](https://www.amazon.it/Mastering-Social-Media-Mining-Python/dp/1783552018/ref=sr_1_1?ie=UTF8&qid=1521482811&sr=8-1&keywords=Mastering+Social+Media+Mining+with+Python)

* Tools
    * [Twitter's Search Bar](https://twitter.com/search-home)
    * [Network repository](http://networkrepository.com/)
    * [Hashtagify](http://hashtagify.me/hashtag/deletefacebook)


## Possible Topics

* DataScience 
	* \#datascience \#AI ...
	* \#facebookgate \#CambridgeAnalytica \#Zuckerberg \#deletefacebook
	* \#privacy \#GDPR

* Politics	
    * Elections
    * Parties
    * Single politicians

* Communities
    * Software communities
    * Town/cities
    * 

* Music

* Brands

* People
    * Popular public persons


## Questions for Rossetti

* Technical 
    * Which library should we use to extract the data/tweets? There is an alternative way to extract tweets about a specific subject without having to setup the full Twitter API?

* Theoretical
    * Which kind of analysis should we do on the obtained dataset? Should we simply apply the metrics seen during the class? There is a preferred path to follow (like the one seen in the paper for example)? 
    
    
    
## Various
Let's begin thinking about quantities.

Full size of a tweet: ~2KB [link to measure the size of a tweet](https://gist.github.com/brendano/1024217)
to be checked, storing in json format?

* How many tweets can we store easily?
	* 100K	tweets 	~200MB
	* 500K	tweets 	~1GB
	* 1M 	tweets 	~2GB
* How much time to build the network? 

* Stream rate?

* How many tweets have already been tweeted about for example \#deletefacebook?

Consideration: since, as seen [here](https://gist.github.com/brendano/1024217), tweets are represented in a dictionary-like data structure, we only have to store the key-value couples that are meaningful for our pourposes. Having a network that has users for nodes and tweets/retweets for links, we only need to store users IDs and infos on the connections between the tweets. However it may be very useful to take a look about all the metadata that comes with a single tweet, in order to see which of the various fields may be used to obtain a richer analysis. Having choosen the kind of infos we want to store, using a compression algorithm like gzip or similar should make the task of storing the data a bit simpler.
