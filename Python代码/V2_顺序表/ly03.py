class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head == None

    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur != None:
            print( cur.item)
            cur = cur.next

    def add(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.prev = cur



    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = Node(item)
            cur = self._head
            count = 0
            # 移动到指定位置的前一个位置
            while count < (pos - 1):
                count += 1
                cur = cur.next
            # 将node的prev指向cur
            node.prev = cur
            # 将node的next指向cur的下一个节点
            node.next = cur.next
            # 将cur的下一个节点的prev指向node
            cur.next.prev = node
            # 将cur的next指向node
            cur.next = node

    def remove(self, item):
        if self.is_empty():
            return
        else:
            cur = self._head
            if cur.item == item:
                if cur.next == None:
                    self._head = None
                else:
                    cur.next.prev = None
                    self._head = cur.next
                return
            while cur != None:
                if cur.item == item:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    break
                cur = cur.next

if __name__ == "__main__":
    ll = DLinkList()
    ll.add(1)
    ll.add(2)
    ll.append(3)
    ll.insert(2, 4)
    ll.insert(4, 5)
    ll.insert(0, 6)
    print( "length: ", ll.length())
    ll.travel()
    print( ll.search(3))
    print( ll.search(4))
    ll.remove(1)
    print( "length:", ll.length())
    ll.travel()

