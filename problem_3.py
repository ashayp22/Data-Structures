import sys

class Node(object):

    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.right = None
        self.left = None


class PriorityQueue(object):

    def __init__(self):
        self.queue = []

    #convert to a string
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def __len__(self):
        return len(self.queue)

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def pop(self):
        min = 0 #the smaller the frequency of the node, the better chance to pop
        for i in range(1, len(self.queue)):
            if self.queue[i].frequency < self.queue[min].frequency:
                min = i
        chosenNode = self.queue[min]
        del self.queue[min]
        return chosenNode

def huffman_encoding(data):
    '''
    :param data: a string containing the data to be encoded
    :return encoded_data: the encoded data, string
    :return tree: the root node for the Huffman tree
    '''

    if data == "":
        return "", None


    '''
    First, determine the frequency of each character in the message
    '''
    frequency_dict = {}
    for d in data:
        if d not in frequency_dict:
            frequency_dict[d] = 0
        else:
            frequency_dict[d] += 1
    '''
    Second,  build and sort a list of nodes in the order lowest to highest frequencies.
    This requires a priority queue
    '''

    priority_queue = PriorityQueue() #create the priority queue
    for key, value in frequency_dict.items(): #add each character and its frequency
        priority_queue.insert(Node(key, value))

    '''
    Do the following:
    1.) Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
    2.) Create a new node with a frequency equal to the sum of the two nodes picked in the above step. 
    3.) Reinsert the newly created node back into the priority queue.
    4.) Repeat steps 1-3 until there is a single element left in the priority queue
    '''

    while len(priority_queue) > 1:
        #grab the two nodes with highest priority
        node1 = priority_queue.pop() #lower frequency
        node2 = priority_queue.pop() #higher frequency

        combinedNode = Node(None, node1.frequency + node2.frequency)
        combinedNode.left = node1
        combinedNode.right = node2

        priority_queue.insert(combinedNode)

    '''
    Based on the Huffman tree, generate unique binary code for each character of our string message. 
    For this purpose, you'd have to traverse the path from root to the leaf node.
    '''

    #generates a binary code for each character
    def generateBinaryCode(node, current):

        code_dict = {}

        #check if character exists
        if node.character is not None:
            code_dict[node.character] = current
            return code_dict

        #check left
        if node.left is not None:
            code_dict.update(generateBinaryCode(node.left, current + "0"))

        #check right
        if node.right is not None:
            code_dict.update(generateBinaryCode(node.right, current + "1"))

        #return the dict
        return code_dict

    root_node = priority_queue.pop()
    binary_codes = generateBinaryCode(root_node, "")

    #Finally, we generate the encoded_data

    encoded_data = ""

    for d in data:
        encoded_data += binary_codes[d]

    return encoded_data, root_node



def huffman_decoding(data, tree):
    '''
    :param data: the encoded string
    :param tree: the root node for the tree
    :return: the decoded string
    '''

    '''
    First, declare a blank decoded string
    '''
    decoded_data = ""

    if tree is None:
        return decoded_data

    '''
    Next, pick a bit from the encoded data, traversing from left to right.
    Start traversing the Huffman tree from the root.
    If the current bit of encoded data is 0, move to the left child
    Else move to the right child of the tree if the current bit is 1.
    
    If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    '''

    current_node = tree
    for d in data:
        if d == "0": #have to move left
            current_node = current_node.left #traverse left
        elif d == "1": #have to move right
            current_node = current_node.right #traverse right
        if current_node.character is not None: #check to see if a character exists
            decoded_data += current_node.character #add to the decoded data
            current_node = tree #go back to the root

    return decoded_data

if __name__ == "__main__":
    codes = {}

    # Test case 1

    a_great_sentence = "the bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2

    a_great_sentence = "aaaabbbb"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3

    a_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))