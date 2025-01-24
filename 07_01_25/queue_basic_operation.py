# Class Queue to represent a queue
class Queue:
    # __init__ function
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None] * capacity
        self.capacity = capacity

    # Queue is full when size becomes equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue.
    # It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Queue is full!")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print(f"{item} enqueued to queue")

    # Function to remove an item from the queue.
    # It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return
        print(f"{self.Q[self.front]} dequeued from queue")
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    # Function to get the front item of the queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            print(f"Front item is {self.Q[self.front]}")

    # Function to get the rear item of the queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty!")
        else:
            print(f"Rear item is {self.Q[self.rear]}")

    def PrintQueue(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        i = self.front
        print("Queue contents: ", end="")
        for _ in range(self.size):
            print(self.Q[i], end=" ")
            i = (i + 1) % self.capacity
        print()
        
# Driver code
if __name__ == '__main__':
    queue = Queue(30)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
    queue.PrintQueue()