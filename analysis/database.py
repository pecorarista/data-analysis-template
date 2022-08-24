import psycopg2


def get_tablenames(uri: str, prefix: str) -> list[str]:
    query = f'''
        select
            relname
        from
            pg_stat_user_tables
        where
            relname like '{prefix}%'
        order by
            relname
    '''
    with psycopg2.connect(uri) as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return [tablename[0] for tablename in cursor.fetchall()]
