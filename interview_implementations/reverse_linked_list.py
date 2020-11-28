class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):

        if not self.head:
            self.head =  Node(value)
            return

        current = self.head
        while True:
            if not current.next:
                current.next = Node(value)
                break
            else:
                current = current.next
    
    def reverse(self):
        current = self.head
        prev = None
        while True:
            if current.next:
                if not prev:
                    temp = current
                    current = current.next
                    temp.next = None
                    prev = temp
                else:
                    temp = current
                    current = current.next
                    temp.next = prev
                    prev = temp
            else:
                current.next = prev
                self.head = current
                break
                
                
if __name__ == "__main__":

    linked_list = LinkedList()
    for i in range(0, 10):
        linked_list.add(i)
    
    current = linked_list.head
    while True:
        print(current.value, end=" ")
        if current.next:
            current = current.next
        else:
            break
    print("\n")
    
    linked_list.reverse()
    while True:
        print(current.value, end=" ")
        if current.next:
            current = current.next
        else:
            break
    print("\n")