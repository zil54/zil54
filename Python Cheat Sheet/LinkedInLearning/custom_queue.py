import heapq

class Queue:
    def __init__(self):
        self.list_as_queue = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.list_as_queue

    def put(self, appending_item, priority):
        heapq.heappush(self.list_as_queue, (priority, appending_item))

    def get(self):
        return heapq.heappop(self.list_as_queue)[1]

    def __str__(self):
        return str(self.list_as_queue)


if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.put("eat", 2)
    q.put("code", 1)
    q.put("sleep", 3)

    print(q)
    print(q.get())
    print(q.get())
    print(q.get())
    print(q)


