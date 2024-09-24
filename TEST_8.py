from boxsdk import OAuth2, Client
import pandas as pd
import cx_Oracle
import oracledb

# Replace with your Box API credentials and file ID
CLIENT_ID = 'rt9xai0co6uvf8tswejjh12gjk0ypsgv'
CLIENT_SECRET = 'FWEl7S3SN6rvrgPF5bGJc4BobK0WB1z7'
ACCESS_TOKEN = 'esYNMuYFlOf1GamI1cfLhsmGGkAjsdRK'
FILE_ID = '1615528134921'  # Extracted from the URL



# Authenticate with Box
oauth2 = OAuth2(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, access_token=ACCESS_TOKEN)
client = Client(oauth2)


file = client.file(FILE_ID).get()
file_content = file.content()