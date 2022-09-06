import os

import pytest
from aws_lambda_powertools.utilities.typing import LambdaContext


@pytest.fixture(scope='session', autouse=True)
def aws_credentials() -> None:
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"


@pytest.fixture(scope='session')
def context() -> LambdaContext:
    return LambdaContext()
