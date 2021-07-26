# Required Python Imports
import creds
from numpy import add
import pandas as pd
import alpaca_trade_api as tradeapi
import datetime as dt
from psaw import PushshiftAPI



def get_assets():
    # Instantiate the Alpaca API to gather Assets Data
    alpaca_api = tradeapi.REST(creds.ALP_ID, creds.ALP_SECRET, creds.ALP_ENDPOINT) ##Instantiating Alpaca trade API

    #Get a list of all assets provided by Alpaca
    assets = alpaca_api.list_assets()

    # Create a dataframe to place all the Assets Info
    assets_df = pd.DataFrame(columns=['name', 'symbol', 'exchange'])

    # Add all the assets into a Panda Dataframe
    for asset in assets:
        new_row = {'name': asset.name, 'symbol': '$' + asset.symbol, 'exchange': asset.exchange}
        assets_df = assets_df.append(new_row, ignore_index=True)

    #print a preview of the Stocks 
    # print(assets_df.head())

    return assets_df

def get_mentions(assets_df, start_date):

    # Instantiate API
    api = PushshiftAPI()

    # # Will look for posts after this date
    # date = int(dt.datetime(2021, 7, 1).timestamp())

    #Edit or Remove'limit' to get more data
    submissions = list(api.search_submissions(after=start_date, 
                            Subreddit='wallstreetbets',
                            filter=['author', 'title', 'subreddit', 'url'],
                            ))
    #Create a Dataframe to put the mentions of stock
    mentions = pd.DataFrame(columns=['mention','name', 'mention_date', 'source', 'subreddit', 'url'])

    # Iterate through all the Submisstion titles 
    for submission in submissions:
        
        #to split the words coming from
        words = submission.title.split()
        

        ##Inline function to Get the words that only starts with $ and put in an list
        cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

        #To print a list if there is at least one item that starts with $
        if len(cashtags) > 0:

            for cashtag in cashtags:
                mention = cashtag.upper()
                url_link = submission.url
                subreddit = submission.subreddit
                submitted_time = pd.to_datetime(submission.created_utc, unit = 's')
                
                if mention in assets_df.values:
                    index = assets_df.index[assets_df['symbol'] == mention].tolist()
                    index = index[0]
                    asset_name = assets_df.at[index, 'name']
                    new_row = {'mention': mention,'name': asset_name , 'mention_date': submitted_time, 'source': 'reddit','subreddit': subreddit , 'url': url_link }
                    mentions = mentions.append(new_row, ignore_index=True)
    
    # print(mentions.head())

    return mentions

def get_topMentions(mentions):

    #Group by cashtag mention and name as counts
    top_mentions = mentions.groupby(['mention', 'name']).size().reset_index(name='mentions_count')

    # Sort by counts
    top_mentions.sort_values(by=['mentions_count'], inplace=True, ascending=False, ignore_index = True)

    # Print the results
    print(top_mentions.head(20))

    return top_mentions


