class DoublyNode:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = DoublyNode()
        self.tail = DoublyNode()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.length = 0
    def append(self, value): #append by value to the end
        if isinstance(value, bool):
            raise ValueError("Value is bool")
        if value is None:
            raise ValueError("Value is null")
        newNode = DoublyNode(value)
        prevNode = self.tail.prev

        prevNode.next = newNode
        self.tail.prev = newNode

        newNode.next = self.tail
        newNode.prev = prevNode

        self.length+=1

    def prepend(self, value): #append by value to the start
        if not value or isinstance(value, bool):
            raise ValueError("Invalid Value | Value is null or bool")
        newNode = DoublyNode(value)
        firstNode = self.head.next

        self.head.next = newNode
        firstNode.prev = newNode

        newNode.next = firstNode
        newNode.prev = self.head

        self.length+=1 

    def insert(self, value, index: int): #append value to index | iterate through everything
        if not 0<=index < self.length:
            raise IndexError("Index not in range.")
        if not value or isinstance(value, bool):
            raise ValueError("Invalid Value | Value is null or bool")
        
        newNode = DoublyNode(value)
        current = self.head
        counter = 0

        while current.next!=self.tail:
            if counter == index:
                current = current.next
                prevNode = current.prev
                current.prev = newNode
                prevNode.next = newNode
                newNode.next = current
                newNode.prev = prevNode
                self.length+=1
                return
            counter+=1
            current = current.next
        return
    
    def remove(self, value): #remove by value | iterate through everything

        found: bool = False
        current = self.head
        while current != self.tail:
            if current.value == value:
                found = True
                deleted = current
                prevNode = deleted.prev
                nextNode = deleted.next
                
                prevNode.next = nextNode
                nextNode.prev = prevNode
                self.length-=1
                return
            current = current.next
        
        if not found:
            raise ValueError("Value not found.")
        return
    
    def pop(self, index: int=None): #remove by index or remove the end if index is None | iterate through everything

        current = self.head
        end = self.tail
        counter = 0
        if index is None:
            deleted = end.prev
            prevNode = deleted.prev
            prevNode.next = end
            end.prev = prevNode
            self.length-=1
            return
        
        if not 0 <= index <self.length:
            raise IndexError("Error out of range")
        
        while counter != index:
            counter+=1
            current = current.next
        
        deleted = current.next
        prevNode = deleted.prev
        nextNode = deleted.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.length-=1
        return deleted

    def display(self): #display or return a list of nodes
        current = self.head
        nodes = []
        while current.next != self.tail:
            nodes.append(current.next.value)
            current = current.next

        return nodes
    
    def getLength(self):
        return self.length
    
    def __str__(self):
        current = self.head
        nodes = []
        while current.next != self.tail:
            nodes.append(current.next.value)
            current = current.next

        return str(nodes)

    def __getitem__(self, index: int):
        if not 0<= index < self.length:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.next.value

    def __iter__(self):
        current = self.head
        while current.next != self.tail:
            yield current.next.value
            current = current.next
        return
    
    def nodes(self):
        current = self.head
        while current != self.tail:
            yield current.next
            current = current.next
        return
    
def main()->None:
    pass

if __name__ == "__main__":
    main()
