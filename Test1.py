# import math

# print('1) ')
# print(4 * (6 + 5) == 44)
# print('2) ')
# print(4 * 6 + 5 == 29)
# print('3) ')
# print(4 + 6 * 5 == 34)

# print((100.25 * 4 - 145) / 32 == 4 + 2 ** 2)

# print(math.sqrt(25))
# print(2 ** 3 == 8)
# print((int) ((60 - 54) + (9 - 10)) ** 2 * (100 / 25))

# a = 5
# a = a + a
# print(a + a)
# print(type(a))
# a = 5 / 2
# print(a)
# print(type(a))

# myIncome = 100
# myTaxRate = 0.1
# print('my income:' + myIncome + ' my tax rate:' + myTaxRate)
# print('my net income: ' + (myIncome * myTaxRate))

# myString = "Hello World"
# print(myString[0] == "H")
# print(myString[-3] == "r")
# print(myString[2:] == "llo World")
# print(myString[:3] == "Hel")
# print(myString[3:-1] == "lo Worl")
# print(myString[::3] == "HlWl")
# print(myString[::-1] == "dlroW olleH")

# name = "Maui"
# print((name + " is one of my cats").split("o"))
# print(name * 4 == "MauiMauiMauiMaui")
# print(name.upper())

# test = "{1} and {0} are my cats. {0} is older than {1}. {0}, {0}, {0}, you are very {c}!"
# print(test.format("Maui", "Riley", c="cute"))

testnum = 100/777
print(f"The result was {testnum:10.3f}" == "The result was      0.129")

# cat1 = "Maui"
# cat2 = "Riley"
# print(f"{cat1} and {cat2} are very cute")

# ourCats = ["Maui", "Riley"]
# biancaCats = ["Luna", "Peanut", "Aurora"]
# allCats = ourCats + biancaCats
# print(ourCats + biancaCats == ["Maui", "Riley", "Luna", "Peanut", "Aurora"])
# allCats.append("Coree")
# print(allCats)
# print(allCats.pop() == "Coree")
# print(allCats.pop(-2) == "Peanut")

# cats = {'Maui' : 'Tortoiseshell', 'Riley' : 'Cream'}
# print(cats)
# cats['Coree'] = 'Tabby'
# print(cats)
# print(cats.keys())
# print(cats.values())
# print(cats.items())

# cats = ("Maui", "Riley")
# print(cats)
# print(cats.count("Maui"))
# cats[2] = "Coree"

# cats = set()
# cats.add("Maui")
# print(cats == {"Maui"})
# cats.add("Riley")
# print(cats == {"Maui", "Riley"})
# cats.add("Maui")
# print(cats == {"Maui", "Riley"})

def print_big(letter):
    db = {'a' : '  *  \n * * \n*****\n*   *\n*   *', 'b' : '**** \n*   *\n**** \n*   *\n**** ', 'c' : ' *** \n*   *\n*    \n*   *\n *** ', 'd' : '**** \n*   *\n*   *\n*   *\n**** ', 'e' : '*****\n*    \n***  \n*    \n*****'}
    return db[letter.lower()]

print(print_big('e'))