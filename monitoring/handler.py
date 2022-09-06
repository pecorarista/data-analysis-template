from __future__ import annotations

from typing import Any

from aws_lambda_powertools.utilities.typing import LambdaContext


def lambda_handler(event: dict[str, Any], context: LambdaContext) -> None:
    return 1
