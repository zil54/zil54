class Stack:
    def __init__(self):
        # empty list
        self.list_as_stack = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.list_as_stack

    def push(self, appending_item):
        self.list_as_stack.append(appending_item)

    def pop(self):
        self.list_as_stack.pop()

    def peek(self):
        return self.list_as_stack[-1]

    def size(self):
        return len(self.list_as_stack)

    def get_stack_as_one_string(self):
        return_str = ""
        return return_str.join(self.list_as_stack)

    def __str__(self):
        return str(self.list_as_stack)


if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(3)
    print(s)
    s.push(7)
    s.push(5)
    print(s)
    s.pop()
    print(s)
