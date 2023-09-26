from linkedin_api import Linkedin
import json
from cli import get_data_processing_parser
from linkedin_custom_search import LinkedinCustomSearch
from processor import Processor
from scraper import Scraper, ScraperConfig2
from pyspark.sql import SparkSession
from dotenv import dotenv_values
import boto3
import os
import pandas as pd


def run_linkedin_scraper(self):
    print(os.getcwd())
    config = dotenv_values("/home/peppe/Master-DE-Scaper/.env")
    parser = get_data_processing_parser()
    args = parser.parse_args()
    EMAIL = args.linkedin_email
    PASSWORD = args.linkedin_password
    print(PASSWORD, "ciao")
    PATH = args.s3_path
    api = Linkedin(EMAIL, PASSWORD)

    ACCESS_KEY1 = config['ACCESS_KEY1']
    SECRET_ACCESS_KEY1 = config['SECRET_KEY1']

    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk-bundle:1.12.349') \
        .config('spark.hadoop.fs.s3a.access.key', ACCESS_KEY1) \
        .config('spark.hadoop.fs.s3a.secret.key', SECRET_ACCESS_KEY1) \
        .getOrCreate()

    processor = Processor()
    searcher = LinkedinCustomSearch(api)
    scraper = Scraper(searcher, processor, ScraperConfig2())

    s3 = boto3.client('s3')
    res = scraper.fetch_job_descriptions_by_scraping_plan()
    final = json.dumps(res)

    df = pd.DataFrame.from_dict(res)
    spark_df = spark.createDataFrame(df)
    spark_df.write.mode('overwrite').parquet(PATH)
