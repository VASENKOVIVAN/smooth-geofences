""" docstring """
from modules.moduleRighTech.get_data import get_data
from modules.moduleRighTech.post_data import post_data
from modules.moduleTranformation.transformation import transformation

# Получаем данные о геозоне
arrData = get_data()

# Получаем массив преобразованных точек
arrResult = transformation(arrData['shape']['points'])

# Пушим скругленную геозону в RighTech
if arrResult:
    post_data(arrResult,  arrData)
else:
    print('(error) - Массив преобразованных точек пустой')
