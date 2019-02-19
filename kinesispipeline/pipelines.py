import boto3
import aws_kinesis_agg.aggregator
import json
from datetime import date, datetime


class KinesisPipeline:
    """
    Scrapy pipeline to store items into S3 bucket with JSONLines format.
    Unlike FeedExporter, the pipeline has the following features:
    * The pipeline stores items by chunk.
    * Support GZip compression.
    """

    def __init__(self, settings, stats):
        self.stats = stats
        self.stream_name = settings['KINESISSTREAM_NAME']
        self.partition_key = settings['KENISISPARTITION_KEY']
        self.kinesis = boto3.client('kinesis')
        self.kinesis_agg = aws_kinesis_agg.aggregator.RecordAggregator()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings, crawler.stats)

    def process_item(self, item, spider):
        """
        Process single item. Add item to items and then upload to S3 if size of items
        >= max_chunk_size.
        """

        # Send records to Kinesis
        pk, ehk, data = self._generate_kinesis_record(item)
        result = self.kinesis_agg.add_user_record(pk, data, ehk)
        if result:
            self._send_record(result)

    def open_spider(self, spider):
        """
        Callback function when spider is open.
        """
        # Store timestamp to replace {time} in S3PIPELINE_URL

        # self.kinesis_agg.on_record_complete(self._send_record)

    def close_spider(self, spider):
        """
        Callback function when spider is closed.
        """
        # Upload remained items to Kinesis.
        self._send_record(self.kinesis_agg.clear_and_get())

    def _send_record(self, agg_record):
        """Send the input aggregated record to Kinesis via the PutRecord API.

        Args:
            agg_record - The aggregated record to send to Kinesis. (AggRecord)"""

        if agg_record is None:
            return

        partition_key, explicit_hash_key, raw_data = agg_record.get_contents()

        # six.print_('Submitting record with EHK=%s NumRecords=%d NumBytes=%d' %
        #            (explicit_hash_key, agg_record.get_num_user_records(), agg_record.get_size_bytes()))
        try:
            self.kinesis.put_record(StreamName=self.stream_name,
                                    Data=raw_data,
                                    PartitionKey=partition_key)
        except Exception as e:
            print(e)
        else:
            print("Success!")

    def _generate_kinesis_record(self, item):
        item_partition_key = item[self.partition_key]
        explicit_hash_key = item[self.partition_key]
        raw_data = json.dumps(item, default=self._json_serial)
        return item_partition_key, explicit_hash_key, raw_data

    @staticmethod
    def _json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))
