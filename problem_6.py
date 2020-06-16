class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def toList(self):
        list = []

        currentNode = self.head
        while currentNode:
            list.append(currentNode.value)
            currentNode = currentNode.next

        return list

def union(llist_1, llist_2):
    # Your Solution Here
    #combine both linked lists to lists
    list1 = llist_1.toList()
    list2 = llist_2.toList()
    #combine list to set
    set1 = set(list1)
    set2 = set(list2)

    #find union
    union_set = set1 | set2
    union_list = list(union_set) #back to a list
    #list to linked list
    combined_llist = LinkedList()
    for l in union_list:
        combined_llist.append(l)
    return combined_llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    list1 = llist_1.toList()
    list2 = llist_2.toList()

    set1 = set(list1)
    set2 = set(list2)

    union_set = set1 & set2
    union_list = list(union_set)

    combined_llist = LinkedList()
    for l in union_list:
        combined_llist.append(l)
    return combined_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

#Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5,linked_list_6))
print (intersection(linked_list_5,linked_list_6))