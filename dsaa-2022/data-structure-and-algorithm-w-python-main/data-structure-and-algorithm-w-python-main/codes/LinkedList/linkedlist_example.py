class Node: 
    def __init__(self, data):
        self.data = data  
        self.next = None  

a = Node(11)
b = Node(52)
c = Node(18)

a.next = b
b.next = c

b = None
c = None

print(f"1 ----->{a}")
print(f"2 ----->{a.next}")
print(f"3 ----->{a.next.next}")

print(f"4 ----->{a.next.data}")
print(f"5 ----->{a.next.next.data}")

