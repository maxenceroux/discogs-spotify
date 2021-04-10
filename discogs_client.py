import requests
from dotenv import load_dotenv
import time
from urllib.parse import parse_qsl
import os
import uuid

load_dotenv()


class DiscogsClient:
    def __init__(self):
        self.key = os.environ["DISCOGS_KEY"]
        self.secret = os.environ["DISCOGS_SECRET"]
        self.url = os.environ["DISCOGS_URL"]

    def get_token(self):
        url = f"{self.url}/oauth/request_token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f'OAuth oauth_consumer_key="{self.key}", oauth_signature_method="PLAINTEXT",oauth_timestamp="{int(time.time())}",oauth_nonce="{uuid.uuid4().hex}",oauth_signature="{self.secret}&"',
            "User-Agent": "discogs-spotify/1.0",
        }
        response = requests.request("GET", url, headers=headers)
        token = dict(parse_qsl(response.content.decode("utf-8")))["oauth_token"]
        token_secret = dict(parse_qsl(response.content.decode("utf-8")))[
            "oauth_token_secret"
        ]
        return token, token_secret

    def get_access_token(self, oauth_token):
        url = f"{self.url}/oauth/access_token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f'OAuth oauth_consumer_key="{self.key}", oauth_nonce="{uuid.uuid4().hex}",oauth_token="{oauth_token}",oauth_signature="{self.secret}&",oauth_signature_method="PLAINTEXT",oauth_timestamp="{int(time.time())}",oauth_verifier="users_verifier',
            "User-Agent": "discogs-spotify/1.0",
        }
        response = requests.request("POST", url, headers=headers)
        print(response.content)

    def search(self, query, token=None):
        url = f"{self.url}/database/search?q={query}"
        if token:
            headers = {"Authorization": f"Discogs token={token}"}
        else:
            headers = {"Authorization": f"Discogs key={self.key}, secret={self.secret}"}
        response = requests.request("GET", url, headers=headers)
        return response.json()