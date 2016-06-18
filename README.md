# Html Data Collector

## The base algorithm 
Allows for the discovery and extraction of all the pages in a web site.  The process proceeds  by downloading a single page, extracting the hrefs and queuing them further process.
The queue continues to grow (and shrink) as the algorithm performs a breadth-first search.  

## Data Logging
Data in the html pages visited is downloaded to the local file system. Url's are logged and indexed.  Duplicate url's are ignored unless the have reached the expiration period (expiriation).

### Expiration
Among the data logged, meta data including the page download time, last time indexed, number of links found etc is also collected.  The meta data allows us to provide a number of important features.  
1. Restarts can be accomplished without the algorithm loosing its place
2. Subsequent runs are faster since only new content needs to be downloaded
3. Expiration routines based on the last time downloaded can be implemented

## Tor Integration
To prevent detection as a bot, tor integration is available to allow requests to be routed through the Tor network

## Threaded IO for Downloads

## Multi Core Support

## Hadoop Support

## Enironment Setup
First, lets get the code. cd to your projects folder and ...
git clone git@github.com:schwab/htmlscrape.git

VirtualEnv is used to isolate our development (and production) environments and to ensure we don't have library conflicts, missing dependencies etc.
To setup virtualenv
 ``` 
	$ pip install virtualenv
	$ cd htmlscrape
	$ git checkout advanced
	$ virtual venv
```
To begin using the virtual environment, it needs to be activated:
```
	$ source venv/bin/activate
```
SQLAlchemy is used for data access
  * pip install 
