from setuptools import setup

setup(name='scrapy-kinesispipeline',
      version='0.2.6',
      description='Scrapy pipeline to store aggregated items into AWS Kinesis',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Framework :: Scrapy',
      ],
      keywords='scrapy pipeline aws kinesis serverless',
      url='https://github.com/fleiheit/scrapy-kinesispipeline',
      author='Atabak Hafeez',
      author_email='atabakhafeez@hotmail.com',
      license='MIT',
      packages=['kinesispipeline'],
      install_requires=[
          'Scrapy>=1.1',
          'boto3',
          'aws_kinesis_agg'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
