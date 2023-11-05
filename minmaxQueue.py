from collections import deque as dq
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
    
    def isEmpty(self):
        return not self.D



