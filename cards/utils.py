import random
import requests
from cards.models import Card


def create_deck():
    suits = [0, 1, 2, 3]
    ranks = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
    cards = [Card(suit=suit, rank=rank) for rank in ranks for suit in suits]
    Card.objects.bulk_create(cards)


def get_random_comic():
    # Get the "num" of the latest one to get the total amount of xkcd comics created
    latest_comic = requests.get("http://xkcd.com/info.0.json").json()

    # Get a random comic from all time
    random_num = random.randint(1, latest_comic['num'])
    random_comic = requests.get("http://xkcd.com/{}/info.0.json".format(random_num)).json()
    return random_comic
