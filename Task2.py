import re

list_of_attributes = ['first name', 'last_name', 'date of birth']
my_s1 = []
for name in list_of_attributes:
    s1 = name
    s2 = re.sub(r'([a-z])([ ])', r'\1_\2', s1).lower()
    my_s1.append(s2)

print(my_s1)

