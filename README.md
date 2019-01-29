# Scrapy Kinesis Pipeline

## Requirements

* Python 3.4+ (Tested in 3.6)
* Scrapy 1.1+ (Tested in 1.4)
* boto3

## Install

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
