import datetime as dt
from get_assets_table import *

# date format YYYY/MM/DD
start_date = int(dt.datetime(2021, 11, 25).timestamp())

# Collect Returned Assets from the Alpaca API and place in a Pandas Dataframe 
assets_table = get_assets()

# Collect all the mentions of stock from the Reddit API and add to the Mentions Dataframe
mentions_table = get_mentions(assets_table, start_date)

# Sort the Mentions Datafra
top_mentions_table = get_topMentions(mentions_table)

# Save to an excel spreadsheet (Optional)
'''UNCOMENT THE FOLLOWING LINE TO SAVE TO AN EXCEL FILE / SUBSTITUTE 'PATH' FOR A DESTINATION PATH'''
# top_mentions.to_excel(r'PATH', index = False)