list_of_names = ['Mayowa','chizoba','Chigozie']
names = []
for name in list_of_names:
    if name[0].isupper() and name[-1] == 'a':
        names.append(name)
    elif name[0].isupper() and name[-1] != 'a':
        name = name[0:-1] + 'a'
        names.append(name)

print(names)

