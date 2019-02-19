# Scrapy Kinesis Pipeline

## Requirements

* Python 3.4+ (Tested in 3.6)
* Scrapy 1.1+ (Tested in 1.4)
* boto3

## Install

Install using pip:

```bash
pip install scrapy-kinesispipeline
```

## Usage

In your `settings.py` file, add the following to `ITEM_PIPELINES`:

```
ITEM_PIPELINES = {
    ...
    'kinesispipeline.KinesisPipeline': 100,
    ...
}
```

Also, set the following variables in `settings.py`:

```
KINESISSTREAM_NAME = '<your_kinesis_stream_name>'
KENISISPARTITION_KEY = '<your_partition_key>'
```

## Development

### Test

```
$ python3 setup.py test
```

### Release

```
$ python3 setup.py bdist_wheel sdist
$ twine upload dist/*
```
