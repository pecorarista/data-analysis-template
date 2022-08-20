from typing import Any

import psycopg2


def get_tablenames(config: dict[str, Any], prefix: str) -> list[str]:

    user = config['user']
    password = config['password']
    host = config['host']
    port = config['port']
    dbname = config['dbname']

    query = f'''
        select
            relname
        from
            pg_stat_user_tables
        where
            relname like '{prefix}%'
    '''
    with psycopg2.connect(f'postgresql://{user}:{password}@{host}:{port}/{dbname}') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return [tablename[0] for tablename in cursor.fetchall()]
