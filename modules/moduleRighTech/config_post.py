""" docstring """
HOST = 'https://app.rightech.io'
PATH = '/api/v1/geofences'
TYPE_TOKEN = 'Bearer'

# Перенести все стили с полученой геозоны
# Если True  - перенесет все стили из полученной зоны
# Если False - применит к создаваемой геозоне параметры определенные ниже
DEFAUL_GEOFENSE_PARAMS = True

# Если DEFAUL_GEOFENSE_PARAMS = False
# То к названию геозоны добавим постфикс
GEOFENSE_NAME_POSTFIX = ' копия'

GEOFENSE_NAME = 'Зона проката #1'
GEOFENSE_COLOR = '#3cc1d4'
GEOFENSE_STYLE_FILLOPACITY = 0.2
GEOFENSE_STYLE_OPACITY = 0.75
GEOFENSE_STYLE_WEIGHT = 2
GEOFENSE_SHAPE_TYPE = "polygon"
