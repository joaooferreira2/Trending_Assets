import creds
from numpy import add
import pandas as pd
import alpaca_trade_api as tradeapi
import datetime as dt
from psaw import PushshiftAPI
from get_assets_table import *

# date format YYYY/MM/DD
start_date = int(dt.datetime(2021, 7, 24).timestamp())

assets_table = get_assets()

mentions_table = get_mentions(assets_table, start_date)

top_mentions_table = get_topMentions(mentions_table)

# Save to an excel spreadsheet (Optional)
'''UNCOMENT THE FOLLOWING LINE TO SAVE TO AN EXCEL FILE / SUBSTITUTE 'PATH' FOR A DESTINATION PATH'''
# top_mentions.to_excel(r'PATH', index = False)