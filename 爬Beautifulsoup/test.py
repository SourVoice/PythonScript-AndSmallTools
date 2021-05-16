import json
import time

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'x-requested-with': 'XMLHttpRequest',
    'cookie': '__cfduid=d546b0b5a8ba2da503347818a6322f2641617941583; first_visit_datetime_pc=2021-04-09+13:13:03; yuid_b=FkWTMzI; p_ab_id=1; p_ab_id_2=2; p_ab_d_id=621411936; __utmz=235335808.1617941588.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=235335808; _gid=GA1.2.1173019886.1617941635; _ga=GA1.2.1464357566.1617941588; device_token=f2fe7523c011d6bbcba071582ce33cdb; c_type=18; a_type=0; b_type=1; login_ever=yes; first_visit_datetime=2021-04-09+13:22:01; webp_available=1; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=67283210=1^9=p_ab_id=1=1^10=p_ab_id_2=2=1^11=lang=zh=1^20=webp_available=yes=1; nexagesuid=6372b00f363d4d2cb0f7f30d216db141; OX_plg=pm; __gads=ID=0df794a4a9e1a594:T=1617942167:S=ALNI_Ma1ky4nch_fFhxlFKwnC17NPWb24Q; cto_bundle=NPOIrV82Uld1OHVrSTNKbEdaTDdwbHRYRHdua2hnd3pwZVExMDFvOFpjemJTR01FU0JyVU5CYnlNbkpHdnpYMkZad3NXdEFLUGMxUkNab0dWZVQ0JTJCcVl5d1JPN1BqdXZ5Z2h3WHFFVFNTdWlZTmZSMlklMkZNUkFFb3NMcUM1N2U1a042S0VvNWRvTWpiQXRVOHVhcm9TZEdpdk9nJTNEJTNE; limited_ads={"t_header":"","t_footer":"11615~11614","responsive":""}; categorized_tags=-L-4bBqjrT~IVwLyT8B6k~OEXgaiEbRa~cpt_Nk5mjc~k-zn4iqKyb; PHPSESSID=67283210_tEXUb739TpwbSbhCHY7XhZYAK3qGn4HH; privacy_policy_agreement=2; __utma=235335808.1464357566.1617941588.1618038754.1618046072.8; tags_sended=1; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~SoxapNkN85~B9VsvJr9Z4~svKogfYWcS~f4V1aCLsyM~5OXRF8yfCA~HY55MqmzzQ~3lxarAOIYi~FRANJWabF9~uW5495Nhg-~pzzjRSV6ZO~-InT1j9djd~XDEWeW9f9i~YjR-YYfhXC~ETjPkL0e6r~LtW-gO6CmS~zEhl6jZjnh~L7-FiupSjg~x7TOrRFRLe~dce-_1EGyq~eVxus64GZU~BtXd1-LPRH~bnY9G94VGN~5oPIfUbtd6~wmxKAirQ_H~Cp5keYns6b~FMm2p3LsNa~03-N2pXILG~OUkihvwBMZ~4-_9de7LBH~cpt_Nk5mjc~8HRshblb4Q~9FHTGgTPQV~dlfkwgDL8s~0Sds1vVNKR~chZEwesQ_3~l5WYRzHH5-~RybylJRnhJ~mqf4KYn6Dx~9FdW67Hfv1~1Xn1rApx2-~tlI9YiBhjp~Oa9b6mEc1T~Cr3jSW1VoH~zwQBF4Mob8~s60GJ0Ed-R~PTyxATIsK0~IfTHG7cZ8v~I5npEODuUW~uIrOmQSYhK~5gCuAOMc6Z~k-zn4iqKyb~BuqZZCHUEc~dJhzkwjS8s~SeMFZ9eRdc~PfIKKVs5MO~hTrcyk7mwx; __cf_bm=17c4b50307823a69a467bd7361cd2550d95551a2-1618048119-1800-Aft0kAX+PVLMcddj04fh4eGFy7VS8cbbGQmjfZB4zKbV9mjKg9VlTZhigS0xoz6+lRtFVyQcQUYzNmdlra3L4ifkLIOqxRT84vIXd+HicafJeHInzADwY2MDoBsAhmjOaGNxxIrSKbdkLpyd1uoaKHt4szy70+yXBTHRY+8t8xFKrYJvzBFR8OTf/ycUOZAmtQ==; __utmt=1; __utmb=235335808.23.10.1618046072'
}

url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust&p='
page_url = []
for page in range(3, 10):
    page_url.append(url + str(page))


def get_html(each):
    response = requests.get(url=each, headers=headers)
    print(response.text)
    time.sleep(4)


for each in page_url:
    get_html(each)
