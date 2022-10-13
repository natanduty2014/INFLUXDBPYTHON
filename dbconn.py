"""
How to check that connection credentials are suitable for queries and writes from/into specified bucket.
"""

from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

"""
Define credentials
"""
url = "http://15.228.220.233:8086"
token = "Zxbb6GfySqph1ekz7ZSVKhKv9GKsAoomX5gXAg_DmYCEJD6lMcRXuhwcH2YcWpcp1yb3p7SIbSAZ18PHfPoCkg=="
org = "admin"
bucket = "admin"

from datetime import datetime, time

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "Zxbb6GfySqph1ekz7ZSVKhKv9GKsAoomX5gXAg_DmYCEJD6lMcRXuhwcH2YcWpcp1yb3p7SIbSAZ18PHfPoCkg=="
org = "admin"
bucket = "admin"

with InfluxDBClient(url="http://15.228.220.233:8086", token=token, org=org) as client:
 write_api = client.write_api(write_options=SYNCHRONOUS)
 data = "sensor,device=ESP8266,host=AWS temperatura=40"
 write_api.write(bucket, org, data)

