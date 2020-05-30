from googleapiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv("YT_API")
print(SECRET_KEY)


api_key = SECRET_KEY

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.channels().list(
    part='statistics',
    forUsername='schafer5',
    # forUsername='techguyweb',
)

response = request.execute()

print(response)
