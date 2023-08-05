# from .fetch import fetch_detail_info

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from libs.adnorm import full_norm
from .models import insert_data
from utils import iso8601


def url_convert(url):
    detail_data_url = url.replace("kani", "kihon")
    return detail_data_url


def get_soup(url):    
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def fetch_company_detail(data_url):
    
    company_soup = get_soup(data_url).find("div", id="tableGroup-1").find("table")

    def extract(soup):

        result_dict = {}
        for soup_td in soup.find_all("td"):
            soup_th = soup_td.find_previous("th")
            th = soup_th.text.split(',')[0].strip()
            td = soup_td.text.strip()
            if "法人番号" in th or td:
                if "法人等の種類" in th:
                    result_dict["company_type"] = td
                elif "法人番号" in th:
                    if td: result_dict["company_code"] = td
                    else: result_dict["company_code"] = "無"
                elif "所在地" in th and td.startswith("〒"):
                    result_dict["company_postal_code"] = td.replace("〒", "")
                elif "所在地" in th and not td.startswith("〒"):
                    result_dict["company_address"] = full_norm(td)
                elif "電話番号" in th:
                    result_dict["company_tel"] = td
                elif "ＦＡＸ番号" in th:
                    result_dict["company_fax"] = td
                elif "ホームページ" in th:
                    result_dict["company_url"] = td
                elif "氏名" in th:
                    result_dict["company_repr"] = td.replace("\u3000", " ")
                elif "職名" in th:
                    result_dict["company_repr_position"] = td
                elif "設立年月日" in th:
                    result_dict["company_established_date"] = \
                        datetime.strptime(td, "%Y/%m/%d").date()
                               
        return result_dict
    
    return extract(company_soup)
                
        # return {
        #     'company_cd': company_cd,
        #     'company_name': company_name,
        #     'company_postal_code': company_postal_code,
        #     'company_address': company_address,
        #     'company_tel': company_tel,
        #     'company_fax': company_fax,
        #     'company_repr': company_repr,
        #     'company_repr_position': company_repr_position,
        #     'detail_fetch_date': detail_fetch_date,
        #     'kouhyou_date': kouhyou_date
        # }


def fetch_jigyosyo_detail(base_data_url):
    
    
    detail_data_url = url_convert(base_data_url)
    soup = get_soup(detail_data_url)
    
    release_datetime = iso8601.from_jp_time(soup.find("p").text.split()[0])

    #事業所の名称の取得
    # jigyosyo_name_tag = soup.find(string="施設の名称").find_next().find_next().find_next()
    # jigyosyo_name = jigyosyo_name_tag.text.strip()

    # 所在地の取得
    jigyosyo_address_tag = soup.find(string="所在地").find_next()
    jigyosyo_address_full = jigyosyo_address_tag.find_next().text.strip()
    jigyosyo_postal_code = jigyosyo_address_full.split('\u3000')[0].replace('〒', '').strip()
    jigyosyo_address = jigyosyo_address_full.replace('〒' + jigyosyo_postal_code, '').strip()
    jisyosyo_address_normalized = full_norm(jigyosyo_address)
    
    # 連絡先の取得
    jigyosyo_tel = soup.find(string="電話番号").find_next().text.strip()
    jigyosyo_fax = soup.find(string="FAX番号").find_next().text.strip()

    # 事業所の管理者の氏名及び職名の取得
    jigyosyo_repr = soup.find(string="氏名").find_next().text.strip().replace("\u3000", " ")
    jigyosyo_repr_position = soup.find(string="職名").find_next().text.strip()

    # スクレイピング取得日を取得
    detail_fetch_datetime = datetime.now().replace(microsecond=0)

    # 公表日を取得
    # kouhyou_date_div = soup.select_one('div.jigyosyoHeaderButtons.noPrint p')
    # if kouhyou_date_div:
    #     kouhyou_date_str = kouhyou_date_div.text.split('\xa0')[0].strip()  # ノーブレークスペースで分割
    #     kouhyou_date = datetime.strptime(kouhyou_date_str, '%Y年%m月%d日%H:%M').strftime('%Y-%m-%d')
    # else:
    #     kouhyou_date = None

    # 介護保険事業所番号の取得
    jigyosyo_cd = base_data_url.split('JigyosyoCd=')[1].split('-')[0]

    return {
        "release_datetime": release_datetime,
        'jigyosyo_cd': jigyosyo_cd,
        # 'jigyosyo_name': jigyosyo_name,
        'jigyosyo_postal_code': jigyosyo_postal_code,
        'jigyosyo_address': jisyosyo_address_normalized,
        'jigyosyo_tel': jigyosyo_tel,
        'jigyosyo_fax': jigyosyo_fax,
        'jigyosyo_repr': jigyosyo_repr,
        'jigyosyo_repr_position': jigyosyo_repr_position,
        'detail_fetch_datetime': detail_fetch_datetime,
    }



def fetch_detail(base_data_url):
    
    detail_data_url = url_convert(base_data_url)
    print(f"~~~~~~~~~~~{detail_data_url}~~~~~~~~~~~~~~~~~")
    
    return {
        **fetch_jigyosyo_detail(detail_data_url),
        **fetch_company_detail(detail_data_url),
    }


def run():
    # 例としてのURL。実際にはデータベースや他のソースから取得することを想定しています。
    DATABASE = 'sqlite:///db/out/kk_jigyosyo.db'
    TABLE_NAME = "list_table"
    
    insert_data(DATABASE, TABLE_NAME, fetch_detail)
    
    # jigyosyo_mixed_info = fetch_detail(base_data_url)
    # print(jigyosyo_mixed_info)

    # ここでデータベースへの保存処理などを実装することができます。

run()