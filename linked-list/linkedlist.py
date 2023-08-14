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
        # every node created by default has an attribute called next that is initialized to 'None'
        self.next = None

# class represents the linked list itself. It has a single attribute 'head', which is a reference to the first node in the linked list 

class LinkedList:
    def __init__(self):
        self.head = None
        # initially, the linked list is empty, so 'head' is set to 'None'
        # when the linked list is first initialized, the self.head is set to 'None'
    
    def append(self, data):
        # append method is used to add a new node with the given 'data' to the end of the linked list
        
        new_node = Node(data)
        # an instance of the Node class ( a new node ) is created, passing in data used in the argument when calling the append method, to create the new node
        # NOTE this node as a 'next' property initialized to 'None' by default

        if self.head is None:
            # if the self.head is None, it means that the linked list is empty. If this is the case, then the 'head' is set to the newly created node (new_node) and exits
            self.head = new_node
            return        
        current = self.head
            # if the linked list IS NOT empty, a variable named current is created and set to the node that represents the 'head'
            # think about this as a variable that represents a "pointer" that will traverse the linked list
        while current.next:
            # while loop traverses through the linked list using the 'current' variable. It starts from the 'head' and moves to the last node by following the 'next' references for each node until it reaches the last node. 'While current.next' means that while current.next is not equal to None, the loop keeps going because the last node isn't reached yet since only the last node will have the 'next' reference as 'None'.

            #starting from the self.head, we are checking if there is an existing 'next' for the current node (for each node) 
            current = current.next
            # to ensure we are moving forward in this loop, we are changing the value of 'current' to the current node's "next" attribute
            #loop ends once current becomes 'None'
        current.next = new_node
        #once the last node has been reached, it updates the 'next' reference of the last node to point to the newly created node, effectively adding it to the end of the linked list

        #NOTE appending = adding to the linked list, so you are finding the last node to attach the new node as the 'next' reference to that last node

    
    def display(self):
        #method is used to print the elements of the linekd list in order. it starts from the 'head' and iterates through the linked list by following the 'next' references. 
        current = self.head
        # the variable 'current' is initialized with the value of 'self.head'. This sets 'current' to point to the first node of the linked list
        while current:
            # starts a while loop that continues as long as the current node exists (current node is not None). The loop iterates through the linked list nodes.
            print(current.data, end=" -> ")
            current = current.next
            # This updates the current variable to point to the next node in the linked list. It moves current from the current node to the next node by following the next reference. This is the key step that allows the loop to move through the linked list.
            # NOTE eventually, there will be a node that will have its current.next set to None which means it is the last node
        print("None")
        # After the loop completes (when current becomes None after traversing through the entire linked list), this line prints "None" to indicate the end of the linked list. This is added for visual clarity to signify that the linked list has been fully displayed.

# Create a linked list and add elements
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

# Display the linked list
my_list.display()
