import sqlite3

DATABASE_PATH = "db/out/kk_jigyosyo.db"

def create_detail_table():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # detail_table の作成
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS detail_table (
        id INTEGER PRIMARY KEY,
        jigyosho_cd TEXT NOT NULL,
        jigyosho_name TEXT NOT NULL,
        address TEXT NOT NULL,
        tel TEXT NOT NULL,
        fax TEXT NOT NULL,
        manager_name TEXT NOT NULL,
        manager_position TEXT NOT NULL
    )
    """)

    connection.commit()
    connection.close()

# テーブルの作成を実行
create_detail_table()
