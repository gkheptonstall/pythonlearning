
# is_hungry = True
# has_food = True
# if is_hungry:
#     print('This is true')
# else:
#     print('No food')

# loc = 'Bank'

# if loc == 'Auto Shop':
#     print('Cars are cool!')
# elif loc == 'Bank':
#     print('Money is cool!')
# else:
#     print('I do not know much.')

# cats = {"Maui" : "Tortoiseshell", "Riley" : "Cream", "Coree" : "Tabby"}
# for cat in cats.keys():
#     print(cat)
#     if cats[cat] == "Cream":
#         print(f"{cat} is a {cats[cat]} cat!");

# cats = [('Maui', 'Tortoiseshell', 'Female'), ('Riley', 'Cream', 'Male'), ('Coree', 'Tabby', 'Male')]
# for a,b,c in cats:
#     if c == 'Female':
#         cute = 'She is very pretty!'
#     elif c == 'Male':
#         cute = 'He is very handsome!'
#     else:
#         cute = 'They are very cute!'
#     print(f'{a} is a {b} cat. {cute}')

# cats = {1 : ('Maui', 'Tortoiseshell', 'Female'), 2 : ('Riley', 'Cream', 'Male'), 3 : ('Coree', 'Tabby', 'Male')}
# for catId, details in cats.items():
#     if details[2] == 'Female':
#         cute = 'She is very pretty!'
#     elif details[2] == 'Male':
#         cute = 'He is very handsome!'
#     else:
#         cute = 'They are very cute!'

#     if catId == 2:
#         continue
#     print(f'{details[0]} has id {catId} and is a {details[1]} cat. {cute}')

# x = 0
# while x < 5:
#     print(f'The current value of x is {x}')
#     x += 1
# else:
#     print(f'{x} IS NOT LESS THAN 5')

# for num in range(10):
#     print(num)

# for num in range(2, 10):
#     print(num)

# for num in range(2, 10, 2):
#     print(num)

# cast to list
# list(range(0,11,2))

# i = 0
# word = 'puchingching'
# for letter in word:
#     print(f'At index {i} the letter is {letter}')
#     i += 1

# enumerate returns tuple(ordered, immutable collection close to list)
# i = 0
# word = 'puchingching'
# for item in enumerate(word):
#     print(item)

# i = 0
# word = 'puchingching'
# for index,letter in enumerate(word):
#     print(f'{letter} char at {index}\n')

# zip returns iterator of tuples
list1 = list(range(10))
list2 = 'puchingchi'
list3 = enumerate(list2)
for item in zip(list1, list2, list3):
    print(item)

print(str.join(list(dict(list3).values())))

# list1 = list(range(10))
# list2 = 'puchingchingychingching'
# list3 = enumerate(list2)
# for id, letter, idLetter in zip(list1, list2, list3):
#     print(idLetter[1])


# print('x' in 'puchingching')
# db = dict(enumerate('puchingching'))
# # db.update(enumerate('puchingching'))
# # for item in enumerate('puchingching'):
# #     print(f'{item[0]} is {item[1]}')
# #     db[item] = item[1]

# for item in db:
#     print(f'{item} is {db[item]}')

# print(f'is 1 in db? ' + str(1 in db))
# print(f'is 13 in db? ' + str(13 in db))
# print(f'is g in db? ' + str('g' in db.values()))
# print(f'is x in db? ' + str('x' in db.values()))

# print(f'min id is: ' + str(min(db)))
# print(f'max id is: ' + str(max(db)))


# from random import shuffle

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

# shuffledKeys = list(db.keys())
# shuffle(shuffledKeys)
# for key in shuffledKeys:
#     print(f'{key} in db is {db[key]}')


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

# randKey = randint(min(db), max(db))

# print(f'{randKey} in db is {db[randKey]}')


from random import randint

print('x' in 'puchingching')
db = dict(enumerate('puchingching'))
# db.update(enumerate('puchingching'))
# for item in enumerate('puchingching'):
#     print(f'{item[0]} is {item[1]}')
#     db[item] = item[1]

for item in db:
    print(f'{item} is {db[item]}')

print(f'is 1 in db? {1 in db}')
print(f'is 13 in db? {13 in db}')
print(f'is g in db? {"g" in db.values()}')
print(f'is x in db? {"x" in db.values()}')

print(f'min id is: {min(db)}')
print(f'max id is: {max(db)}')

inputKey = int(input('Enter a number: '))

if inputKey in db.keys():
    print(f'{inputKey} in db is {db[inputKey]}')

def filter_vowels(self):
    vowels = 'aeiou'
    noVowels = []
    for letter in self:
        if letter not in vowels:
            noVowels.append(letter)
    
    return str(noVowels)

filter_vowels('hackerrank')



def floor(a):
    return str(a)[0]


print(floor(1.1))