# Node class
class Node:

# Function to initialise the node object
    def __init__(self, key, data):
        self.key = key
        self.data = data # Assign data
        self.next = None # Initialize next as null
        self.prev = None # Initialize prev as null


# Queue class contains a Node object
class Queue:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last=None


# Function to add an element data in the Queue
    def enqueue(self, key, data):
        if self.last is None:
            self.head = Node(key, data)
            self.last = self.head
            return self.head
        else:
            self.last.next = Node(key, data)
            self.last.next.prev = self.last
            self.last = self.last.next
            return self.last

    def dequeueNode(self, node):
        '''
        remove the node by severing the connections
        between it and its previous and next
        and then create a connection between its previous and next
        '''

        if node.prev is not None:
            node.prev.next = node.next
            node.next.prev = node.prev

        if node is self.head:
            self.head = self.head.next

        return node.data

    # Function to remove first element and return the element from the queue
    def dequeue(self):

        if self.head is None:
            return None
        else:
            temp= self.head
            self.head = self.head.next
            self.head.prev=None
            return temp


    # Function to return top element in the queue
    def first(self):
        return self.head.data


    # Function to return the size of the queue
    def size(self):

        temp=self.head
        count=0
        while temp is not None:
            count=count+1
            temp=temp.next
        return count


    # Function to check if the queue is empty or not
    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False

class LRU_Cache(object):

    def __init__(self, capacity):
        '''
        We will be using a queue as the data structure that holds the keys.
        The queue will be built with a doubly linked list.
        This is because in order for the LRU element to be removed,
        the data structure must be FIFO. The queue will store the values.

        We will also be using a dictionary to store the keys and nodes in the queue.
        '''

        # Initialize class variables
        self.queue = Queue()
        self.capacity = capacity
        self.dict = dict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dict:
            #update the cache
            data = self.queue.dequeueNode(self.dict[key]) #remove the node from its current spot
            newNode = self.queue.enqueue(key, data) #add it to the front of the queue
            self.dict[key] = newNode #update the dictionary
            return self.dict[key].data #return the data of the node
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        #remove the LRU is the capacity is reached
        if self.queue.size() == self.capacity:
            lru = self.queue.dequeue() #remove the LRU
            del self.dict[lru.key]

        #now, we enqueue the new item
        newNode = self.queue.enqueue(key, value)
        #and we update the dictionary with the new node
        self.dict[key] = newNode

    def printCache(self):
        currentNode = self.queue.head
        print("  ")
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
        print("  ")


#Test case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

#Test case 2
cache2 = LRU_Cache(5)
cache2.set(1, 1)
cache2.set(2, 4)
cache2.set(3, 9)
cache2.set(4, 16)
cache2.set(5, 25)
cache2.set(6, 36)
print(cache2.get(2))
# returns 4
print(cache2.get(1))
# returns -1 because 6 is not present in the cache

#Test case 3
empty_cache = LRU_Cache(5)
print(cache2.get(1))
#returns -1