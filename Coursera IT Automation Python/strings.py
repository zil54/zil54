name = "James Bond"
print(name[2])
print(name[-1])
print(name[6:10])
print(name[6:])
print(name[6:])
print(name[:5])
print(name.index("J"))
# 0
# print(name.index("q"))
# error
print("q" in name)

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])


def count_letters(text):
    # Initialize a new dictionary.
    dictionary = {}
    currentlettercount = 1
    # Complete the for loop to iterate through each "text" character and
    # use a string method to ensure all letters are lowercase.
    for element in text:
        # Complete the if-statement using a string method to check if the
        # character is a letter.

        if element.lower().isalpha():
            # Complete the if-statement using a logical operator to check if
            # the letter is not already in the dictionary.

            if element.lower() not in dictionary:
                # Use a dictionary operation to add the letter as a key
                # and set the initial count value to zero.
               # currentlettercount = 1
                dictionary[element.lower()] = 1   # existing key, overwrite

            else:
                existing_count = int(dictionary.get(element.lower()))
                dictionary[element.lower()] = existing_count+1

           #     dictionary.update({element.lower(), currentlettercount})


    return dictionary


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}