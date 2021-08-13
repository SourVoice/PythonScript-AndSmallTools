import requests


class Pixiv():
    def __init__(self):
        self.url = 'https://www.pixiv.net/ranking.php'
        self.headers = {
            'cookies': 'first_visit_datetime_pc=2021-04-09+13:13:03; yuid_b=FkWTMzI; p_ab_id=1; p_ab_id_2=2; p_ab_d_id=621411936; __utmz=235335808.1617941588.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _ga=GA1.2.1464357566.1617941588; c_type=18; a_type=0; b_type=1; login_ever=yes; first_visit_datetime=2021-04-09+13:22:01; nexagesuid=6372b00f363d4d2cb0f7f30d216db141; __gads=ID=0df794a4a9e1a594:T=1617942167:S=ALNI_Ma1ky4nch_fFhxlFKwnC17NPWb24Q; cto_bundle=NPOIrV82Uld1OHVrSTNKbEdaTDdwbHRYRHdua2hnd3pwZVExMDFvOFpjemJTR01FU0JyVU5CYnlNbkpHdnpYMkZad3NXdEFLUGMxUkNab0dWZVQ0JTJCcVl5d1JPN1BqdXZ5Z2h3WHFFVFNTdWlZTmZSMlklMkZNUkFFb3NMcUM1N2U1a042S0VvNWRvTWpiQXRVOHVhcm9TZEdpdk9nJTNEJTNE; limited_ads={"t_header":"","t_footer":"11615~11614","responsive":""}; privacy_policy_agreement=2; PHPSESSID=67283210_UEsSkZoADbrQCEHqFoeaCl0fYHRB1IDm; device_token=fdb032c71b847b25c52d9d8c8828b871; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=67283210=1^9=p_ab_id=1=1^10=p_ab_id_2=2=1^11=lang=zh=1^20=webp_available=yes=1; ki_r=; tag_view_ranking=RTJMXD26Ak~Lt-oEicbBr~SoxapNkN85~B9VsvJr9Z4~svKogfYWcS~f4V1aCLsyM~5OXRF8yfCA~HY55MqmzzQ~3lxarAOIYi~FRANJWabF9~0Sds1vVNKR~uW5495Nhg-~pzzjRSV6ZO~0KixsJBDVn~QzHaAvrA-w~on24wzx7AW~AU5OlIQ9Fy~mu7939gcfy~85s1qqXlWy~SofU-3Fogt~sddUfryc0L~Hry6GxyqEm~Mf52HwdQ_f~-InT1j9djd~XDEWeW9f9i~YjR-YYfhXC~ETjPkL0e6r~LtW-gO6CmS~zEhl6jZjnh~L7-FiupSjg~x7TOrRFRLe~dce-_1EGyq~eVxus64GZU~BtXd1-LPRH~bnY9G94VGN~5oPIfUbtd6~wmxKAirQ_H~Cp5keYns6b~FMm2p3LsNa~03-N2pXILG~OUkihvwBMZ~4-_9de7LBH~cpt_Nk5mjc~8HRshblb4Q~9FHTGgTPQV~dlfkwgDL8s~chZEwesQ_3~l5WYRzHH5-~RybylJRnhJ~mqf4KYn6Dx~9FdW67Hfv1~1Xn1rApx2-~tlI9YiBhjp~Oa9b6mEc1T~Cr3jSW1VoH~zwQBF4Mob8~s60GJ0Ed-R~PTyxATIsK0~IfTHG7cZ8v~I5npEODuUW~uIrOmQSYhK~5gCuAOMc6Z~k-zn4iqKyb~BuqZZCHUEc~dJhzkwjS8s~SeMFZ9eRdc~PfIKKVs5MO~hTrcyk7mwx; _im_vid=01F5QX7E2RANSA7Q8W9TMBD27V; ki_t=1621078678653;1621078678653;1621078853484;1;4; __utma=235335808.1464357566.1617941588.1621078654.1621420473.12; __utmc=235335808; __utmt=1; __cf_bm=082ecd1077c5644cd33124abe6673017f3ab05f9-1621420472-1800-AZwTvM0smy3YVuP5j8cQSZX/DTv+620En9iLbPWLD+2VhT3dY/g+KQqS27/xeZTwGrMqVg/bx9hlPq3nkUI142eLW/4nuo05mcRz4RYgx53eiok5vSWcWuzjJHAqlVkaVjwWi7LywxVcdAlEfQf/cCHSENB2Ea7+quKaVaXve6JO4N0lN7mk53obtQtroK7Bkg==; __utmb=235335808.4.10.1621420473',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
            'referer': 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'
        }
        self.params = {
            "content": "all",
            "mode": "daily_r18",
            "p": "1",
            "date": "20210519",
            "format": "json",
        }

    def getresponse(self):
        req = requests.get(self.url, headers=self.headers, params=self.params)
        print(req.text)


if __name__ == "__main__":
    spider = Pixiv()
    spider.getresponse()
