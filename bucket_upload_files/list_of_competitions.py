import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'http://api.football-data.org/v4/competitions/'
response = requests.get(url)


if response.status_code == 200:
    response_url = response.json()

else:
    print("Error: Unable to fetch data from the API")


competitions = response_url["competitions"]


def list_of_competition():
    competition_name = []
    for competition_list in competitions:
        for keys, values in competition_list.items():
            if keys == "name":
                competition_name.append(values)
    return competition_name


list_a = list_of_competition()

data_df = pd.DataFrame(list_a)

session = boto3.Session(
    aws_access_key_id=os.getenv('aws_access_key'),
    aws_secret_access_key=os.getenv('aws_secret_key'),
    region_name=os.getenv('region'))

wr.s3.to_csv(
    df=data_df,
    path="s3://toludebuckets/competition/list_of_competitions",
    boto3_session=session,
    mode="append",
    dataset=True
   )
