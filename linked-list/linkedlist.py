# Creating a SINGLY linked list as a class allows us to encapsulate the behavior and data associated with a linked list into a single entity.


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
        # append method is used to add a new node with the given 'data' to the end of the linked list
        
        new_node = Node(data)
        # an instance of the Node class ( a new node ) is created, passing in data used in the argument to create the new node
        if self.head is None:
            # if the self.head is None, it means that the linked list is empty. If this is the case, then the 'head' is set to the newly created node (new_node) and exits
            self.head = new_node
            return        
        current = self.head
            # if the linked list IS NOT empty, a variable named current is created and set to the node that represents the 'head'
        while current.next:
            # while loop traverses through the linked list using the 'current' variable. It starts from the 'head' and moves to the last node by following the 'next' references until it reaches the last node. 'While current.next' means that while current.next is not equal to None, the loop keeps going because the last node isn't reached yet since only the last node will have the 'next' reference as 'None'.
            current = current.next
        current.next = new_node
        #once the last node has been reached, it updates the 'next' reference of the last node to point to the newly created node, effectively adding it to the end of the linked list

        #NOTE appending = adding to the linked list, so you are finding the last node to attach the new node as the 'next' reference to that last node

    
    def display(self):
        #method is used to print the elements of the linekd list in order. it starts from the 'head' and iterates through the linked list by following the 'next' references. 
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
