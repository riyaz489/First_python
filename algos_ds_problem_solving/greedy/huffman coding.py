# Huffman coding is a lossless data compression algorithm. The idea is to assign variable-length codes
# to input characters, lengths of the assigned codes are based on the frequencies of corresponding characters.
# The most frequent character gets the smallest code and the least frequent character gets the largest code.
from queue import PriorityQueue

# The variable-length codes assigned to input characters are Prefix Codes, means the codes (bit sequences) are
# assigned in such a way that the code assigned to one character is not the prefix of code assigned to any other
# character. This is how Huffman Coding makes sure that there is no ambiguity when decoding the generated bitstream.
# Let us understand prefix codes with a counter example. Let there be four characters a, b, c and d, and their
# corresponding variable length codes be 00, 01, 0 and 1. This coding leads to ambiguity because code assigned
# to c is the prefix of codes assigned to a and b. If the compressed bit stream is 0001, the de-compressed
# output may be "cccd" or "ccb" or "acd" or "ab".
# See this for applications of Huffman Coding.

# There are mainly two major parts in Huffman Coding:
# 1. Build a Huffman Tree from input characters.
# 2. Traverse the Huffman Tree and assign codes to characters.

# Steps to build Huffman Tree:
# 1. Input is an array of unique characters along with their frequency of occurrences and output is Huffman Tree.
#    Create a leaf node for each unique character and build a min heap of all leaf nodes (Min Heap is used as a priority
#    queue. The value of frequency field is used to compare two nodes in min heap. Initially, the least frequent
#    character is at root)
# 2. Extract two nodes with the minimum frequency from the min heap.
# 3. Create a new internal node with a frequency equal to the sum of the two nodes frequencies. Make the first
# extracted node as its left child and the other extracted node as its right child. Add this node to the min heap.
# Repeat steps#2 and #3 until the heap contains only one node. The remaining node is the root node and the
# tree is complete.

# by building using mean heap ensures that chars which has least freq will have more depth in tree.
# that means they get larger lenght codes to represent, in comparison to high freq chars.
# Also as we are building binary tree and only leaf node represent each char and its freq.
# and if we take path of leaf nodes (from root to leaf) in binary tree, then it will always be unique.
# so it will ensure that any code will not be prefix of another code.
# if we could have used non-leaf nodes to represent our chars, then we could have got the codes which is prefix of
# other nodes.
#    5  (0)
#(0) /  \ (1)
#   2  3
# as you can notice 2 code will be (00) and 3 code will be (01).

# Steps to print codes from Huffman Tree:
# Traverse the tree formed starting from the root. Maintain an auxiliary array. While moving to the left child,
# write 0 to the array. While moving to the right child, write 1 to the array. Print the array
# when a leaf node is encountered.

# note: you might be wondering for same freq chars it will give same code but that's not the case.
# even if we have same frequency for few chars, huffman coding will give optimal results.
# because same freq items will be added in same level ether as left or right child.
# we are marking leaf nodes with char name, as for different chars we have different leaf nodes.
# that means we will get different codes also.

import heapq


# because we don't have custom comparator functionality in python heapq or PriorityQueue classes.
# so we will provide custom comparator in our input data itself.
# we will covert input data into HuffManNode, where we have defined custom comparator for each data.
class HuffManNode:
    def __init__(self, freq, char=None):
        self.freq=freq
        self.char = char
        self.left = None
        self.right = None

    def __ge__(self, other):
        return self.freq >= other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __le__(self, other):
        return self.freq <= other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

# our tree after this method look like
# for input a: 3, b: 2, c:1

#             (6, '')
#            /       \
#         (3, 'a')  (3, '')
#                    /     \
#                 (1,'c')  (2,'b')

def build_huffman_coding_tree(data:dict):

    # create a tree first
    heap = []
    for k, v in data.items():
        # first converting items to huffmanNode class objects, so that heapq can do > < operations.
        # then pushing into min heap
        heapq.heappush(heap, HuffManNode(freq=v, char=k))

    # now remove items from heap and build tree
    while len(heap) > 1:
        left_node = heapq.heappop(heap)
        right_node = heapq.heappop(heap)

        new_node = HuffManNode(freq=(left_node.freq + right_node.freq))
        # smaller items goes on left side and greater one on right side. (if both are equal then its just random
        # assignment) and their sum will become new node.
        # well id doesn't if we put some node on right or left, the only thing matters is lower freq items should be at
        # highest depth.
        new_node.left = left_node
        new_node.right = right_node
        # above statements will construct tree from bottom to top

        # adding new node to heap again
        heapq.heappush(heap, new_node)


    # last remaining item in heap, will be root node. which will be equal to sum of all frequencies.
    return heap[0]


def get_encoding_of_all_chars(root, s='', res={}):
    # we will do a simple prefix traversal, and keep adding encoded string to the respective character in res dict
    # if we fond leaf node and char for node is also not null that means we found complete encoding for current char.
    if root.left is None and root.right is None and root.char is not None:
        # adding encoding for char in res dict
        res[root.char] = s
        return
    # 0 for left traversal and 1 for right traversal
    get_encoding_of_all_chars(root.left, s+'0')
    get_encoding_of_all_chars(root.right, s+'1')

    return res


def decode_char(root, encoded_data):
    cur = root
    for i in encoded_data:
        if cur is None:
            return None
        if i=='0':
            cur = cur.left
        else:
            cur = cur.right


    return cur.char

data = {'a': 60,
        'b':100,
        'c': 30,
        'd':10,
        'e':20,
        'f': 30}
root = build_huffman_coding_tree(data)
res = get_encoding_of_all_chars(root)
print(data)
print(res)
print(decode_char(root, res['c']))
