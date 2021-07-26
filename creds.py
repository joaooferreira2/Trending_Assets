from dotenv import load_dotenv
import os

load_dotenv()

#pushshift.io API
PUSH_USER = os.getenv("PUSH_USER")
PUSH_ID = os.getenv("PUSH_ID")
PUSH_SECRET = os.getenv("PUSH_SECRET")

#Alpaca API
ALP_USER = os.getenv("ALP_USER")
ALP_ID = os.getenv("ALP_ID")
ALP_SECRET = os.getenv("ALP_SECRET")
ALP_ENDPOINT = os.getenv("ALP_ENDPOINT")

