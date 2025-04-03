import requests
url = 'http://api.football-data.org/v4/competitions/'
response = requests.get(url)


response_url = response.json()
#print(response_url)

response.status_code


competitions = response_url["competitions"]


def list_of_competition():
  competition_name = []
  for competition_list in competitions:
    for keys, values in competition_list.items():
      if keys == "name":
        competition_name.append(values)
  return competition_name


list_a = list_of_competition()
#print(list_a)


import pandas as pd
data_df = pd.DataFrame(list_a)


data_df.to_csv('test1.csv', index = False)


from dotenv import load_dotenv
import os
import awswrangler as wr
import boto3 



file="test1.csv"




session = boto3.Session(
aws_access_key_id=os.getenv('aws_access_key'),
aws_secret_access_key=os.getenv('aws_secret_key'),
region_name = os.getenv('region')
)

wr.s3.to_parquet(
    df=data_df,
    path="s3://tolufile/competition/",
    boto3_session=session,
    mode="append",
    dataset=True 
   )
