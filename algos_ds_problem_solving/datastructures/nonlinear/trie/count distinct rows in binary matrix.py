# here we have to simply return the count unique of binary rows.
# [0,1,1,0]
# [1,0,1,0]
# [0,1,1,0]
# so output is 2 in this case.


# we cant use dict or set in this case, as list is mutable and we can't hash it.
# we have to use trie again.

from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: dict = field(default_factory=dict)
    is_end_of_word: bool = field(default=False)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # whenever do insert we will return True/ false . True if added and false if already same word exists.
    def insert(self, data):
        cur = self.root
        index = 0
        for ch in data:
            index += 1
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            if index == len(data) :
                # if we are at last word, then we can check if that word s already a end of some other word.
                # or it was not exists/false earlier.
                # if it was true then it means its duplicate word.
                # as there is only one way to reach to this last word, so would have reached to this last node.
                # ether by adding new prefix or following already added prefix.
                if not cur.children[ch].is_end_of_word:
                    cur.children[ch].is_end_of_word = True
                    return True
                else:
                    return False
            cur = cur.children[ch]


data = [[0,1,1,0],
        [1,0,1,0],
        [1,0,1,0],
        [1,1,1,0],
        [0,1,1,0]]

res = 0
t = Trie()
for i in data:
    if t.insert(i):
        res+=1
print(res)