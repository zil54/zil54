# Python Cheat Sheet
# Dictionary

# Creating an empty Dictionary
DictEuropeanCities = {}

# Populate DictEuropeanMainCitiesPerCountry

DictEuropeanCities['Croatia'] = 'Zagreb<-->Dubrovnik'
DictEuropeanCities['Italy'] = 'Rome<-->Naples<-->Turin<-->Milan'
DictEuropeanCities['Germany'] = 'Berlin<-->Frankfurt-->Cologne<-->Dresden'

# add value key-value pair to dic
DictEuropeanCities.update(France='Paris<-->Nice<-->Lyon<-->Avignon')
DictEuropeanCities.update(Spain='Madrid<-->Barcelona<-->Malaga<-->Valencia',
                          Holland='Amsterdam<-->Rotterdam<-->Hague<-->Utrecht')

# add parametrized key-value pair to dic
y = 'Stockholm<-->Malmo<-->Gothenburg'
DictEuropeanCities.update(Sweden=y)

# Iterate Dictionary via enumerate
for i, (k, v) in enumerate(DictEuropeanCities.items()):
    splitter_arr = v.split('<-->')
    capital = splitter_arr[0]
    print(capital)
    print(i)

# Iterate Dictionary keys
for country in DictEuropeanCities:
    print(country)

# Iterate Dictionary value
for cities in DictEuropeanCities.values():
    print(cities)

# Iterate Key value pairs
for country, cities in DictEuropeanCities.items():
    print(country, ":", cities)

# get dictionary value by key
print(DictEuropeanCities.get('Croatia'))

# get dictionary key by value
print("One line Code Key value: ",
      list(DictEuropeanCities.keys())[list(DictEuropeanCities.values()).index('Zagreb<-->Dubrovnik')])

print("-------------")
# Create on empty list
ListContinentsEmpty = []

# Populated
ListContinents = ['Africa', 'SAmerica', 'NAmerica', 'Europe', 'Asia', 'Australia']
# append
ListContinents.append('Antarctica')
print("individual continent")
print(ListContinents[3])

print("version 1 --> range")
for x in range(len(ListContinents)):
    print(ListContinents[x])

print("version 2 --> simple for loop")
for continent in ListContinents:
    print(continent)

print("version 3 --> enumerate")
for i, continent in enumerate(ListContinents):
    print(ListContinents[i])
    # or:
    print(continent)

print("\n")
"""
Python - List Comprehension
List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
Example
Get your own Python Server
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

With list comprehension you can do all that with only one line of code:
Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

The Syntax
newlist = [expression for item in iterable if condition == True]

The return value is a new list, leaving the old list unchanged.
Condition

The condition is like a filter that only accepts the items that valuate to True.
Example

Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]

The condition if x != "apple"  will return True for all elements other than "apple",
making the new list contain all fruits except "apple".

The condition is optional and can be omitted:
Example

With no if statement:
newlist = [x for x in fruits]
Iterable

The iterable can be any iterable object, like a list, tuple, set etc.
Example

You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

Same example, but with a condition:
Example

Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
Expression

The expression is the current item in the iteration, but it is also the outcome, which you can
manipulate before it ends up like a list item in the new list:
Example

Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]

You can set the outcome to whatever you like:
Example

Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

The expression can also contain conditions, not like a filter, but as a way to manipulate
the outcome:
Example

Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
"""

def squares(start, end):
    squares_list = [x**2 for x in range(start, end+1)]
    return squares_list # Create the required list comprehension.


print(squares(2, 3)) # Should print [4, 9]
print(squares(1, 5)) # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# functions using args and kwargs as lists and dictionaries, respectively:

def invadeEarth(attackingFleet, *args):
    if len(args) > 0:
        attackingFleetPerContinent = attackingFleet / len(args)
        print("Attacking fleet per continent: " + str(attackingFleetPerContinent) + "\n")
        for i, arg in enumerate(args):
            j = i + 1
            print("Continent # " + str(j) + ": " + arg)
    else:
        print("No continent specific split - just all-out assault against everyone with " + str(attackingFleet))


invadeEarth(77, *ListContinents)
invadeEarth(77)


def travelEurope(numberOfDays, **kwargs):
    if len(kwargs) > 0:
        citiesPlanned = 0
        print("Number of Days per City: " + "\n")
        for i, (j, k) in enumerate(kwargs.items()):
            splitter_arr = k.split('<-->')
            citiesPlanned = citiesPlanned + len(splitter_arr)
        print(str(numberOfDays / citiesPlanned))


travelEurope(18, **DictEuropeanCities)

# Tuples

# Creating an empty tuple
emptyTuple = ()

# Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
# 1-member tuple
oneMemberTuple = ("zzz",)

primeNumbersAround100 = (97, 101, 103, 107, 109)

# iterate
print("Prime Numbers around 100: " + "\n")
for primn in primeNumbersAround100:
    print(primn)

# Sets - a set is a collection which is unordered and unindexed. In Python sets are written with curly brackets. Elements unique
set1 = {"x", "y", "z"}

# empty set:
set2 = set()

# can be for-loop'ed
for elem in set1:
    print(elem)

set2.add("a")
set2.update(["b", "c", "d"])
set2.remove("c")
print(set2)

# non-unique elements nothing will get added
set1.add("x")
for elem in set1:
    print(elem)
# ---------------------------------------------------
# Exercises:
speed_limits = {"street": 35, "highway": 65, "school": 15}
print(speed_limits["highway"])
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)


def alphabetize_lists(list1, list2):
    list3 = list1 + list2

    return sorted(list3)


a_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
b_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]

print(alphabetize_lists(a_list, b_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']
