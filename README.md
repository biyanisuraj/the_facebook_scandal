# Social-Network-Analysis

## Books/Articles/Papers/Tools
* Articles
    * [Twitter and social network analysis](http://datadrivenjournalism.net/news_and_analysis/twitter_and_social_network_analysis)
    * [Esempio di utilizzo di gephy e twitter su referendum ed influencer](http://www.misurarelacomunicazione.it/2016/11/24/iovotono-vs-bastaunsi-gli-influencers-twitter/)
    * [Social network analysis of Twitter](http://www.mediative.com/social-network-analysis-twitter/)
	* [Data Mining for Predictive Social Network Analysis](https://www.toptal.com/data-science/social-network-data-mining-for-predictive-analysis)
	* [Network analysis on Clinton Wikileaks data, by MIT](https://clinton.media.mit.edu/clinton#)
    * [A social network analysis of Twitter: Mapping the digital humanities community](https://www.tandfonline.com/doi/full/10.1080/23311983.2016.1171458) 
	
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
- stream rate?

* How many tweets have already been tweeted about for example \#deletefacebook?

Consideration: since, as seen in [this link](https://gist.github.com/brendano/1024217), tweets are represented in a dictionary-like data structure, we only have to store the key-value couples that are meaningful for our pourposes. Having users for nodes and tweets/retweets for links we only have to store the users IDs and the infos about 
