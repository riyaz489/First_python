### lru cache ####
# remove the least recent used data from cache
# it can be done easily with ordered dict also
# behind the scenes ordered dict also used doubly linked list and hashmap(dict) to get items in o(1) and
# maintain order at the same time, like we did below


# doubly linked list to maintain ordering and in dict we will store linked list node memory location, so that
# we can access any data from linked list in o(1), and we used double linked list, so that we can remove
# last element in o(1), because we are adding from front and removing from back, so we can easily
# fetch first,second and last and second last values using doubly linked list
class DoubleLinkedList:
     def __init__(self, data,key,next_p=None, prev=None):
         self.next_p=next_p
         self.prev = prev
         self.data = data
         self.key = key


class LRUCache:
    def __init__(self, limit):
        self.limit = limit
        self.last = None
        self.head = None
        self.dct = dict()

    def get(self, key):
        if key not in self.dct:
            return -1
        else:
            pointer = self.dct[key]
            self.move_node_to_top(pointer)
            return pointer.data


    def set(self, key,value):

        if key in self.dct:
            self.move_node_to_top(self.dct[key])
            self.dct[key].data = value
        else:
            if len(self.dct) == self.limit:
                node = self.remove_from_last()
                if node:
                    self.dct.pop(node.key)
            self.dct[key] = DoubleLinkedList(key=key,data=value)
            self.add_node_to_top(self.dct[key])

    def add_node_to_top(self,node):
        if self.head is not None:
            self.head.prev = node
            node.next_p = self.head
        else:
            self.last = node
        self.head = node

    def remove_from_last(self):
        if self.last is None:
            return
        else:
            temp = self.last
            if self.last.prev is not None:
                self.last = self.last.prev
                self.last.next_p = None
            else:
                self.last = None
                self.head = None
            return temp

    def move_node_to_top(self, node):

        if self.head == node:
            return
        else:
            if self.last == node:
                self.last = node.prev
                self.last.next_p = None
            else:
                node.prev.next_p = node.next_p
                node.next_p.prev = node.prev
            self.head.prev = node
            node.next_p = self.head
            self.head = node
            self.head.prev = None

lRUCache = LRUCache(2)
lRUCache.set(1, 1)
lRUCache.set(2, 2)
print(lRUCache.get(1))
lRUCache.set(3, 3)
print(lRUCache.get(2))


from collections import OrderedDict

class LRUCache2:
 # all the functions are similar behind the scenes, what we implemented above
    def __init__(self, limit):
        self.limit = limit
        self.dct = OrderedDict()
    def set(self, key, value):
        if key in self.dct:
            self.dct.move_to_end(key,last=True)
            self.dct[key]=value
        else:
            if len(self.dct) == self.limit:
                self.dct.pop(list(self.dct.keys())[0])
            self.dct[key]= value
    def get(self,key):
        if key in self.dct:
            self.dct.move_to_end(key,last=True)
            return self.dct[key]
        else: return -1

lRUCache = LRUCache2(2)
lRUCache.set(1, 1)
lRUCache.set(2, 2)
print(lRUCache.get(1))
lRUCache.set(3, 3)
print(lRUCache.get(2))