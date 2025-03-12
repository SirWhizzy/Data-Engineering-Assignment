list_of_names = ['Wofai','Zainab','Aatullah']
names = []
for name in list_of_names:
    if name.isalpha() != True:
        print(f'Invalid entry contains numbers. The affected entry is {name}')
    else:
        names.append(name)
