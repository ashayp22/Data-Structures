import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = self.data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class BlockChain:

    def __init__(self):
        self.head = None

    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, 0)
        else:
            # Move to the tail (the last node)

            node = self.head
            while node.next:
                node = node.next

            node.next = Block(timestamp, data, self.head.hash)
            node.next.previous_hash = node.hash

    def print_chain(self):
        node = self.head
        while node:
            print("-----------------")
            print("Timestamp: " + str(node.timestamp))
            print("Data: " + str(node.data))
            print("SHA256 Hash: " + str(node.hash))
            print("Previous Hash: " + str(node.previous_hash))
            print("-----------------")
            node = node.next


def getTime():
    ts = time.gmtime()
    return time.strftime("%Y-%m-%d %H:%M:%S", ts)

#Test case 1

chain1 = BlockChain()
chain1.append(getTime(), "data 1")
chain1.append(getTime(), "data 2")
chain1.append(getTime(), "data 3")
chain1.print_chain()

#Test case 2

chain2 = BlockChain()
chain2.print_chain()

#test case 3

chain3 = BlockChain()
chain3.append(getTime(), "data 1")
chain3.append(getTime(), "data 2")
chain3.append(getTime(), "data 3")
chain3.append(getTime(), "data 4")
chain3.append(getTime(), "data 5")
chain3.append(getTime(), "data 6")
chain3.print_chain()