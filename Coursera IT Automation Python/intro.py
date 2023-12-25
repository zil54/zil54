import math

print(type("a"))
print(type('q'))
print(type(True))
print(type(math.pi))
print(type(math.ceil(2.55)))
print("blue" == "Blue")

#multi-return
def convert_seconds(secs):
    hrs = secs // 3600
    mins = (secs - hrs * 3600) // 60
    remaining_secs = secs - hrs * 3600 - mins * 60
    return hrs, mins, remaining_secs

print(str(convert_seconds(56)));
print(str(convert_seconds(10000)));
print(str(convert_seconds(180)));
#tuple
print(type((convert_seconds(180))));
print((2**2) == 4)
print("A dog" + "A mouse")
print(9999+8888 + 100*100)

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    return full_blocks, partial_block_remainder


print("full block, partial block: " + str(calculate_storage(1)))    # Should be 4096
print("full block, partial block: " + str(calculate_storage(4096))) # Should be 4096
print("full block, partial block: " + str(calculate_storage(4097))) # Should be 8192
print("full block, partial block: " + str(calculate_storage(6000))) # Should be 8192
print("big" > "small")
print(11%5)
print((10 >= 5*2) and (10 <= 5*2))





def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))
def calculate_storage2(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder =  filesize % block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        if filesize < block_size:
            return block_size
        else:
            return (full_blocks + 1) * block_size
    return full_blocks * block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192




"""In Python, we can use comparison operators to compare values. 
When a comparison is made, Python returns a boolean result, or simply a True or False.
To check if two values are the same, we can use the equality operator: ==
To check if two values are not the same, we can use the not equals operator: !=
We can also check if values are greater than or lesser than each other using > and <. 
If you try to compare data types that aren’t compatible, like checking if a string is greater than an integer, Python will throw a TypeError.
We can make very complex comparisons by joining statements together using logical operators with our comparison operators. 
These logical operators are and, or, and not. When using the and operator, both sides of the statement being evaluated must be true for the whole statement to be true. 
When using the or operator, if either side of the comparison is true, then the whole statement is true. 
Lastly, the not operator simply inverts the value of the statement immediately following it. 
So if a statement evaluates to True, and we put the not operator in front of it, it would become False."""