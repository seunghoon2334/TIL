class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n

front, rear = None, None

def enQueue(item):      # 연결큐의 삽입 연산
    global front, rear
    newNode = Node(item)#새로운 노드 생성
    if front == None:   #큐가 비어있다면
        front = newNode
    else:
        rear.next = newNode
    rear = newNode
def isEmpty():
    return front == None
def deQueue():
    global front, rear
    if isEmpty():
        print("Queue Empty")
        return None
    item = front.item
    front = front.next
    if front == None:
        rear = None
    return item
def Qpeek() :
    return front.item
def printQ():
    f = front
    s = ""
    while f:
        s += f.item+" "
        f = f.next
    return s

enQueue("A")
print(printQ())
enQueue("B")
print(printQ())
enQueue("C")
print(printQ())
deQueue()
print(printQ())
deQueue()
print(printQ())
deQueue()
print(printQ())
