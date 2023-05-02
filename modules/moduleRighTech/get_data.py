""" docstring """
import os
import requests
from dotenv import load_dotenv, find_dotenv
from modules.moduleRighTech.config_get import HOST, PATH, TYPE_TOKEN, ID_GEOFENCE

load_dotenv(find_dotenv())
TOKEN_API = os.environ.get("TOKEN_API")

URL = HOST + PATH + ID_GEOFENCE

payload = {}

headers = {
    'Authorization': f'{TYPE_TOKEN} {TOKEN_API}'
}


def get_data():
    """ docstring """
    response = requests.get(
        URL,
        headers=headers,
        data=payload,
        timeout=12
    )
    print('1) Получение данных о геозоне:\n', response)
    return response.json()
