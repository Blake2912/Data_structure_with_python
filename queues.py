class Queues:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.insert(0, data)

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print("Queue underflow")
        else:
            print("Item popped", self.queue.pop())

    def display(self):
        if self.is_empty():
            print("The queue is empty!")
        else:
            for value in self.queue:
                print(value,end=" ")


queue1 = Queues()
option = 100
while option != 0:
    print("\nMenu\n\t1. Push\n\t2. Pop\n\t3. Display\n\t0. Exit")
    option = int(input("Enter the option: "))
    if option == 1:
        data1 = int(input("Enter the number to push: "))
        queue1.push(data1)
    elif option == 2:
        queue1.pop()
    elif option == 3:
        queue1.display()

