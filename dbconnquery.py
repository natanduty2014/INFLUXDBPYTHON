from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "Zxbb6GfySqph1ekz7ZSVKhKv9GKsAoomX5gXAg_DmYCEJD6lMcRXuhwcH2YcWpcp1yb3p7SIbSAZ18PHfPoCkg=="
org = "admin"
bucket = "admin"

with InfluxDBClient(url="http://15.228.220.233:8086", token=token, org=org) as client:
 query = 'from(bucket: "admin") |> range(start: -1h)'
 tables = client.query_api().query(query, org=org)
 for table in tables:
    for record in table.records:
        print(record)