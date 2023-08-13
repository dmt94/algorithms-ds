# Creating a linked list as a class allows us to encapsulate the behavior and data associated with a linked list into a single entity.


#NOTE We define a class called 'Node'
#in a linked list, a node represents an individual element in the list
#each node contains two main components:
  # actual data ('data')
  # reference to the next node ('next')

# this class represents the individual elements or nodes in the linked list
# each node has two attributes: 'data' to store the value of the node and 'next' to store a reference to the next node in the sequence
class Node:
    def __init__(self, data):
        # constructor, is a special method in a class that is used to initialize the attributes and state of an instance when it is created. This is what initializes the attributes of 'data' and 'next' when a new node is created
        self.data = data
        self.next = None

# class represents the linked list itself. It has a single attribute 'head', which is a reference to the first node in the linked list 

class LinkedList:
    def __init__(self):
        self.head = None
        # initially, the linked list is empty, so 'head' is set to 'None'
    
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
