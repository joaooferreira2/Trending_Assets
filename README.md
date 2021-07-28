## About Trending_Assets 

After the GameStop frenzy, a lot of people have been wondering what stocks are trending on Reddit. If you are one of these people, this program might help you get some nice information on what stocks and other assets are popping from the famous subreddit 'WallStreetBets'.

Original Author: https://github.com/hackingthemarkets

Trending_Assets Author: https://github.com/joaooferreira2

The original version, wallstreetbets-tracker, used a PostgreSQL database to store the data for possible assets and assets mentions. 

The version Trending_Assets used Pandas Dataframe to store the data for possible assets and assets mentions. In addition, the version Trending_Assets will return a dataframe already sorted with the TOP mentions, so no need to query a Database to find the most commented stocks.

## Current Development ##

So far this program will only provide you the assets mentions that appear on the title of the posts for WallStreetBets. The development is still ongoing and I plan to add more features to include comments and more Subreddits.

## Requirements

1. Install python - https://www.python.org/downloads/
2. Install pandas - pip install pandas
3. Install psaw   - pip install psaw
5. Install Alpaca - pip install alpaca-trade-api
5. Get your Alpaca API credentials 
   a. Sign up and Log in to https://alpaca.markets/
   b. Go to paper trading api
   c. Generate New Keys



