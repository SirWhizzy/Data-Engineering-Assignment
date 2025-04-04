import os

import awswrangler as wr
import boto3
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

url = 'https://randomuser.me/api/?results=500'
response = requests.get(url)

if response.status_code == 200:
    response_url = response.json()

else:
    print("Error: Unable to fetch data from the API")

results = response_url["results"]

list_of_male_profiles = []
list_of_female_profiles = []
for profiles in results:
    for keys, values in profiles.items():
        if keys == 'gender' and values == 'male':
            list_of_male_profiles.append(profiles)
        elif keys == 'gender' and values == 'female':
            list_of_female_profiles.append(profiles)

male_profiles_df = pd.DataFrame(list_of_male_profiles)

female_profiles_df = pd.DataFrame(list_of_female_profiles)

age_of_dob = []
for profiles in results:
    for keys, values in profiles.items():
        if keys == 'dob':
            age_of_dob.append(values["age"])

dob_df = pd.DataFrame(age_of_dob)

full_name = []
for profiles in results:
    for keys, values in profiles.items():
        if keys == 'name':
            full_name.append(values["first"] + " " + values["last"])

full_name_df = pd.DataFrame(full_name)

session = boto3.Session(aws_access_key_id=os.getenv('aws_access_key'),
    aws_secret_access_key=os.getenv('aws_secret_key'),
    region_name=os.getenv('region'))

wr.s3.to_csv(
    df=male_profiles_df,
    path="s3://toludebuckets/random_users_api/male_profiles",
    boto3_session=session,
    mode="append",
    dataset=True
   )

wr.s3.to_csv(
    df=female_profiles_df,
    path="s3://toludebuckets/random_users_api/female_profiles",
    boto3_session=session,
    mode="append",
    dataset=True
   )

wr.s3.to_csv(
    df=dob_df,
    path="s3://toludebuckets/random_users_api/dob",
    boto3_session=session,
    mode="append",
    dataset=True
   )

wr.s3.to_csv(
    df=full_name_df,
    path="s3://toludebuckets/random_users_api/full_name",
    boto3_session=session,
    mode="append",
    dataset=True
   )
