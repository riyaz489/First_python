# disjoint sets are those set which has nothing in common.
# now here each set represent different universe.
# when we do a union of 2 sets, then all the items present in both sets now become part of new larger set.

# now let take a sample problem, we have give some list of persons. now our task it to
# make friedns. when we make 2 people friend, we want that their friends or friend also become friend.
# for example: A is friend of B and D is friend of C. and if we make B and C friends, then A and D also become friends
# next operation is to find if X is friend of Y or not.

# now if we are going to implement it using normal python set, then it would be very difficult.
# as we will need different sets for different friendship.
# also to make friend of friend operation will be in-efficient.

# So for this kind of problem, where  changing one item in universe will change all items in given universe.
# it is also to keep track of connected items

# so we will implement this data structure using tree, lets consider friends problem mentioned above.
# lets say each node of tree has 2 properties, one is data another one is parent.
# note this tree will be different than normal tree as here nodes will keep track of parent, instead of child.
# and multiple nodes can have same parent.
# initially, each node will point to itself as parent.
# when we call make friends function, then one node will make its parent as other node.
# for now we will choose leader randomly.
# -> 1<-2
# |__|
# if we make 1 and 2 friends,  now you can see 1 is pointing to itself and 2 is now pointing to 1.
# each tree will have one representative which will be first parent in each tree, which we randomly choose above.

# for example:
#      ____
#      |  |
#      |_>3
#         |\
#         1 2
#         |
#         4
# representative of 4,1,2,3 is 3.

# whenever we want to check friendship status we will simply check who is final parent(representative) of given nodes.
# if they are same then it means they are friends.

# and whenever we do union we move nodes representative node the current node.
# because if we move only current node then only current node friends will be changed,  but we want
# to change its friends of friends. so to do so we move whole representative, so that current complete
# tree will become part of another tree.

# 1       5
# |       |
# 2       3

# if we want to make 3 with friends with 2 then we do union of 1 and 5 so that each node in left tree will become
# friend of each node in right tree.


# to optimize it we can simply implement it using array also, instead of tree.
# as array are cache friendly.
# we will simply create a parent array which will track who is parent of item at index i.
class DisJoinSet:

    def __init__(self, data):
        self.data = data
        # storing indices of each item in parent arr.
        # this array will store parent node index for node which present at index i.
        # as initially each node is parent of itself, so we just copied their own indicies.
        self.parent = [* range(len(data))]

        # this is used by rank union function.
        # initially rank for each node is 0
        self.rank = [0]* len(data)

    def simple_find_parent(self, node): #O(n)
        # this function return index instead of data
        if node == self.parent[node]:
            return node
        else:
            # we will recursively find this relationship representative.
            return self.simple_find_parent(self, self.parent[node])

    def simple_union(self,node1, node2): #O(n) in worst case
        # in this union we will simply make left node parent as representative. as we are going with random parent
        #  approach.

        node1_par = self.simple_find_parent(node1)
        node2_par = self.simple_find_parent(node2)

        if node1_par == node2_par:
            print(' they are alkready friends no need to join')
            return

        # make left node tree as representative.
        self.parent[node2_par] = node1_par

        # now consider a case when we got skewed tree.
        # like union(1,3)
        # tree be like  1<-3

        # then (2,3)
        # tree be like 2<-1<-3

        # then (4,3)
        # tree be like 4<-2<-1<-3

        # so here searching parent/ union operation will become O(n)
        # now we will write optimized methods, so that our tree height is balanced after union and search operations.

    def rank_union(self, node1, node2):
        # here we will use rank array to store rank of each node.
        # here rank represent depth of give tree.
        # The term rank is preferred instead of height because if path compression technique
        # (we have discussed it below) is used, then rank is not always equal to height.
        # our goal is to add new tree under higher rank representative tree.
        # because if we add tree under higher rank sub-tree then our resultant tree height will be smaller.
        #   1
        #   5<-6
        # if we do union of 1 and 6 then if we choose lower rank item, then tree will look like this.
        #  1<-5-<-6 # as you can see it increase tree depth.

        # if we choose higher rank tree as new representative then tree height remained same. which is 1 (counting edges)
        # 5<-6
        # ^
        # |
        # 1

        node1_par = self.path_compression_search(node1)
        node2_par = self.path_compression_search(node2)

        if self.rank[node1_par]> self.rank[node2_par]:
            self.parent[node2_par] = node1_par
        elif self.rank[node1_par]< self.rank[node2_par]:
            self.parent[node1_par] = node2_par

        else:
            # if both ranks are same then choosing left one as parent
            self.parent[node2_par] = node1_par
            self.rank[node1_par] +=1

    def path_compression_search(self, node):
        # here will change parent of current nodes while doing the search.
        # it will basically help up to reduce the height of tree.
        # The idea of path compression is to make the found root as parent of x
        # so that we don't have to traverse all intermediate nodes again

        # let say our tree look like this
        # 1<-2<-6<-3<-4-<-5
        # search for 3
        # then after search tree will look like this
        #   ------->1   < - 2
        #  |        ^
        #  |        |
        #  3<-4<-5  6
        # as you can notice parent for 3 is directly now 1 instead of 2,
        # and it optimized search for 4 and 5 as well as they are now closer to 1.
        # and 6 is also pointing to 1 now, so 6 is also optimized.

        if node == self.parent[node]:
            return node
        else:
            # we will recursively find this relationship representative.
            self.parent[node] = self.path_compression_search(self.parent[node])
            return self.parent[node]


    # after using these 2 path compression for find and rank union for union
    # our time complexity will become some constant value. (proof is complex so we are skipping proof part)


d = DisJoinSet([1,2,4,5,6,7,8,9])
# note: we pass indicies instead of values
d.rank_union(2,3)
d.rank_union(5,1)
d.rank_union(1,7)
print(d.path_compression_search(7))

