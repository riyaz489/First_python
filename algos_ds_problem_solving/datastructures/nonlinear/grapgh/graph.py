# in graph we have edges and vertices.
# there are multiple types of grapghs:
# 1. undirected graphs    : here we don't have direction in edges, if an adge exists between 2 potins then we can move
# in both directions.
#                       5
#                       |
#                       4
# we can go to 4 to 5 and 5 to 4

# 2.directed graphs: here edges have directions also, and we can move only in given direction.
#                   5
#                   ^
#                   |
#                   3
# we can only go 3 to 5, vice versa is not possible.

# 3.connected graph: a graph is connected. if we can traverse all the edges form any given points. i.e.,
# there is a path from any point to any other point in the graph

#                       4-1
#                       |
#                       2
# this is connected graph all vertices are reachable from any point.
# like we can go to 4 and 1 from 2 and , from 4 also we can go to 2 and 1, and from 1 we can go to 4 and 2.

# 4. disconnected graph: where we can not traverse all vertices from any point.
#                       4-1   2-3
# these 2 are disconnected graphs.

# 5. weighted graph: where edges have some weights.



## graph representation###
# well there we 2 ways to represent graphs, one is using (vertices x vertices) 2D matrix.
# but this is inefficient as it takes more space.
# another ways is to  use list inside dict. where key will be vertices and value_list will be adjacent connected
# vertices.
# so max possible edges will be =  combination(Vertices, 2). (if each vertices tries to connect with another vertices.)
# so each key in adj matrix will have v-1 lenght list. as each vertx is connected with another vertex in worst case.
# so space consumed in worst case will be v^2. as we have v keys.
# for below grapgh
#                       4-1
#                       |
#                       2
# adj dict will be like : {1: [4], 4:[1,2], 2:[4]}


class Grapgh:

    def __init__(self):
        # this will contains both vertices and their adjacent connected vertices.
        self.adj = {}

    def add_edge(self, v1, v2):
        # as we are doing undirected graph,we have to add connection both ways.
        # for directed graph we will not add both ways.
        # for weighted grapgh we will add tuple into list instead of just vertex name
        # it will be like {v1: [(v2, 4),(v3, 1) ]}

        # note: before adding vertex to current vertex adj list, we can check that vertex connection already exists
        # or not. if already exists then we can skip addition.
        if v1 not in self.adj:
            self.adj[v1] = [v2]
        else:
            self.adj[v1].append(v2)

        if v2 not in self.adj:
            self.adj[v2] = [v1]
        else:
            self.adj[v2].append(v1)

    def add_directed_edge(self, v1,v2):
        if v1 not in self.adj:
            self.adj[v1] = [v2]
        else:
            self.adj[v1].append(v2)
        if v2 not in self.adj:
            self.adj[v2] = []

    def remove_edge(self, v1, v2):
        # given edge do not exist
        if v1 not in self.adj:
            return
        if v2 not in self.adj:
            return

        self.adj[v1].remove(v2)
        self.adj[v2].remove(v1)

    def bfs(self):
        # in BFS we first traverse all adjacent vertices of current node, then we will traverse neighbours of those
        # adjacent vertices and so on.
        # for example:  5-3
        #               |
        #               1-2
        # if we start with 5 then we first print 5
        # then its adjacent nodes which is 3 and 1.
        # then 1s node adjacent which is 2.
        # so output will be -> 5,1,3,2

        # in case of cycles in graph we will end in looping same path infinitely, so that's why we used visited set.
        # so that we will not traverse same node again
        visited = set()
        number_of_connected_grapgh = 0
        for v in self.adj.keys():
            if v in visited:
                continue
            # in case graph is connected, this loop will only end when all the nodes are printed.
            # but in case of disconnected graph, few of the nodes might miss. that why we have running a for loop above
            # to make sure all the nodes are covered.
            number_of_connected_grapgh+=1 # this will tell us how many connected graphs are present. like for input
            # 1-2 6-8-5. we have 2 connected graphs.

            # here we like tree dfs we will use queue to store current nodes.
            queue = [v]
            while queue:
                item = queue.pop(0)
                if item not in visited:
                    print(item)
                    visited.add(item)
                    # adding its adjacent vertices to queue, so that it can be traversed first.
                    queue.extend(self.adj[item])
        print(f'\nnumber of connected graphs is {number_of_connected_grapgh}\n')

    def dfs(self):
        # in DFS we first pick one adjacent node go down in same path till we reached to end.
        # then we will pick another adjacent node and follow same approach.
        # for example:  5-3
        #               |
        #               1-2
        # so if we start with 5, and its first adjacent node we 1, then 1 will be printed, then we traverse first
        # adjacent node of 1 which is 2. now when we reached to end, then we will traverse 3.
        # as you can notice we are first traversing one path first, instead of moving in all direction like in BFS
        # where we first traversed all the adjacent nodes of current item.
        # so output will be -> 5,1,2,3

        # the problem with DFS is, let say if certain branch is infinitely long.
        # root -> v1 -> v2 -> v3 -> ... goes on forever
        # and we used dfs to find some vertex on grapgh, then we will never get our result.
        # but in case of BFS it is possible, as it does not traverse in one direction. so bfs is better to find elements

        # in case of cycles in graph we will end in looping same path infinitely, so that's why we used visited set.
        # so that we will not traverse same node again
        visited = set()
        number_of_connected_graph = 0


        def inner_dfs(node):
            if node in visited:
                return
            print(node)
            visited.add(node)
            for adj in self.adj[node]:
                # first it will traverse current ndoe first adj, then that adj node's first adjacent node and so on.
                # so it will complete one branch first, then others.
                inner_dfs(adj)


        # calling for loop for disconnected graph same like bfs for remaining keys
        for v in self.adj.keys():
            if v in visited:
                continue
            number_of_connected_graph += 1
            inner_dfs(v)
        print(f'\nnumber of connected graphs is {number_of_connected_graph}\n')

    def find_shortest_path_of_all_other_nodes_from_give_node_in_unweighted_graph(self, source):
        # idea is simple if we traverse in BFS way then we always get the shortest path.
        dis = {}
        # now instead of visited set we will use dis dict only, as if we found distance for some node, that means
        # it is traversed also.

        queue = [source]
        dis[source] = 0
        while queue:
            current_node = queue.pop(0)

            for adj_nodes in self.adj[current_node]:
                # adding distance, when we first encountered given node.
                if adj_nodes not in dis:
                    # adj nodes distance will be current node dis +1
                    dis[adj_nodes] = dis[current_node]+1
                    queue.append(adj_nodes)


        print(dis)

    def find_loop_in_undirected_graph(self):
        # To find loop in undirected graph, we can simply check visited, if we reached to same node again,
        # then it means there is a cycle.
        # but there is problem in above approach : 1-2 if we take this simple example
        # first 1 is traversed and added to visited list, then we will try to visit 2 and add 2 in visited array.
        # but as you can notice 1 is 2s adjacent node. so we will again go to 1. and our code will say we found cycle.
        # but in actual it is not cycle. To resolve this issue we have to keep track of parents nodes also.
        # so if its adjacent was parent then we will not consider it as loop.

        parent = {}

        for v in self.adj.keys(): # running loop to check for other disconnected graphs
            if v in parent:
                continue
            parent[v] = -1 # marking parent for starting node as -1
            queue = [v]

            while queue:
                current = queue.pop()

                for adj in self.adj[current]:
                    if adj in parent: # that means current node is already visited,
                        # we haven't created visited array, we are using parent dict only to do same

                        if parent[current] != adj:# checking if we are going back to parent node.
                            # if not then it means we came back to some other node which is already
                            # visited and which is not a parent of current node
                            #   1-2-3
                            #   |___|
                            # like 3 is current node and its adjacent is 2 and 1. both will exist in parent node.
                            # but so when we see 2, we will be fine as 3s parent is 2. but when we notice
                            # 3's adjacent is 1 which is not his parent and it is also already visited.
                            # that means we found loop.
                            return True
                    else:
                        parent[adj] = current
                        queue.append(adj)
        return False

    def find_loop_in_directed_graph(self):
        # cycle
        # here we have to find a back edge, which is pointing to a node which is already visited.
        # here can't simply use visisted or parent array to decide.
        # 0-> 1 <-2
        # as you can see there 2 disconnected graphs and here in first traversal
        # and 0 and 1 will be visisted and 1's parent will be 0 but next time when we reached to 1 from 2.
        # then our prev program will say loop detected which is not true.
        # So here we will use DFS traversal, as in DFS we traverse one complete branch. and during that branch traveral
        # if we reached to any visisted node again, then it means we found loop.
        # As in directed graph we will meet a given node only once, if we follow single current path,
        # if it is not cyclic.
        # and after successfully branch traversal
        # we will reset visited array. so that next time if we reached to same node from different branch, then our code
        # will not result as loop detected.

        def detect_loop_inner(root):
            if root in rec_stack:
                return True
            visited.add(root)
            rec_stack.add(root)
            for i in self.adj[root]:
                if i not in visited and detect_loop_inner(i):
                    return True
                elif i in rec_stack: # checking if current adj is repeating or not.
                    # as we skipped recursive call for same visited element, for this element checking manually.
                    # because result after this element we already know from rec calls.
                    return True
            # removing current node from recursion stack after all its branch traversals.
            rec_stack.remove(root)
            return False
        visited = set() # our code will run without visited set also, but to optimized the code we have added it.
        # to avoid already traversed paths
        rec_stack = set() # it will keep track of all the nodes visited in current branch
        for k in self.adj.keys():
            if k not in visited and detect_loop_inner(k):
                return True

        return False

    def topological_sort(self):
        # we run this only for DAG directed acyclic(no cycle) graphs.
        # here child nodes can not be printed before their parent nodes.
        #  basically dependent nodes will only be printed when their parent node is printed.
        #     2<-1->3
        # 2 or 3 will only printed after 1.

        # to solve this we will use in-degree concept.
        # in-degree(number of incoming edges) for a given node tells us, how many adjacent nodes coming towards current node.
        # for example for above case in-degree of 1 is 0, 2 is 1, and 3 is 1.
        # in-degree also tells us, number of nodes, current node depends on.

        # we will first calculate in-degree of all vertices.
        # we will only print items of in-degree 0.
        # when item is removed, we will decrease in-degree by 1, of items which depends on it(adjacent items).
        # then repeat above steps till all the items are removed from indegree dict.

        # If the count of visited nodes is not equal to the number of nodes in the graph, or there are still some
        # vertices remaining in in_degree dict then the
        # topological sort is not possible for the given graph. (this is another way to detect cycle in directed graph)

        # to calculate in-degree, we will simpy check, how many times a given item comes in adj_list of other items.
        in_degree = {}
        for i, adj_list in self.adj.items(): # time complexity of inner and outer loop combined
            # would be O(V+E) time
            for j in adj_list:
                if j in in_degree:
                    in_degree[j] += 1
                else:
                    in_degree[j] = 1
            # adding vertices if it is not added above. because if a vertices has 0 indegree, then it will never be
            # added in above loop.
            if i not in in_degree:
                in_degree[i] = 0

        queue = []
        # pushing initial items of indegree 0 into queue.
        for k,v in in_degree.items():
            if v ==0:
                queue.append(k)

        # now we will remove items from queue, decrease removed item adj nodes indegree and add new items of in-degree 0
        # into queue
        while queue:
            item = queue.pop(0)
            in_degree.pop(item)
            print(item)
            for ad in self.adj[item]:
                in_degree[ad] -= 1
                if in_degree[ad] == 0:
                    queue.append(ad)



g = Grapgh()
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

