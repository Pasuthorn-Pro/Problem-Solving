class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None
    
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Given a reference to the head of a list and a key,
    # delete the first occurrence of key in the linked list
    def deleteNode(self, key):
        # Case 1: The list is empty
        if self.head is None:
            print("List is empty")
            return

        # Case 2: If the node to be deleted is the head
        if self.head.data == key:
            self.head = self.head.next
            return
        
        # Case 3: Search for the key in the rest of the list
        current = self.head
        while current.next is not None:
            if current.next.data == key:
                current.next = current.next.next  # Delete the node
                return
            current = current.next
    
    # Function to reverse the linked list
    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next  
            current.next = prev       
            prev = current            
            current = next_node
        
        self.head = prev  

    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print("%d" %(temp.data))
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)
    
    print("Created Linked List:")
    llist.printList()
    
    llist.deleteNode(1)
    print("Linked List after Deletion of 1:")
    llist.printList()

    llist.reverseList()
    print("Reversed Linked List:")
    llist.printList()
