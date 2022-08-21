from typing import Generator

import psycopg2
import pytest

from analysis.config import Config
from analysis.database import get_tablenames


@pytest.fixture(scope='module', autouse=True)
def tablenames() -> list[str]:
    return ['x_abc', 'x_bca', 'x_cab', 'y_abc']


@pytest.fixture(scope='module', autouse=True)
def create_tables(config: Config, tablenames: list[str]) -> None:
    with psycopg2.connect(config.database.uri) as conn:
        with conn.cursor() as cursor:
            for tablename in tablenames:
                query = f'create table if not exists {tablename} (k integer)'
                cursor.execute(query)
            conn.commit()


@pytest.fixture(scope='module', autouse=True)
def drop_tables(config: Config, tablenames: list[str]) -> Generator[None, None, None]:
    yield
    with psycopg2.connect(config.database.uri) as conn:
        with conn.cursor() as cursor:
            for tablename in tablenames:
                query = f'drop table if exists {tablename} cascade'
                cursor.execute(query)
            conn.commit()


def test_database(config: Config) -> None:
    prefix = 'x_'
    results = get_tablenames(config.database.uri, prefix)
    expected = ['x_abc', 'x_bca', 'x_cab']
    assert results == expected
