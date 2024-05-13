# same keys with different ordering of insertion can generate tree with different heights.
# also the longer the height of tree, the longer it will take time to perform search/delete/insert operations.
# for example if tree is skewed then it will take O(n) time.
# so we need to balance tree to that we can optimize other operations.

# https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
# check or 4 cases and how to fix them.