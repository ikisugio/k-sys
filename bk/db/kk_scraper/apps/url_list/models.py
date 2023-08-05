from sqlalchemy import (
    create_engine,
    Table,
    Column,
    String,
    DateTime,
    Date,
    MetaData,
    UniqueConstraint,
)
from sqlalchemy.exc import IntegrityError
from db.test import url_lists_data
from datetime import date, datetime


def create_table(engine):
    metadata = MetaData()
    
    # テーブルを作成
    my_table = Table('list_table', metadata,
        Column('jigyosyo_cd', String),
        Column('jigyosyo_name', String),
        Column('jigyosyo_url', String),
        Column('url_fetch_datetime', DateTime),
        Column('detail_fetch_datetime', DateTime),
        Column('jigyosyo_postal_code', String),
        Column('jigyosyo_address', String),
        Column('jigyosyo_tel', String),
        Column('jigyosyo_fax', String),
        Column('jigyosyo_repr', String),
        Column('jigyosyo_repr_position', String),
        Column('release_datetime', DateTime),
        Column('company_type', String),
        Column('company_code', String),
        Column('company_postal_code', String),
        Column('company_address', String),
        Column('company_tel', String),
        Column('company_fax', String),
        Column('company_url', String),
        Column('company_repr', String),
        Column('company_repr_position', String),
        Column('company_established_date', Date),
        UniqueConstraint('jigyosyo_cd', 'jigyosyo_name', name='uix_1')  # 両方が一緒に重複している場合にエラー
    )


    metadata.create_all(engine)

    return my_table


def hydrate(data_object):
    # データベースへの接続を作成
    engine = create_engine('sqlite:///db/out/kk_jigyosyo.db')

    # テーブル作成（存在しない場合）
    my_table = create_table(engine)
    with engine.begin() as connection:
        try:
            ins = my_table.insert().values(
                detail_fetch_datetime=data_object.get('detail_fetch_datetime', None),
                jigyosyo_cd=data_object['jigyosyo_cd'],
                jigyosyo_name=data_object['jigyosyo_detail']['jigyosyo_name'],
                jigyosyo_url=data_object['jigyosyo_detail']['jigyosyo_url'],
                url_fetch_datetime=datetime.now().replace(microsecond=0),
                jigyosyo_postal_code=data_object.get('jigyosyo_postal_code', ''),
                jigyosyo_address=data_object.get('jigyosyo_address', ''),
                jigyosyo_tel=data_object.get('jigyosyo_tel', ''),
                jigyosyo_fax=data_object.get('jigyosyo_fax', ''),
                jigyosyo_repr=data_object.get('jigyosyo_repr', ''),
                jigyosyo_repr_position=data_object.get('jigyosyo_repr_position', ''),
                release_datetime=data_object.get('release_datetime', None),
                company_type=data_object.get('company_type', ''),
                company_code=data_object.get('company_code', ''),
                company_postal_code=data_object.get('company_postal_code', ''),
                company_address=data_object.get('company_address', ''),
                company_tel=data_object.get('company_tel', ''),
                company_fax=data_object.get('company_fax', ''),
                company_url=data_object.get('company_url', ''),
                company_repr=data_object.get('company_repr', ''),
                company_repr_position=data_object.get('company_repr_position', ''),
                company_established_date=data_object.get('company_established_date', None)
            )
            connection.execute(ins)
        except IntegrityError as e:
            print(f"Error occurred: {e}")



def update_detail_table(data):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE detail_table SET
        detail_fetch_datetime = ?,
        jigyosyo_postal_code = ?,
        jigyosyo_address = ?,
        jigyosyo_tel = ?,
        jigyosyo_fax = ?,
        jigyosyo_repr = ?,
        jigyosyo_repr_position = ?,
        kouhyou_date = ?,
        company_type = ?,
        company_code = ?,
        company_postal_code = ?,
        company_address = ?,
        company_tel = ?,
        company_fax = ?,
        company_url = ?,
        company_repr = ?,
        company_repr_position = ?,
        company_established_date = ?
    WHERE jigyosyo_cd = ? AND jigyosyo_name = ?
    """, (
        data['detail_fetch_datetime'],
        data['jigyosyo_postal_code'],
        data['jigyosyo_address'],
        data['jigyosyo_tel'],
        data['jigyosyo_fax'],
        data['jigyosyo_repr'],
        data['jigyosyo_repr_position'],
        data['kouhyou_date'],
        data['company_type'],
        data['company_code'],
        data['company_postal_code'],
        data['company_address'],
        data['company_tel'],
        data['company_fax'],
        data['company_url'],
        data['company_repr'],
        data['company_repr_position'],
        data['company_established_date'],
        data['jigyosyo_cd'],
        data['jigyosyo_name']
    ))

    connection.commit()
    connection.close()