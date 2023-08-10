# Creating a linked list as a class allows us to encapsulate the behavior and data associated with a linked list into a single entity.


#NOTE We define a class called 'Node'
#in a linked list, a node represents an individual element in the list
#each node contains two main components:
  # actual data ('data')
  # reference to the next node ('next')
class Node:
    def __init__(self, data):
        # constructor, is a special method in a class that is used to initialize the attributes and state of an instance when it is created.
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list and add elements
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Display the linked list
my_list.display()
