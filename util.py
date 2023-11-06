# Python 3 implementation to design
# a queue data structure to get
# minimum element in O(1) time
from collections import deque as dq

# class for the queue

class MinMaxQueue:

	def __init__(self):
		# Queue to store the
		# element to maintain the
		# order of insertion
		self.Q = dq([])

		# Doubly ended queue to
		# get the minimum element
		# in the O(1) time
		self.D = dq([])

	# Function to push a element
	# into the queue
	def enque_element(self, element):
		# If there is no element
		# in the queue
		if (len(self.Q) == 0):
			self.Q.append(element)
			self.D.append(element)

		else:
			self.Q.append(element)

			# Pop the elements out
			# until the element at
			# back is greater than
			# current element
			while (self.D and
				self.D[-1][0] > element[0]):
				self.D.pop()

			self.D.append(element)

	# Function to pop the element
	# out from the queue

	def deque_element(self,):
		# Condition when the Minimum
		# element is the element at
		# the front of the Deque
		if (self.Q[0] == self.D[0]):
			self.Q.popleft()
			self.D.popleft()

		else:
			self.Q.popleft()

	# Function to get the
	# minimum element from
	# the queue

	def getMin(self,):
		return self.D[0]

def get_trace(pred, n):
    id_list = []
    id = pred[n]
    while id >= 0:
        id_list = [id] + id_list
        id = pred[id]
    return id_list

# test
if __name__ == '__main__':
	k = MinMaxQueue()
	example = [1, 10, 5, 6, 2]

	# Loop to enque element
	for i in range(5):
		k.enque_element(example[i])

	print(k.getMin())
	k.deque_element()
	print(k.getMin())
