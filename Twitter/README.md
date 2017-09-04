<H1>Twitter Scraper</H1>

**The goal of this project:**
<br>Implement scripts to fetch Tweets for given topics and perform analysis on resulting data

**Approach:**
<br>There are two .py files PythonTwitterTool_Fetch.py and Analysis.py. 
The first one is used to search and save data. The second one is used to perform relevant anyalysis.

**Running the code:**
<br>To fetch data with search_term and tweet_date:
<br>python Fetch_Tweets.py [-h] [--search_term SEARCH_TERM] [--tweet_date TWEET_DATE]
<br>optional arguments:
<br>  -h, --help            show this help message and exit
<br>  --search_term SEARCH_TERM
<br>                        search term
<br>  --tweet_date TWEET_DATE
<br>                       tweet created date in yyyy-mm-dd

<br>To show analysis results according the data fetched above
<br>python Analysis.py [-h] [--search_term SEARCH_TERM] [--min_date MIN_DATE] [--max_date MAX_DATE]
<br>optional arguments:
<br>  -h, --help            show this help message and exit
<br>  --search_term SEARCH_TERM
<br>                        search term
<br>  --min_date MIN_DATE   min date in yyyy-mm-dd
<br>  --max_date MAX_DATE   max date in yyyy-mm-dd
