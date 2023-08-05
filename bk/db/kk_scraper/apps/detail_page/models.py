from sqlalchemy import create_engine, MetaData, Table, select, insert, update
from datetime import datetime, timedelta

def insert_data(db_path, table_name, func):
    # データベースへの接続を作成
    engine = create_engine(db_path)
    metadata = MetaData()

    # テーブルをロード
    jigyosyo_table = Table(table_name, metadata, autoload_with=engine)

    # データベースからすべてのレコードを取得
    with engine.connect() as connection:
        query = select(jigyosyo_table)
        result = connection.execute(query)
        rows = result.fetchall()

        # レコードを一時的に保存するリスト
        records_to_insert = []

        # 各行に対して
        for i, row in enumerate(rows):
            # URLを取得(row はタプルオブジェクト、データベースのカラムの3番目がURLだから row[2])
            JIGYOSYO_URL_COLUMN_ORDER = 2
            jigyosyo_url = row[JIGYOSYO_URL_COLUMN_ORDER]

            # detail_fetch_datetimeが6か月以内ならスキップ
            URL_FETCH_DATETIME_COLUMN_ORDER = 3
            DETAIL_FETCH_DATETIME_COLUMN_ORDER = 4
            fetch_datetime = row[DETAIL_FETCH_DATETIME_COLUMN_ORDER]
            
            DETAIL_FETCH_PERIOD_MONTHS = 3
            
            if fetch_datetime and fetch_datetime > datetime.now() - timedelta(months=DETAIL_FETCH_PERIOD_MONTHS):
                continue

            # URLから詳細情報を取得
            detail_info = func(jigyosyo_url)

            # レコードを一時的に保存
            records_to_insert.append(detail_info)

            # リストが10件のレコードを含む場合、それらをデータベースに挿入
            if len(records_to_insert) == 10:
                for record in records_to_insert:
                    # レコードが存在するか確認
                    query = select(jigyosyo_table).where(jigyosyo_table.c.jigyosyo_url == jigyosyo_url)
                    result = connection.execute(query)
                    existing_record = result.fetchone()

                    if existing_record:
                        # レコードが存在する場合は更新
                        query = (
                            update(jigyosyo_table).
                            where(jigyosyo_table.c.jigyosyo_url == jigyosyo_url).
                            values(**record)  # 辞書のキーと値をフィールド名と値として使用
                        )
                    else:
                        # レコードが存在しない場合は挿入
                        query = insert(jigyosyo_table).values(**record)

                    connection.execute(query)

                # リストをクリア
                records_to_insert = []

        # 全てのレコードが処理された後に残ったレコードをデータベースに挿入
        for record in records_to_insert:
            # レコードが存在するか確認
            query = select(jigyosyo_table).where(jigyosyo_table.c.jigyosyo_url == jigyosyo_url)
            result = connection.execute(query)
            existing_record = result.fetchone()

            if existing_record:
                # レコードが存在する場合は更新
                query = (
                    update(jigyosyo_table).
                    where(jigyosyo_table.c.jigyosyo_url == jigyosyo_url).
                    values(**record)  # 辞書のキーと値をフィールド名と値として使用
                )
            else:
                # レコードが存在しない場合は挿入
                query = insert(jigyosyo_table).values(**record)

            connection.execute(query)
