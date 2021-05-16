string = """illust_ids[]: 83708121
illust_ids[]: 76066275
illust_ids[]: 83451316
illust_ids[]: 66580027
illust_ids[]: 79748832
illust_ids[]: 47621790
illust_ids[]: 80616033
illust_ids[]: 32740714
illust_ids[]: 68126965
illust_ids[]: 73939373
illust_ids[]: 34844544
illust_ids[]: 79026576
illust_ids[]: 68322571
illust_ids[]: 83493912
illust_ids[]: 66877708
illust_ids[]: 78533060
illust_ids[]: 88887343
illust_ids[]: 77890738
illust_ids[]: 82352123
illust_ids[]: 78265237
illust_ids[]: 71314896
illust_ids[]: 70875247
illust_ids[]: 82432221
illust_ids[]: 78256101
lang: zh"""
string_list = string.split('\n')
print(string_list)
for string in string_list:
    dict_s = {string.split(':')[0]: string.split(':')[-1]}
