import pytest

from analysis.config import Config


@pytest.fixture(scope='session')
def config() -> Config:
    return Config('example.toml')
