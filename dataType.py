from typing import Text


class Stack:
    def __init__(self) -> None:
        self.li = []

    def append(self, data):
        self.li.append(data)

    def pop(self):
        if self.getSize() > 0:
            return self.li.pop()

    def getSize(self):
        return len(self.li)

    def clear(self):
        self.li.clear()


class Queue:
    def __init__(self) -> None:
        self.li = []

    def enqueue(self, data):
        self.li.append(data)

    def pop(self):
        if self.getSize() > 0:
            return self.li.pop(0)

    def getSize(self):
        return len(self.li)

    def clear(self):
        self.li.clear()


class Node():
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next


class Link():
    def __init__(self, head=None) -> None:
        txt = ''
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            t = self.head
            while t.next != None:  # Run to last
                t = t.next
            t.next = newNode
            newNode.prev = t

    def getSize(self):
        t = self.head
        count = 0
        while t:
            t = t.next
            count += 1
        return count

    def isEmpty(self):
        if self.getSize() == 0:
            return True
        else:
            return False

    def pop(self, pos=-1):

        if self.getSize() > 0:
            if pos == -1:
                pos = self.getSize() - 1

            if pos == 0:
                result = self.head.data
                temp = self.head.next
                del self.head
                self.head = temp
                return result
            elif pos < self.getSize() - 1:
                t = self.head
                for i in range(pos-1):
                    t = t.next
                result = t.next.data
                t.next = t.next.next
                return result
            elif pos == self.getSize() - 1:
                t = self.head
                while t.next.next != None:
                    t = t.next
                result = t.next.data
                del t.next
                t.next = None

                return result

    def getTail(self):
        if self.getSize() > 0:
            t = self.head
            while t.next != None:
                t = t.next
            return t
        else:
            return None

    def __str__(self):
        txt = ''
        t = self.head
        isStart = False
        while t:
            if isStart == True:
                txt += " -> "
            txt += str(t.data)
            isStart = True

            t = t.next
        return txt

    def show(li):
        for i in range(len(li)):
            print("{} : {}".format(i, li[i]))

    def getValue(self):
        return self.txt


class TestObj:
    def __init__(self, text: str, day: int) -> None:
        self.text = text
        self.day = day

    def __str__(self) -> str:
        return "{}:{}".format(self.text, self.day)


def sort(li: Link, dayTarget: int):
    node = li.head
    tempNode = None
    if li.head.data.day < dayTarget and li.getSize() > 1:
        while node.next != None:
            if node.next.data.day >= dayTarget and tempNode == None:
                tempNode = node.next
                node.next = None
                node = tempNode
                # print("Found")
            else:
                node = node.next

        else:
            if tempNode != None:
                node.next = li.head
                li.head = tempNode
    node = li.head
    li = []
    while node != None:
        li.append(node.data)
        node = node.next
    return li

# linkList = Link()
# linkList.append(TestObj("Test1",0))
# linkList.append(TestObj("Test2",1))
# linkList.append(TestObj("Test3",1))
# linkList.append(TestObj("Test4",3))
# linkList.append(TestObj("Test5",5))
# dayTarget = 1
# print(linkList)
# linkList = sort(linkList,dayTarget)
# print("sort---------")
# for i in linkList:
#     print(i)
