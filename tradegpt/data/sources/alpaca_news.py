import os
import requests
import json
from dataclasses import dataclass, asdict
from dotenv import load_dotenv
from arrow import Arrow

load_dotenv()

# Define a data class to structure the news data
@dataclass
class NewsArticle:
    author: str
    headline: str
    summary: str
    created_at: str
    updated_at: str
    url: str
    symbols: list
    content: str = ""

class AlpacaNews:
    def __init__(self):
        self.api_key_id = 'PKW5M98VOJXNN0BJKELF'
        self.api_secret_key = '2w5b3N9XvNfluWZrJwjDJ0MyLZYlmZ8EhqRr76Ou'
        self.base_url = "https://data.alpaca.markets/v1beta1/news"

    def fetch_news(self, symbols: list):
        headers = {
            'Apca-Api-Key-Id': self.api_key_id,
            'Apca-Api-Secret-Key': self.api_secret_key
        }
        response = requests.get(self.base_url, headers=headers)
        print(response)
        response_data = response.json()
        news_list = response_data.get('news', [])
        articles = [self.parse_article(article) for article in news_list[:10]]
        return articles

    @staticmethod
    def parse_article(data):
        return NewsArticle(
            author=data.get('author', ''),
            headline=data.get('headline', ''),
            summary=data.get('summary', ''),
            created_at=data.get('created_at', ''),
            updated_at=data.get('updated_at', ''),
            url=data.get('url', ''),
            symbols=data.get('symbols', []),
            content=data.get('content', '')
        )

# Example of using the AlpacaNews class
if __name__ == "__main__":
    news_source = AlpacaNews()
    latest_news = news_source.fetch_news(['COIN', 'BTCUSD'])
    print(json.dumps([asdict(article) for article in latest_news], indent=2))  # Use asdict from dataclasses