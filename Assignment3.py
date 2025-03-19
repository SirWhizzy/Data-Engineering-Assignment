import requests
url = 'https://randomuser.me/api/?results=500'
response = requests.get(url)
response_url = response.json()
results = response_url["results"]

#get the list of male and female profiles in 2 separate lists
list_of_male_profiles = []
list_of_female_profiles = []
for profiles in results:
  for keys, values in profiles.items():
    if keys == 'gender' and values == 'male':
      list_of_male_profiles.append(profiles)
    elif keys == 'gender' and values == 'female':
      list_of_female_profiles.append(profiles)

#to check the male profiles list
print(list_of_male_profiles)

#to check the female profiles list
print(list_of_female_profiles)



#extract the age segment of the dob dictionary into a list

age_of_dob = []
for profiles in results:
  for keys, values in profiles.items():
    if keys == 'dob':
      age_of_dob.append(values["age"])

#to check the extracted age list
print(age_of_dob)




#concatenate first and last name together into a list
full_name = []

for profiles in results:
  for keys, values in profiles.items():
    if keys == 'name':
      full_name.append(values["first"] + " " + values["last"])

#to check the concatenated list
print(full_name)