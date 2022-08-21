from pathlib import Path
from typing import Union

import toml


class Database:
    def __init__(
        self,
        user: str,
        password: str,
        host: str,
        port: int,
        dbname: str
    ) -> 'Database':
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        self.uri = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.dbname}'


class Config:
    def __init__(self, filename: Union[Path, str]) -> 'Config':
        config = toml.load(filename)
        db = config['database']
        self.database = Database(db['user'], db['password'], db['host'], db['port'], db['dbname'])
