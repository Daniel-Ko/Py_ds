import data_structures as ds

#==================================
#           STACK TESTS
#==================================

# test initialisation conditions
stack = ds.Stack()
assert stack.size() == 0
assert stack.isEmpty()

# test push() conditions
stack.push('abc')
assert stack.size() == 1
assert not stack.isEmpty()

# test pop() conditions
assert stack.pop() == 'abc'
assert stack.size() == 0
assert stack.isEmpty()

# test null cases
assert stack.pop() == None
assert stack.peek() == None

# test correct execution
stackwithwrapper = ds.Stack([0, 1, 2, 3], ) 
assert stackwithwrapper.pop() == 3
assert stackwithwrapper.peek() == 2
assert stackwithwrapper.size() == 3

# test object reference is returned
stackwithobj = ds.Stack([[0, 1], [2, 3], [4, 5]]) # stack of lists
(stackwithobj.peek())[0] = 6
assert (stackwithobj.peek())[0] == 6
assert (stackwithobj.pop())[0] == 6


#==================================
#           QUEUE TESTS
#==================================

# test initialisation conditions
queue = ds.Queue()
assert queue.size() == 0
assert queue.isEmpty()

# test push() conditions
queue.offer('abc')
assert queue.size() == 1
assert not queue.isEmpty()

# test pop() conditions
assert queue.poll() == 'abc'
assert queue.size() == 0
assert queue.isEmpty()

# test null cases
assert queue.peek() == None
assert queue.poll() == None

# test correct execution
queuewithwrapper = ds.Queue([0, 1, 2, 3])
assert queuewithwrapper.poll() == 0
assert queuewithwrapper.peek() == 1
assert queuewithwrapper.size() == 3

# test object reference is returned
queuewithobj = ds.Queue([[0, 1], [2, 3], [4, 5]]) # queue of lists
(queuewithobj.peek())[0] = 6
assert (queuewithobj.peek())[0] == 6
assert (queuewithobj.poll())[0] == 6


#==================================
#           DEQUE TESTS
#==================================

# test initialisation conditions
deque = ds.Deque()
assert deque.size() == 0
assert deque.isEmpty()

# test push() conditions
deque.offer('abc')
assert deque.size() == 1
assert not deque.isEmpty()

# test pop() conditions
assert deque.poll() == 'abc'
assert deque.size() == 0
assert deque.isEmpty()

# test push() conditions
deque.push('abc')
assert deque.size() == 1
assert not deque.isEmpty()

# test pop() conditions
assert deque.pop() == 'abc'
assert deque.size() == 0
assert deque.isEmpty()

# test null cases
assert deque.peek_first() == None
assert deque.poll() == None
assert deque.peek_last() == None
assert deque.pop() == None


# test correct execution
dequewithwrapper = ds.Deque([0, 1, 2, 3, 4])
assert dequewithwrapper.peek_first() == 0
assert dequewithwrapper.peek_last() == 4
assert dequewithwrapper.poll() == 0
assert dequewithwrapper.pop() == 4

assert dequewithwrapper.peek_first() == 1
assert dequewithwrapper.peek_last() == 3
assert dequewithwrapper.size() == 3


# test object reference is returned
dequewithobj = ds.Deque([[0, 1], [2, 3], [4, 5]]) # deque of lists
(dequewithobj.peek_first())[0] = 6
assert (dequewithobj.peek_first())[0] == 6
assert (dequewithobj.poll())[0] == 6

(dequewithobj.peek_last())[0] = 10
assert (dequewithobj.peek_last())[0] == 10
assert (dequewithobj.pop())[0] == 10

#==================================
#           HEAP TESTS
#==================================
heap = ds.PriorityQueue()
assert heap.size() == 0
assert heap.isEmpty()

heap.offer('d')
heap.offer('b')
heap.offer('c')
heap.offer('g')
heap.offer('a')
heap.offer('z')
heap.offer('m')

# check correct order
largerpoll = chr(ord('z')+1) # guaranteed to be larger than 'z'
while(not heap.isEmpty()):
    smallerpoll = heap.poll()
    assert smallerpoll < largerpoll
    largerpoll = smallerpoll







