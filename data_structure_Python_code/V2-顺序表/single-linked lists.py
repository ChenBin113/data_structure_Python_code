class SingleNode(object):
    def __init__(self, item):
        # 数据和指针
        self.item = item
        self.next = None


class SingleLinkedList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        # while cur is not None:
        # 当cur为真即存在
        while cur:
            print(cur.item)
            cur = cur.next
        return None

    def add_first(self, item):
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        node = SingleNode(item)
        # node = None
        # return
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            # cur一定存在，已经证明列表不为空
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        node =SingleNode(item)
        if pos <= 0:
            self.add_first(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            # pos位置是从0开始计数的
            # 插入是从前面插入
            while count < (pos - 1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self._head
        pre = None
        # 当列表不为空时才能执行操作
        while cur is not None:
            # 当数据符合条件时
            if cur.item is item:
                # 如果没有前一个存在即cur为列表第一个元素
                if not pre:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                # 不要忘记中断循环
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    sll = SingleLinkedList()
    sll.add_first(10)
    sll.add_first(20)
    sll.append(30)
    sll.insert(0, 4)
    print("Length of sll is {}".format(sll.length()))

    sll.travel()

    print(sll.search(30))
    print(sll.search(32))

    sll.remove(20)
    print("Length of sll is {}".format(sll.length()))
    sll.travel()