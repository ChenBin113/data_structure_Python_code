class SingleNode(object):
	def __init__(self, item):
		# 数据和指针
		self.item = item
		self.next = None


class SingleCycleLinkedList(object):
	def __init__(self):
		self._head = None

	def is_empty(self):
		return self._head is None

	def length(self):
		if self.is_empty():
			return 0
		else:
			count = 1
			cur = self._head
			# 当循环一周后终止
			while cur.next != self._head:
				count += 1
				cur = cur.next
			return count

	def travel(self):
		if self.is_empty():
			return
		cur = self._head
		while cur.next != self._head:
			cur = cur.next
			print(cur.item)

	def add_first(self, item):
		node = SingleNode(item)
		if self.is_empty():
			self._head = node
			node.next = self._head
			# node.next = node
		else:
			# 插入头部
			node.next = self._head
			cur = self._head
			# 因为是循环表，还需要把最后一个连接到这个插入项
			while cur.next != self._head:
				cur = cur.next
			cur.next = node
			# 将head指针指向node
			self._head = node
