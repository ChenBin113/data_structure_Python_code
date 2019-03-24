

class SingleNode(object):

    def __init__(self, item):
        self.item = item

        self.next = None


class SingleLinkList(object):

    def __init__(self):
        self._head = None


    def isEmpty(self):
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

        while cur:
            print(cur.item)
            cur = cur.next

        return None

    def addFirst(self, item):
        node = SingleNode(item)

        node.next = self._head

        self._head = node


    def append(self, item):
        node = SingleNode(item)

        if self.isEmpty():
            self._head = node

        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.addFirst(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0

            pre = self._head
            while count<(pos-1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self._head
        pre = None

        while cur != None:
            if cur.item == item:
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next

                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False



if __name__ == "__main__":
    sll = SingleLinkList()
    sll.addFirst(10)
    sll.addFirst(20)
    sll.append(30)
    sll.insert(2,4)

    print("Length of sll is {0}".format(sll.length()))

    sll.travel()

    print(sll.search(30))
    print(sll.search(32))

    sll.remove(20)
    print("Length of sll is {0}".format(sll.length()))
    sll.travel()