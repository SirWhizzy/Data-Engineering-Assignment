import requests

url = 'http://api.football-data.org/v4/competitions/'
response = requests.get(url)
response_url = response.json()
competitions = response_url["competitions"]

competition_name = []
for competition_list in competitions:
  for keys, values in competition_list.items():
    if keys == "name":
      competition_name.append(values)

print(competition_name)