
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insert(self, value):
		node = Node(value)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
	
	def search(self, value):
		actual = self.head
		while actual is not None:
			if value == actual.value:
				return actual
			actual = actual.next
		return None
	
	def delete(self, value):
		actual = self.head
		prev = None
		while actual is not None:
			if value == actual.value:
				node_to_delete = actual
				break
			prev = actual
			actual = actual.next

		if node_to_delete is not None:
			if node_to_delete == self.head:
				self.head = node_to_delete.next
			elif node_to_delete == self.tail:
				prev.next = None
			else:
				prev.next = node_to_delete.next
			
			del node_to_delete
			
	def update(self, value, new_value):
		actual = self.head
		
		while actual is not None:
			if value == actual.value:
				actual.value = new_value
				break
			actual = actual.next
		
	
	def print(self):
		node = list.head
		while node is not None:
			print(node.value, end=' ')
			node = node.next


if __name__ == '__main__':
	
	values = [1, 2, 3, 6, 2, 20, 4, 22, 5]
	
	list = LinkedList()
	
	for value in values:
		list.insert(value)
	
	value_to_search = 1
	result_node = list.search(value_to_search)
	
	
	print(f'searching number {value_to_search}...')
	if result_node is not None:
		print(f'value found: {result_node.value}')
	else:
		print(f'value {value_to_search} was not found')
	
	
	list.print()
	
	print(f'deleting numbers 3, 1 and 5..')
	list.delete(3)
	list.delete(1)
	list.delete(5)
	
	print('\n')
	list.print()
	
	print(f'updating number 4 to 888')
	
	list.update(4, 888)
	
	list.print()