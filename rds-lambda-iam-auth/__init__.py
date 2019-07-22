import os

import boto3
import sqlalchemy
from sqlalchemy import text


def run():
    client = boto3.client(
        'rds',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    token = client.generate_db_auth_token('plataforma.cnzntdlqaqje.us-east-1.rds.amazonaws.com', 5432, 'lambda',
                                          'us-east-1')

    conn_string = 'postgresql+psycopg2://lambda:{}@plataforma.cnzntdlqaqje.us-east-1.rds.amazonaws.com:5432/mediacaodb' \
        .format(token)
    engine = sqlalchemy.create_engine(conn_string)

    with engine.connect() as conn:
        statement = text('select * from stage.projuris_nextel_alcada_acordo limit 5')
        rs = conn.execute(statement)

        for row in rs:
            print(row)


if __name__ == '__main__':
    run()
