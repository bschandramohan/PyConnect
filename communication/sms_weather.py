import os

from twilio.rest import Client  # For Sending SMS
import requests  # For Rest calls
from dotenv import load_dotenv

OMDB_API_URL = "http://www.omdbapi.com/"


load_dotenv()
omdb_key = os.getenv("omdb_api_key")
twilio_sid = os.getenv("twilio_sid")
twilio_api_key = os.getenv("twilio_api_key")
twilio_from_number = os.getenv("twilio_from_number")
twilio_to_number = os.getenv("twilio_to_number")

print(twilio_sid)
print(type(twilio_sid))

movie_name = "luca"
movie_response = requests.get(f"{OMDB_API_URL}?t={movie_name}&apikey={omdb_key}")
print(movie_response.json())


client = Client(twilio_sid, twilio_api_key)
message = client.messages.create(
    body=f"{movie_response.json()}",
    from_=twilio_from_number,
    to=twilio_to_number
)

print(message.status)
