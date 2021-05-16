from pygal_maps_world.maps import COUNTRIES


def get_country_code(country_name):
    for code, name in COUNTRIES.items():
        if name == country_name:  # 仅获取所要国家数据
            return code
    return None  # 没找到返回NONE
