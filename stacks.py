class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def pop(self):
        if self.is_empty():
            print("Stack Underflow!")
        else:
            print("Item popped:", self.stack.pop())

    def display(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            for value in self.stack:
                print(value, end=" ")


stack1 = Stack()
option = 100
while option != 0:
    print("\nMenu\n\t1. Push\n\t2. Pop\n\t3. Display\n\t0. Exit")
    option = int(input("Enter the option: "))
    if option == 1:
        data1 = int(input("Enter the number to push: "))
        stack1.push(data1)
    elif option == 2:
        stack1.pop()
    elif option == 3:
        stack1.display()
