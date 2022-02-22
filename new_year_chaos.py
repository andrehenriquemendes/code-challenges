
class Queue:
	def __init__(self, expected):
		self.initial = list(range(1, len(expected)+1))
		self.expected = expected
		self.count_swaps = 0
		self.is_too_chaotic = False

	def swap(self, i, j):
		self.initial[i], self.initial[j] = self.initial[j], self.initial[i]

def minimumBribes(q):
	queue = Queue(q)
	for i in range(len(q)):
		
		if queue.initial[i] == queue.expected[i]:
			continue
		
		elif i+1 < len(q) and queue.expected[i] == queue.initial[i+1]:
			queue.swap(i, i+1)
			queue.count_swaps += 1
		elif i+2 < len(q) and queue.expected[i] == queue.initial[i+2]:
			queue.swap(i+1, i+2)
			queue.swap(i, i+1)
			queue.count_swaps += 2
		
		else:
			queue.is_too_chaotic = True
			break
	
	if queue.is_too_chaotic:
		print('Too chaotic')
	else:
		print(queue.count_swaps)
	

if __name__ == '__main__':
	t = int(input().strip())
	
	for t_itr in range(t):
		n = int(input().strip())
		
		q = list(map(int, input().rstrip().split()))
		
		minimumBribes(q)