import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_detail_info(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # 事業所の名称の取得
    jigyosho_name = soup.find(text="事業所の名称").find_next().text.strip()

    # 所在地の取得
    address = soup.find(text="所在地").find_next().text.strip()

    # 連絡先の取得
    tel = soup.find(text="電話番号").find_next().text.strip()
    fax = soup.find(text="FAX番号").find_next().text.strip()

    # 事業所の管理者の氏名及び職名の取得
    manager_name = soup.find(text="氏名").find_next().text.strip()
    manager_position = soup.find(text="職名").find_next().text.strip()

    # スクレイピング取得日を取得
    detail_fetch_date = datetime.now().strftime('%Y-%m-%d')

    # 公表日を取得
    kouhyou_date = soup.select_one('div.date').text.split('公表')[0].strip()

    # 介護保険事業所番号の取得
    jigyosho_cd = url.split('JigyosyoCd=')[1].split('-')[0]

    return {
        'jigyosho_cd': jigyosho_cd,
        'jigyosho_name': jigyosho_name,
        'address': address,
        'tel': tel,
        'fax': fax,
        'manager_name': manager_name,
        'manager_position': manager_position,
        'detail_fetch_date': detail_fetch_date,
        'kouhyou_date': kouhyou_date
    }