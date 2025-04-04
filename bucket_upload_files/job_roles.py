import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo'
response = requests.get(url)

if response.status_code == 200:
    response_url = response.json()

else:
    print("Error: Unable to fetch data from the API")

jobs = response["jobs"]

list_of_managers = []
for job in jobs:
    for keys, values in job.items():
        if keys == 'jobTitle' and "Manager" in values:
            list_of_managers.append(values)

managers_df = pd.DataFrame(list_of_managers)

list_of_seniors = []
for job in jobs:
    for keys, values in job.items():
        if keys == 'jobTitle' and "Senior" in values:
            list_of_seniors.append(job)

seniors_df = pd.DataFrame(list_of_seniors)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
    aws_secret_access_key=os.getenv('aws_secret_key'),
    region_name=os.getenv('region'))

wr.s3.to_csv(
    df=managers_df,
    path="s3://toludebuckets/job_roles/list_of_managers",
    boto3_session=session,
    mode="append",
    dataset=True
   )


wr.s3.to_csv(
    df=seniors_df,
    path="s3://toludebuckets/job_roles/list_of_seniors",
    boto3_session=session,
    mode="append",
    dataset=True
   )
