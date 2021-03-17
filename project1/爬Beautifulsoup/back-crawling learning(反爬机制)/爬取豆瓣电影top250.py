import requests
from lxml import etree
from multiprocessing.dummy import Pool

cookie = 'bid=N3Zqe_FFUKc; douban-fav-remind=1; viewed="27093751"; ' \
         '_vwo_uuid_v2=D401F17C96234AE149C4E04B78C3C8066|6fcc3cefe576bff2b89cdf28c4c5f597; ' \
         '__gads=ID=21cdec44606b00df-2250ba4d7ac4009b:T=1604034713:RT=1604034713:S=ALNI_Mb6iYJKYfbUjLxlisTQX5HCODTGKg' \
         '; gr_user_id=fb6ac40c-94c3-400e-b170-47e126a9b78a; _gid=GA1.2.1520341169.1612004212; ' \
         '_ga=GA1.2.645228582.1602221486; ll="108288"; ' \
         'UM_distinctid=17752f076e4530-0b6eef25ebabba-f7b1332-1fa400-17752f076e57f0; ' \
         'Hm_lvt_19fc7b106453f97b6a84d64302f21a04=1612004228; Hm_lpvt_19fc7b106453f97b6a84d64302f21a04=1612004253; ' \
         'ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1612004299%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; ' \
         '_pk_ses.100001.4cf6=*; __utma=30149280.645228582.1602221486.1611225800.1612004300.9; ' \
         '__utmb=30149280.0.10.1612004300; __utmc=30149280; __utmz=30149280.1612004300.9.9.utmcsr=google|utmccn=(' \
         'organic)|utmcmd=organic|utmctr=(not%20provided); ' \
         '__utma=223695111.645228582.1602221486.1612004300.1612004300.1; __utmb=223695111.0.10.1612004300; ' \
         '__utmc=223695111; __utmz=223695111.1612004300.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(' \
         'not%20provided); _pk_id.100001.4cf6=9a1bb1df4597b334.1612004299.1.1612005471.1612004299. '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/85.0.4183.83 Safari/537.36',
}

url = 'https://movie.douban.com/top250'

number_ls = []
for i in range(0, 251, 25):
    number_ls.append(i)

print(number_ls)

"""
    with open('douban.html', 'w', encoding='utf-8') as fp:
        fp.write(page_content)
"""


def get_information(number_ls):
    param = {
        'start': number_ls,
        'filter': ''
    }
    page_content = requests.get(url=url, headers=headers, params=param).text

    tree = etree.HTML(page_content)
    vedio_title = tree.xpath('//ol[@class="grid_view"]//div[@class="pic"]//a/img/@alt')
    star = tree.xpath('//ol[@class="grid_view"]//div[@class="star"]/span[@class="rating_num"]/text()')

    vedio_title_ls = []
    star_ls = []
    for i in vedio_title:
        vedio_title_ls.append(i)
    for i in star:
        star_ls.append(i)

    j = 0
    while j < len(star_ls):
        print("the movie is ", vedio_title_ls[j])
        print("the star is ", star_ls[j])
        print()
        j += 1


pool = Pool(4)
pool.map(get_information, number_ls)
