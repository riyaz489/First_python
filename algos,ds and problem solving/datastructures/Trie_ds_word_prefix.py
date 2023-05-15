import re


# this ds have O(26) = O(1) complexity for searching
class TrieNode:

    def __init__(self, ch):
        self.ch = ch
        # children means, immediate next chracters to form word
        self.children = []
        # if it is the last char of any word
        self.word_finished = False
        # how many times char appeared in the process
        self.counter = 1


def add(root, word):
    """ adding word to TRIE tree"""
    word = word.lower()
    node = root
    for char in word:
        found_in_child = False
        # searching for the character in the children of the present 'node'
        for child in node.children:
            if child.ch == char:
                # increase counter to keep track that, how many words are formed from this char at this place
                child.counter += 1
                node = child
                found_in_child = True
                break

        # if not found adding a new child
        if not found_in_child:
            new_node = TrieNode(char)
            i = 0
            for c in node.children:
                if c.ch < char:
                    i += 1
            node.children.insert(i, new_node)
            node = new_node

    node.word_finished =True


def find_prefix(root, prefix):
    """ give the last node of given prefix and also return if prefix exists and count of words with prefix"""
    node =root
    # if root is empty then, it means trie is empty
    if not root.children:
        return False, 0, node
    for char in prefix:
        char_not_found = True
        for child in node.children:
            if child.ch == char:
                char_not_found = False
                node = child
                break
        # return false if any of char of prefix is missing in our current node child
        if char_not_found:
            return False,  0, node

    # if we are out of loop, that means we found the prefix
    # counter represent, how many words this char have
    # because each time a new word is generated this counter updated
    # note: child count can not actually determine the number of words this char have below it
    return True, node.counter, node


def print_suggestions(prefix, node):
    global search_result
    if node.word_finished:
        search_result.append(prefix)
    for char in node.children:
        print_suggestions(prefix+char.ch, char)


def print_suggestion_wrapper(prefix,node, exists):
    global search_result
    search_result = []
    if not exists:
        #print('words not exits')
        return
    print_suggestions(prefix, node)


search_result = []
if __name__ == '__main__':
    para = input('enter para to store words\n')

    # this * is root node and this holds other TrieNode objects as child and this will make chain
    root = TrieNode('')
    for word in re.split('\W', para):
        add(root, word)

    # traversing all nodes of TRIE
    print('sorted array\n')
    print_suggestion_wrapper('', root, True)
    print(search_result)

    # searching words with prefix
    prefix = input('enter prefix to find suggestions\n')
    res = find_prefix(root, prefix)
    print_suggestion_wrapper(prefix, res[2], res[0])
    print(search_result)
