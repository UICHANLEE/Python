'''
Code -> Interpreter -> OS -> CPU,Memory

Array와 list의 단점
1. 데이터의 삽입이나 삭제를 위한 공간을 만드는 시간 사용
2. Fixed Size
3. Array의 공간확보

공간확보를 위한 Searching Time (Flexible & Speed)

Linked List
1. 데이터를 순서대로 memory 주소기반으로 연결
2. Array와 같은 메모리 공간의 확보없이 데이터를 연결
3. Insertion과 deletion 등 기존 array 대비 연산장점을 가짐

Node에 구조체를 가지고 있음 (Class)
Iterable한 구조 => forloop와 같이 하나씩 가져와서 출력  
'''



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

print(a)
print(a.next)
print(a.next.next)

print(a.next.data)
print(a.next.next.data)

import random
 
class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1

for eggs in RandomIterable():
    print(eggs)
