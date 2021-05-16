import requests
import json
import urllib.request

session = requests.session()
target_headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36',
    'referer': 'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page',
    'cookie': '__cfduid=d546b0b5a8ba2da503347818a6322f2641617941583; first_visit_datetime_pc=2021-04-09+13%3A13%3A03; yuid_b=FkWTMzI; p_ab_id=1; p_ab_id_2=2; p_ab_d_id=621411936; __utmz=235335808.1617941588.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=235335808; _gid=GA1.2.1173019886.1617941635; _ga=GA1.2.1464357566.1617941588; device_token=f2fe7523c011d6bbcba071582ce33cdb; c_type=18; a_type=0; b_type=1; login_ever=yes; first_visit_datetime=2021-04-09+13%3A22%3A01; webp_available=1; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=67283210=1^9=p_ab_id=1=1^10=p_ab_id_2=2=1^11=lang=zh=1^20=webp_available=yes=1; nexagesuid=6372b00f363d4d2cb0f7f30d216db141; OX_plg=pm; __gads=ID=0df794a4a9e1a594:T=1617942167:S=ALNI_Ma1ky4nch_fFhxlFKwnC17NPWb24Q; cto_bundle=NPOIrV82Uld1OHVrSTNKbEdaTDdwbHRYRHdua2hnd3pwZVExMDFvOFpjemJTR01FU0JyVU5CYnlNbkpHdnpYMkZad3NXdEFLUGMxUkNab0dWZVQ0JTJCcVl5d1JPN1BqdXZ5Z2h3WHFFVFNTdWlZTmZSMlklMkZNUkFFb3NMcUM1N2U1a042S0VvNWRvTWpiQXRVOHVhcm9TZEdpdk9nJTNEJTNE; limited_ads=%7B%22t_header%22%3A%22%22%2C%22t_footer%22%3A%2211615~11614%22%2C%22responsive%22%3A%22%22%7D; categorized_tags=-L-4bBqjrT~IVwLyT8B6k~OEXgaiEbRa~cpt_Nk5mjc~k-zn4iqKyb; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~uW5495Nhg-~pzzjRSV6ZO~-InT1j9djd~XDEWeW9f9i~YjR-YYfhXC~ETjPkL0e6r~LtW-gO6CmS~zEhl6jZjnh~L7-FiupSjg~x7TOrRFRLe~dce-_1EGyq~eVxus64GZU~BtXd1-LPRH~bnY9G94VGN~5oPIfUbtd6~wmxKAirQ_H~Cp5keYns6b~FMm2p3LsNa~03-N2pXILG~OUkihvwBMZ~4-_9de7LBH~cpt_Nk5mjc~8HRshblb4Q~9FHTGgTPQV~dlfkwgDL8s~0Sds1vVNKR~chZEwesQ_3~l5WYRzHH5-~RybylJRnhJ~mqf4KYn6Dx~9FdW67Hfv1~1Xn1rApx2-~tlI9YiBhjp~Oa9b6mEc1T~Cr3jSW1VoH~B9VsvJr9Z4~zwQBF4Mob8~SoxapNkN85~s60GJ0Ed-R~PTyxATIsK0~IfTHG7cZ8v~I5npEODuUW~uIrOmQSYhK~5gCuAOMc6Z~k-zn4iqKyb~BuqZZCHUEc~dJhzkwjS8s~SeMFZ9eRdc~PfIKKVs5MO~hTrcyk7mwx; PHPSESSID=67283210_tEXUb739TpwbSbhCHY7XhZYAK3qGn4HH; privacy_policy_agreement=2; __utma=235335808.1464357566.1617941588.1618038754.1618046072.8; __utmt=1; tags_sended=1; __cf_bm=a1a9e5ab4d575f921ad3773a03cb1213c8fdbdaf-1618046080-1800-AUFs6q92Y5lpsq7JU3aduIdIvkA/fQtlBvZnRQjejjxuI8JwC4SZ/evgqpLOFnNXaE7pHfpU6uWS91FSW4ZvhatqwQxv7pZbljztA0Eo2BFg; __utmb=235335808.3.10.1618046072'
}


class GetDownload(object):
    def __init__(self):
        self.login_url = 'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page'
        self.login_headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
            'referer': 'https://accounts.pixiv.net/',

            'cookie': '__cfduid=d546b0b5a8ba2da503347818a6322f2641617941583; first_visit_datetime_pc=2021-04-09+13%3A13%3A03; yuid_b=FkWTMzI; p_ab_id=1; p_ab_id_2=2; p_ab_d_id=621411936; __utmz=235335808.1617941588.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=235335808; _gid=GA1.2.1173019886.1617941635; _ga=GA1.2.1464357566.1617941588; device_token=f2fe7523c011d6bbcba071582ce33cdb; c_type=18; a_type=0; b_type=1; login_ever=yes; first_visit_datetime=2021-04-09+13%3A22%3A01; webp_available=1; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=67283210=1^9=p_ab_id=1=1^10=p_ab_id_2=2=1^11=lang=zh=1^20=webp_available=yes=1; nexagesuid=6372b00f363d4d2cb0f7f30d216db141; OX_plg=pm; __gads=ID=0df794a4a9e1a594:T=1617942167:S=ALNI_Ma1ky4nch_fFhxlFKwnC17NPWb24Q; cto_bundle=NPOIrV82Uld1OHVrSTNKbEdaTDdwbHRYRHdua2hnd3pwZVExMDFvOFpjemJTR01FU0JyVU5CYnlNbkpHdnpYMkZad3NXdEFLUGMxUkNab0dWZVQ0JTJCcVl5d1JPN1BqdXZ5Z2h3WHFFVFNTdWlZTmZSMlklMkZNUkFFb3NMcUM1N2U1a042S0VvNWRvTWpiQXRVOHVhcm9TZEdpdk9nJTNEJTNE; limited_ads=%7B%22t_header%22%3A%22%22%2C%22t_footer%22%3A%2211615~11614%22%2C%22responsive%22%3A%22%22%7D; categorized_tags=-L-4bBqjrT~IVwLyT8B6k~OEXgaiEbRa~cpt_Nk5mjc~k-zn4iqKyb; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~uW5495Nhg-~pzzjRSV6ZO~-InT1j9djd~XDEWeW9f9i~YjR-YYfhXC~ETjPkL0e6r~LtW-gO6CmS~zEhl6jZjnh~L7-FiupSjg~x7TOrRFRLe~dce-_1EGyq~eVxus64GZU~BtXd1-LPRH~bnY9G94VGN~5oPIfUbtd6~wmxKAirQ_H~Cp5keYns6b~FMm2p3LsNa~03-N2pXILG~OUkihvwBMZ~4-_9de7LBH~cpt_Nk5mjc~8HRshblb4Q~9FHTGgTPQV~dlfkwgDL8s~0Sds1vVNKR~chZEwesQ_3~l5WYRzHH5-~RybylJRnhJ~mqf4KYn6Dx~9FdW67Hfv1~1Xn1rApx2-~tlI9YiBhjp~Oa9b6mEc1T~Cr3jSW1VoH~B9VsvJr9Z4~zwQBF4Mob8~SoxapNkN85~s60GJ0Ed-R~PTyxATIsK0~IfTHG7cZ8v~I5npEODuUW~uIrOmQSYhK~5gCuAOMc6Z~k-zn4iqKyb~BuqZZCHUEc~dJhzkwjS8s~SeMFZ9eRdc~PfIKKVs5MO~hTrcyk7mwx; PHPSESSID=67283210_tEXUb739TpwbSbhCHY7XhZYAK3qGn4HH; privacy_policy_agreement=2; __utma=235335808.1464357566.1617941588.1618038754.1618046072.8; __utmt=1; tags_sended=1; __cf_bm=a1a9e5ab4d575f921ad3773a03cb1213c8fdbdaf-1618046080-1800-AUFs6q92Y5lpsq7JU3aduIdIvkA/fQtlBvZnRQjejjxuI8JwC4SZ/evgqpLOFnNXaE7pHfpU6uWS91FSW4ZvhatqwQxv7pZbljztA0Eo2BFg; __utmb=235335808.3.10.1618046072'
        }

        self.Query_string_param = {
            'req_id': '63daddc4f9440af4'
        }
        self.payload = {
            "m": "d0713c513de9f7ff4e07c8defb940f43de0be116-1618046080-1800-AVijIyztrpJXHzI5jZiBokZZ94l78GENJPHu10CeQIx++2EGG1Aeq0tuIsgPGYw33J28wmUn08g/qMhgINd6Imsn7sDwL3w9AjfmL4oB0hdFgdFSGav/e4JjlnbinD2orQ==", "results": ["3a8c0e80762170e375d5dc5af93ffc48", "ad7c270da16dc2b70bbbcfab7799271d"], "timing": 71, "fp": {"id": 3, "e": {"r": [355, 635], "ar": [635, 355], "pr": 2.0000000298023224, "cd": 24, "wb": 'false', "wp": 'false', "wn": 'false', "ch": 'true', "ws": 'false', "wd": 'false'}}
        }

    def login_act(self):
        req_target = session.post(url=self.login_url, headers=self.login_headers)
        print(req_target.text)

    def urls_(self):
        req = session.get(
            'https://www.pixiv.net/discovery',
            headers=target_headers, timeout=3)
        json_data = json.loads(req.content)
        print(json_data)


if __name__ == '__main__':
    dl = GetDownload()
    dl.login_act()
    dl.urls_()
