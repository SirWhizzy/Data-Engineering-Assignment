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

import os
import awswrangler as wr
import boto3 
from dotenv import load_dotenv, dotenv_values


#AWS credentials
aws_access_key_id = os.getenv('AWS_ACCESS_KEY')
aws_secret_access_key = os.getenv('AWS_SECRET_KEY')
aws_region = os.getenv('region')

# Upload the DataFrame to S3 as a Parquet file using awswrangler
wr.s3.to_csv(
    df= data_df,
    dataset=True,  
    mode='append'
)


file="test1.csv"


load_dotenv()

session = boto3.Session(
aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
aws_region = os.getenv('region')
)

wr.s3.to_parquet(
    df=data_df,
    path="s3://tolufile/competition",
    boto3_session=session,
    mode="append",
    dataset=True 
   )
