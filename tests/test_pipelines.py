from unittest import TestCase

from scrapy.settings import BaseSettings

from kinesispipeline import KinesisPipeline

class TestPipelines(TestCase):
    def setUp(self):
        self.settings = BaseSettings({
            'S3PIPELINE_URL': 's3://my-bucket/{name}/{time}/items.{chunk:07d}.jl.gz',
            'KINESISSTREAM_NAME': 'kinesis-stream',
            'KENISISPARTITION_KEY': 'kinesis-partition-key'
        })

    def test_settings(self):
        pipeline = KinesisPipeline(self.settings, None)
        self.assertEqual(pipeline.stream_name, 'kinesis-stream')
        self.assertEqual(pipeline.partition_key, 'kinesis-parition-key')
