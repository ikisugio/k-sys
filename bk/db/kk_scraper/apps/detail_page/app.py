from .fetch import fetch_detail_info

def run():
    # 例としてのURL。実際にはデータベースや他のソースから取得することを想定しています。
    url = "https://www.kaigokensaku.mhlw.go.jp/01/index.php?action_kouhyou_detail_010_kihon=true&JigyosyoCd=0175701069-00&ServiceCd=331"
    
    info = fetch_detail_info(url)
    print(info)

    # ここでデータベースへの保存処理などを実装することができます。
