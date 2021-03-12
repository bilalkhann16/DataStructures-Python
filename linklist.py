class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class LL:
    def __init__(self):
        self.head = None

    def insert(self, value):
        n = Node(value)
        print ('n.val', n.val)

        if self.head == None:
            print ('list empty')
            self.head = n
            self.current = self.head
        else:
            while(self.current.next == None):
                print('I am here')
                self.current.next= n
                self.current = self.current.next
                return
            self.current = self.current.next
            
        
    def printll(self):
        self.current= self.head
        while (self.current):
            print (self.current.val)
            self.current = self.current.next

L = LL()
L.insert(12)
L.insert(13)
L.insert(15)
L.insert(16)
L.insert(18)
L.insert(22)
L.printll()
