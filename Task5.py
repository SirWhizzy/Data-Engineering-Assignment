'''
This function is designed to track all bad entries(integers) and return them

Args: Supply the list of bad entries
The code run through the list of entry in the supplied data and checks for values that are not string

'''
def take_input(entries):
    for entry in entries:
        if type(entry) != str:
            yield entry



entries = [4,'Bolade','Tolu',5]
output = take_input(entries)
for i in output:
    print(i)

