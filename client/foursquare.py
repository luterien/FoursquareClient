import datetime
import requests
import json
import logging

from django.conf import settings


QUERY_URL = "https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=%s&near=%s&query=%s"


def make_request(query, location):

    url = build_url(query, location)

    r = requests.get(url)

    try:
        return json.loads(r.text)["response"]["venues"]
    except Exception as e:
        logging.error("json exception: " + str(e))
        return []


def build_url(query, location):

    date = datetime.datetime.now().strftime('%Y%m%d')

    return QUERY_URL % (
            settings.FOURSQUARE["client_id"], 
            settings.FOURSQUARE["client_secret"],
            date,
            location,
            query
        )
