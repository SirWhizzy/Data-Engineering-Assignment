def firstname():
    name = 'Tolu'
    return name


def lastname():
    name = 'Oladipo'
    return name

def fullname():
    first = firstname()
    last = lastname()
    fullname = print(f'My full name is {first} {last}')
    return fullname

fullname()
