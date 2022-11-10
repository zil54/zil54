def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0 and n != 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
print ("-------")

print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

print ("-------")
def sum_divisors(n):
  sum = 0

  if n == 0:
    sum = n
  elif n > 1:
    divisor = 1
    while divisor < n - 1:
      divisor = divisor + 1
      if n % divisor == 0:
        sum = sum + divisor

  if n > 2:
    sum += 1

  return sum

#range([start], stop[, step]), stop never includes the last element
def factorial(n):
  result = 1
  starter_variable = 1
  for i in range(n):
    result = result * starter_variable
    starter_variable += 1
  return result
print ("-------")
print(factorial(4))


def factorial(n):
  result = 1
  for x in range(1, n):
    result = result * x
  return result


for n in range(0, 10):
  print(n, factorial(n + 1))

print ("-------")
def multiples_seven(range_start, range_end):
    result = []
    while range_start <= range_end:
      if range_start % 7 == 0:
        result.append(range_start)
        range_start = range_start  + 7
      else:
        range_start = range_start + 1
    return result


print('\n'.join(map(str, multiples_seven(0, 100))))
print ("-------")

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)



votes(['yes', 'no', 'maybe'])
print ("-------")
for x in range(10):
    for y in range(x):
        print(y)
print ("-------")
for x in range(1, 10, 3):
    print(x)

print ("-------")
def even_numbers(maximum):
	return_string = ""
	for x in range(2, maximum+1,2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


def digits(n):
  count = 0
  while (n > 9):
    n = n / 10
    count += 1
  count += 1
  return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(9999))  # Should print 5
print(digits(0))  # Should print 1


#The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise.
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x -= 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x +=1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

#This function prints out a multiplication table (where each number is the result of multiplying the first number of its row by the number at the top of its column).
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:
#123
#246
#369

def multiplication_table(start, stop):
    temp_list_iterator = []
    while start <= stop:
        temp_list_iterator.append(start)
        start += 1
    for x in temp_list_iterator:
        for y in temp_list_iterator:
            print(str(x*y), end=" ")
        print()


multiplication_table(1, 3)