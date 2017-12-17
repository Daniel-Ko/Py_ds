from copy import deepcopy

class Stack:
    def __init__(self, data=[]):
        self.data = data

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data.pop())

    def peek(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data[-1])

    def size(self):
        return len(self.data)

class Queue:
    def __init__(self, data=[]):
        self.data = data

    def isEmpty(self):
        return self.data == []

    def offer(self, item):
        self.data.append(item)

    def poll(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data.pop(0))

    def peek(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data[0])

    def size(self):
        return len(self.data)   
    
class Deque:
    def __init__(self, data=[]):
        self.data = data

    def isEmpty(self):
        return self.data == []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data.pop())

    def offer(self, item):
        self.data.append(item)

    def poll(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data.pop(0))

    def peek_first(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data[0])

    def peek_last(self):
        if len(self.data) == 0:
            return None
        return deepcopy(self.data[-1])

    def size(self):
        return len(self.data)

class PriorityQueue:
    def __init__(self, data=[]):
        self.data = data
        if len(data) > 0:
            self.sink_down(0)

    def isEmpty(self):
        return self.data == []

    def bubble_up(self, index):
        if self.size() == 1:
            return
        
        parent = index // 2
        if 0 <= parent and self.data[index] > self.data[parent]:
            self.swap(index, parent)
            self.bubble_up(parent)
                

    def swap(self, ind1, ind2):
        a = self.data[ind1]
        self.data[ind1] = self.data[ind2]
        self.data[ind2] = a


    def sink_down(self, index):
        if self.size() <= 1:
            return

        left_child = (index << 1) + 1 
        right_child = (index << 1) + 2

        left_child_exists = left_child < self.size()
        right_child_exists = right_child < self.size()

        if left_child_exists and (self.data[left_child] > self.data[index]):
            if right_child_exists and (self.data[right_child] > self.data[left_child]):
                self.swap(right_child, index)
                self.sink_down(right_child)
            else:
                self.swap(left_child, index)
                self.sink_down(left_child)
        elif right_child_exists and self.data[right_child] > self.data[index]:
            self.swap(right_child, index)
            self.sink_down(right_child)


    def offer(self, item):
        self.data.append(item)
        self.bubble_up(len(self.data)-1)

    def poll(self):
        item = self.data.pop(0)
        self.sink_down(0)
        return item
        
    def size(self):
        return len(self.data)
    