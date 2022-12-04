# myfile = open("myfile.txt")
# print(myfile.read())
# contents = myfile.read()
# print(contents == "")
# myfile.seek(0)
# contents = myfile.read()
# myfile.seek(0)
# print(myfile.readlines())
# myfile.close()

with open('myfile.txt', mode='r') as my_new_file:
    contents = my_new_file.readlines()

with open('myfile.txt', mode='w') as my_new_file:
    contents = my_new_file.readlines()

with open('myfile.txt', mode='a') as my_new_file:
    contents = my_new_file.readlines()

with open('myfile.txt', mode='r+') as my_new_file:
    contents = my_new_file.readlines()

with open('myfile.txt', mode='w+') as my_new_file:
    contents = my_new_file.readlines()

print(contents)


# filename = 'mynewfile.txt'
# with open(filename, mode='r') as f:
#     print(f.read())

# with open(filename, mode='a') as f:
#     f.write('\nFOUR ON FOURTH')

# print(open(filename).readlines())

# with open('anothernewfile.txt', mode='w') as f:
#     f.write('THIS IS A BRAND NEW FILE')

# print(open('anothernewfile.txt').readlines())

print(1 < 2 < 3)
print(not 1 > 2 and 2 < 3)
print(1 > 2 or 2 < 3)
print(1 != 2)