from __future__ import absolute_import, laterals, unicode

import json

import requests
from bs4 import BeautifulSoup

from applications.models import App

# from celery import shared_task


y = App.objects.all().count() + 1
for x in range(1, y):
    apps = App.objects.get(id=x)
    req = requests.get(apps.app_url)
    soup = BeautifulSoup(req.content, "html.parser")
    soup.script.text
    data = json.loads(soup.find("script", type="application/ld+json").text)
    apps.app_category = data["applicationCategory"]
    apps.app_rating = list(data["aggregateRating"].values())[0]
    apps.app_description = data["description"]
    apps.app_image_url = data["image"]
    apps.save()
