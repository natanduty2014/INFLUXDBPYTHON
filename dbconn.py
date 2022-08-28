"""
How to check that connection credentials are suitable for queries and writes from/into specified bucket.
"""

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

"""
Define credentials
"""
url = "http://localhost:8086"
token = "qjtfFHcYStz3kBn0g1JXmXBD_1esNFr-_S3JU19dxkpZu7BfQLW1CAAwqDiy-GDgBNihkL604foMvLcaOdse9w=="
org = "aws"
bucket = "aws"

from datetime import datetime, time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "qjtfFHcYStz3kBn0g1JXmXBD_1esNFr-_S3JU19dxkpZu7BfQLW1CAAwqDiy-GDgBNihkL604foMvLcaOdse9w=="
org = "aws"
bucket = "-aws"

with InfluxDBClient(url="http://localhost:8086", token=token, org=org) as client:
 write_api = client.write_api(write_options=SYNCHRONOUS)
 data = "sensor,device=ESP8266,host=AWS temperatura=31"
 write_api.write(bucket, org, data)


