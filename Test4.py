# from random import randint

# print('x' in 'puchingching')
# db = dict(enumerate('puchingching'))
# # db.update(enumerate('puchingching'))
# # for item in enumerate('puchingching'):
# #     print(f'{item[0]} is {item[1]}')
# #     db[item] = item[1]

# for item in db:
#     print(f'{item} is {db[item]}')

# print(f'is 1 in db? {1 in db}')
# print(f'is 13 in db? {13 in db}')
# print(f'is g in db? {"g" in db.values()}')
# print(f'is x in db? {"x" in db.values()}')

# print(f'min id is: {min(db)}')
# print(f'max id is: {max(db)}')

# inputKey = int(input('Enter a number: '))

# if inputKey in db.keys():
#     print(f'{inputKey} in db is {db[inputKey]}')
# else:
#     print(f'{inputKey} is not in db!')

from random import randint

print('x' in 'puchingching')
db = dict(enumerate('puchingching'))
# db.update(enumerate('puchingching'))
for item in enumerate('puchingching'):
    print(f'{item[0]} is {item[1]}')
    db[item] = item[1]

for item in db:
    print(f'{item} is {db[item]}')

print(f'is 1 in db? {1 in db}')
print(f'is 13 in db? {13 in db}')
print(f'is g in db? {"g" in db.values()}')
print(f'is x in db? {"x" in db.values()}')

print(f'min id is: {min(db)}')
print(f'max id is: {max(db)}')

randKeys = [i * 2 - 1 for i in db.keys() if i%2 == 0]
for randKey in randKeys:
    if randKey in db.keys():
        print(f'{randKey} in db is {db[randKey]}')
    else:
        print(f'{randKey} is not in db!')

# evenWords = [word if len(word) % 2 != 0 else 'even!' for word in 'Print every word in this sentence that has an even number of letters'.split(' ')]
# print(evenWords)

# firstChars = [word[0] for word in 'Create a list of the first letters of every word in this string'.split(' ')]
# print(firstChars)

# for num in range(1,100):
#     if (num % 5) + (num % 3) == 0:
#         print('FizzBuzz')
#     elif num % 5 == 0:
#         print('Buzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     else:
#         print(num)