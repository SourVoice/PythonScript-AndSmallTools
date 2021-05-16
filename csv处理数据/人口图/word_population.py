import json
from countries_codes import get_country_code

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':  # 查找所有字典key为Year的字典，
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))  # 通过json发现字典中value的值为字符串，需要转换成int或，但是有小数的情况需要先用float
        # print(country_name + ':' + str(population))
        code = get_country_code(country_name)
        if code:
            print(code + ":" + str(population))
        else:
            print('Error - ' + country_name)
