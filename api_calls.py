import requests
from api_key import api_key as API_KEY


def get_call(start_date):
    """The Feed date limit is only 7 Days"""

    params = {
        'start_date': start_date,
        'api_key': API_KEY
    }

    url = 'https://api.nasa.gov/neo/rest/v1/feed?'

    response = requests.get(url, params=params)
    response = response.json()
    return response
