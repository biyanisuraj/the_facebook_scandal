# The Facebook scandal

![Unipi](https://img.shields.io/badge/Unipi-Social%20Network%20Analysis-orange.svg) ![Python Version](https://img.shields.io/badge/python-2.7-brightgreen.svg) ![Mongodb Version](https://img.shields.io/badge/mongodb-v3.6.4-ff69b4.svg)

This repository contains the code base for the [Social Network Analysis](https://elearning.di.unipi.it/course/view.php?id=114) course hosted by the Master's degree in Computer Science of the University of Pisa. 

## The case story
On Saturday 17th of March 2018, The New York Times and The Guardian / The Observer broke reports on how the consulting  firm Cambridge
Analytica harvested private information from the Facebook profiles of more than 50 million users without their permission, making it one 
of the largest data leaks in the social network’s history. 

Cambridge Analytica described itself as a company providing consumer research,
targeted advertising and other data-related services to both political and corporate clients. The whistleblower Christopher Wylie,
datascientist and former director of research at Cambridge Analytica revealed to the Observer how Cambridge Analytica used personal
information taken without authorisation in early 2014 to build a system that could profile individual US voters, in order to target them 
with personalised political advertisements. 

Christopher Wylie, who worked with a Cambridge University academic to obtain the data, told 
the Observer: 

>“_We exploited Facebook to harvest millions of people’s profiles. And built models to exploit what we knew about them and 
target their inner demons. That was the basis the entire company was built on._”

## The network
We have considered a network composed by the authors of tweets about the case, during the  first period of the scandal outbreak.
The data have been collected via the Twitter API and we built the network using the following consecutive steps:
  1. Crawling of all the available tweets over a period of more than 15 days, since the 17th of March, containing at least one of the 
  most popular hashtags regarding the case:
     * __#cambridgeanalytica__ 
     * __#facebookgate__
     * __#deletefacebook__ 
     * __#zuckerberg__
  2. Cleaning of the crawled tweets, by selecting and storing in a MongoDB database only the users informations about the authors of 
  tweets, excluding retweets and mentions.
  3. Selection of the case outbreak time period by observing the 
  [time history](https://github.com/germz01/the_facebook_scandal/blob/master/scripts/network_analysis/imgs/time_history.pdf). 
  The selected time period consists of 8 days, from the 17th to the 24th of March included (considering the Italian timezone).
  4. Crawling of the following list for each of the selected authors, extracting the following/follower relationships.
