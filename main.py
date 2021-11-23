username = input("Enter username: ")

if (len(username) <= 12):
    print("Username set to " + username)
else:
    print("Username too long")

slicing_start = int(input("From where to slice? ")) - 1
slicing_end = int(input("To where? "))
slice = username[slicing_start:slicing_end]

print("Here's your slice: " + slice)

