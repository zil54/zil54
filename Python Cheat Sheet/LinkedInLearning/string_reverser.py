import custom_stack

string = "Gugu gaga"
reversed_string = ""
stringAsCharStack = custom_stack.Stack()
reverseStringAsCharStack = custom_stack.Stack()
for ch in string:
    stringAsCharStack.push(ch)

#dz:
s = stringAsCharStack.size()
while s > 0:
    reverseStringAsCharStack.push(stringAsCharStack.peek())
    stringAsCharStack.pop()
    s = s-1

#reversed_string = reverseStringAsCharStack.get_stack_as_one_string()

#class:
#while not stringAsCharStack.is_empty():
#   reversed_string = reversed_string + (str)get_stack_as_one_stringstringAsCharStack.pop()

print(reversed_string)







