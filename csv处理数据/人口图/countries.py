from pygal_maps_world.maps import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    """获取所有的国别码， 并按字母顺序排序"""
    print(country_code, COUNTRIES[country_code])
