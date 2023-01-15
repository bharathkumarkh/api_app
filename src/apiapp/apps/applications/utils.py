import json

import requests
from bs4 import BeautifulSoup


def update_app_data(instance):
    req = requests.get(instance.app_url)
    soup = BeautifulSoup(req.content, "html.parser")
    soup.script.text
    data = json.loads(soup.find("script", type="application/ld+json").text)
    instance.app_category = data["applicationCategory"]
    instance.app_rating = list(data["aggregateRating"].values())[1]
    instance.app_description = data["description"]
    instance.app_image_url = data["image"]
    instance.save()
    return instance
