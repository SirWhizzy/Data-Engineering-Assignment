import requests
url = 'https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo'
response = requests.get(url)
print(response)
response_url = response.json()
jobs = response["jobs"]

#list of job titles with manager as title
list_of_manager = []
for job in jobs:
  for keys, values in job.items():
    if keys == 'jobTitle' and "Manager" in values:
      list_of_manager.append(values)

print(list_of_manager)

#list of job titles with Senior as title
list_of_senior = []
for job in jobs:
  for keys, values in job.items():
    if keys == 'jobTitle' and "Senior" in values:
      list_of_senior.append(job)

print(list_of_senior)