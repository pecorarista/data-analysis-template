import os
from typing import Generator

import boto3
import pytest
from boto3_type_annotations.s3 import Bucket
from moto import mock_s3

from analysis.config import Config
from analysis.storage import read_s3_targz_lines


@pytest.fixture(scope='function')
def bucket(config: Config) -> Generator[Bucket, None, None]:
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

    bucket_name = config.cloud_storage.bucket_name
    with mock_s3():
        s3 = boto3.resource('s3')
        s3.create_bucket(Bucket=bucket_name)
        bucket = s3.Bucket(bucket_name)
        yield bucket


def test_read_s3_targz_lines(bucket: Bucket) -> None:
    key = 'example.tar.gz'
    bucket.upload_file('resources/example.tar.gz', key)
    results = read_s3_targz_lines(bucket, key, delimiter=',', skip_header=True)
    expected = set([(1, 'cat'), (2, 'dog'), (3, 'rabbit'), (4, 'bird')])
    assert set([(int(fields[0]), fields[1]) for fields in results]) == expected
