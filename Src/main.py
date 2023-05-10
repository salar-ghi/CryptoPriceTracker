import requests
import json
import time
from django.db import models


class Crypto(models.Model):
    name = models.CharField(max_length = 50)
    symbol = models.CharField(max_length = 10)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


api_url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
api_key = "YOUR_API_KEY" # Replace with your own API key from coinmarketcap
api_params = {
"start": 1,
"limit": 10,
"convert": "USD"
}