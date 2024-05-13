# Trie is k-ary type tree.
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    children: dict = field(default_factory=dict)
    is_end_of_word: bool = field(default=False)

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, data): # O(size of word);
        cur = self.root
        index = 0
        for ch in data:
            index+=1

            # if this char not exits as child for current node then we will add it.
            if ch not in cur.children:
                cur.children[ch] = TrieNode()

            # marking last node as end_of_word True, whether its new node or existing node.
            if index == len(data):
                cur.children[ch].is_end_of_word = True

            # updating cur with current child.
            cur = cur.children[ch]

    def search(self, data):
        # while traversing char by char in tree we will return false false in 2 cases:
        # if current node does not have requested char as its child.
        # if we traversed whole word and last char is not end_of_word
        cur = self.root
        for i in data:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.is_end_of_word

    def delete(self, data):
        # for delete there will be 3 scenarios
        # 1. if this word is unique branch in the tree, and we can safely delete complete branch of this word from tree.
        # 2. requested word is prefix of some other word, then we will simply change end_of_word of last char of
        #    requested node to False
        # 3. other word is prefix of requested word, then we will delete last chars which are not overlapping with
        #    other words.

        def rec_delete(root, data,depth=0):

            # if we reached to last char then we will check if last node has children or not
            # it will cover 2nd scenario. if it has children then we will simply change its end_of_word flag to false.
            # if it has not children then we will delete this node. and we will delete its parents node also recursively
            # as we go back in recursive stack, until we found a node which has end_of_word as True.
            # if there is no node exists then we will end up deleting complete branch.
            # so this will cover 1st and 3rd scenario.

            nonlocal found_other_word_as_prefix

            if depth == len(data):
            # if last char
                if root.children:
                    # if node has childs then simply make current node as  `not a end of word`.
                    # 2nd scenario
                    root.is_end_of_word = False
                    return root
                else:
                    # we will remove this node
                    # 1st scenario
                    return None
            else:
                # going towards nextx child.
                if rec_delete(root.children[data[depth]], data, depth+1) is None:
                    # if we get None that means we removed that child, and we can remove it from dict
                    root.children.pop(data[depth])

                # if we found that there is some other word exists as prefix, then it means
                # we don't have to do delete/modification anymore of parent nodes, we can return as it is.
                if found_other_word_as_prefix:
                    return root

                # if we reached to this step that means we already traversed last char of word.
                # now we are traversing its parent nodes.
                if not root.is_end_of_word and not root.children:
                    # we will check for current node children also, because it might be possible that
                    # current node contains other branches/words, if we delete this we will lose other words also.
                    # 1st and 3rd scenario
                    return None
                else:
                    # return original node without any modification.
                    # 3rd scenario
                    found_other_word_as_prefix = True
                    return root

        # before calling this method we can search to check if word exists or not.

        # this will tell us if we end in 3rd scenario or not.
        found_other_word_as_prefix = False

        return rec_delete(self.root, data, 0)

    def print_suggestions(self, prefix):
        result = []

        # first reach to that prefix last node
        cur = self.root
        for i in prefix:
            cur = cur.children[i]
        # now cur is at prefix last char


        def find_words_with_prefix(root, word_so_far):
            if root.is_end_of_word:
                # add word to result
                result.append(word_so_far)

            for ch, node in root.children.items():
                # keep looking for other words
                find_words_with_prefix(node, word_so_far+ch)

        find_words_with_prefix(cur, prefix)
        return result

t = Trie()
t.insert('batter')
t.insert('bat')
t.insert('sad')
t.insert('bad')
print(t.search('battey'))


