def car_info(manufacturer, car_type, **other_infos):
    info = {}
    info['manu'] = manufacturer
    info['type'] = car_type
    for key, value in other_infos.items():
        info[key] = value
    return info

result = car_info('subaru', 'outback', color='blue', tow_package=True)
print(result)