import csv
import gzip
import io
import tarfile
import tempfile

from boto3_type_annotations.s3 import Bucket


def read_s3_targz_lines(bucket: Bucket, key: str, delimiter: str, skip_header: bool) -> list[str]:
    with tempfile.TemporaryFile(mode='w+b') as temp:
        bucket.download_fileobj(key, temp)
        temp.seek(0)
        with tarfile.open(fileobj=temp, mode='r:gz') as tar:
            for member in tar.getmembers():
                r = tar.extractfile(member)
                reader = csv.reader(io.TextIOWrapper(r), delimiter=delimiter)
                if skip_header:
                    next(reader)
                for fields in reader:
                    yield fields


def read_s3_gz_lines(bucket: Bucket, key: str, delimiter: str, skip_header: bool) -> list[str]:
    with tempfile.TemporaryFile(mode='w+b') as temp:
        bucket.download_fileobj(key, temp)
        temp.seek(0)
        with gzip.open(temp, mode='rt') as rt:
            reader = csv.reader(rt, delimiter=delimiter)
            if skip_header:
                next(reader)
            for fields in reader:
                yield fields
