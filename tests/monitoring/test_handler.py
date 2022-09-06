from aws_lambda_powertools.utilities.typing import LambdaContext

from monitoring.handler import lambda_handler


def test_lambda_handler(context: LambdaContext) -> None:
    event = {}
    result = lambda_handler(event, context)
    expected = 1
    assert result == expected
