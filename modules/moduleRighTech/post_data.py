""" docstring """
import os
import json
import requests
from dotenv import load_dotenv, find_dotenv
from modules.moduleRighTech.config_post import \
    HOST, \
    PATH, \
    TYPE_TOKEN, \
    GEOFENSE_NAME,\
    GEOFENSE_COLOR, \
    GEOFENSE_STYLE_FILLOPACITY, \
    GEOFENSE_STYLE_OPACITY, \
    GEOFENSE_STYLE_WEIGHT, \
    GEOFENSE_SHAPE_TYPE, \
    DEFAUL_GEOFENSE_PARAMS, \
    GEOFENSE_NAME_POSTFIX

load_dotenv(find_dotenv())
TOKEN_API = os.environ.get("TOKEN_API")

URL = HOST + PATH


def post_data(arr_result, arr_data):
    """ docstring """
    if DEFAUL_GEOFENSE_PARAMS:
        payload = json.dumps({
            'name': arr_data['name']+GEOFENSE_NAME_POSTFIX,
            'color': arr_data['color'],
            'style': {
                'fillOpacity': arr_data['style']['fillOpacity'],
                'opacity': arr_data['style']['opacity'],
                'weight': arr_data['style']['weight']
            },
            "shape": {
                "type": arr_data['shape']['type'],
                "points": arr_result,
            }
        })
    else:
        payload = json.dumps({
            'name': GEOFENSE_NAME,
            'color': GEOFENSE_COLOR,
            'style': {
                'fillOpacity': GEOFENSE_STYLE_FILLOPACITY,
                'opacity': GEOFENSE_STYLE_OPACITY,
                'weight': GEOFENSE_STYLE_WEIGHT
            },
            "shape": {
                "type": GEOFENSE_SHAPE_TYPE,
                "points": arr_result,
            }
        })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'{TYPE_TOKEN} {TOKEN_API}'
    }

    response = requests.post(
        URL,
        headers=headers,
        data=payload,
        timeout=12
    )

    print('\n3) Отправка новой геозоны в RighTech:\n', response)
    print('\n4) ID созданной геозоны: ', response.json()['_id'])
    return response.json()
