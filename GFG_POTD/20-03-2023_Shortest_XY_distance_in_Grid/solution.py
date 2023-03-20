# User function Template for python3

from collections import deque


class Node:
    def __init__(self, value, coord_i, coord_j):
        self.value = value
        self.signature = str(coord_i) + "-" + str(coord_j)
        self.neighbors = []

    def add_neighbor(self, node_signature):
        self.neighbors.append(node_signature)


class Graph:
    def __init__(self):
        self.nodes = {}

    def add(self, node):
        self.nodes[node.signature] = node


class Solution_BFS:
    def shortestXYDist(self, grid, N, M):
        # print("Grid: ", grid)
        # code here
        # 1. Transform the grid to a Graph structure
        def make_graph(grid):

            G = Graph()

            # Create nodes
            for i in range(N):
                for j in range(M):
                    node = Node(value=grid[i][j], coord_i=i, coord_j=j)
                    for neigh_coord in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        x, y = neigh_coord[0], neigh_coord[1]
                        if ((x < N) and (x >= 0)) and ((y < M) and (y >= 0)):
                            node_signature = str(x) + "-" + str(y)
                            node.add_neighbor(node_signature=node_signature)
                    G.add(node=node)

            return G

        G = make_graph(grid=grid)

        # 2. Do BFS to find nearest Y neighbor in the graph and return the distance
        def find_nearest_y(node, graph, global_minimum):
            visited = set()
            closest_intermediate_X = None

            if global_minimum:
                min_distance = global_minimum
            else:
                min_distance = N + M
            queue = deque()
            for sig in node.neighbors:
                queue.append((sig, 1))

            while queue:
                current_node_sig, current_node_dist = queue.popleft()
                current_node = graph.nodes[current_node_sig]

                visited.add(current_node_sig)

                if current_node.value == 'X':
                    closest_intermediate_X = current_node_dist

                if current_node.value == 'Y':
                    if current_node_dist < min_distance:
                        min_distance = current_node_dist
                    break
                else:
                    for sig in current_node.neighbors:
                        if (sig not in visited) and (current_node_dist + 1 < min_distance):
                            queue.append((sig, current_node_dist + 1))

            if closest_intermediate_X:
                max_dist_for_closest_intermediate_X = min_distance - closest_intermediate_X + 2
                return min([min_distance, max_dist_for_closest_intermediate_X])
            else:
                return min_distance

        # 3. Do this for all cells with an X value
        global_minimum = None
        distances = []
        for _, node in G.nodes.items():
            if node.value == 'X':
                # print("node with X: ", node.signature)

                distance = find_nearest_y(node=node, graph=G, global_minimum=global_minimum)

                if not global_minimum:
                    global_minimum = distance
                elif global_minimum and distance < global_minimum:
                    global_minimum = distance

                if global_minimum == 1:
                    return global_minimum

        return global_minimum


class Solution:
    def shortestXYDist(self, grid, N, M):
        # 1. Find all positions with 'X' value
        x_positions = set()
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 'X':
                    x_positions.add((i, j))

        # 2. Do BFS from each 'X' position to find nearest 'Y' position
        min_distance = float('inf')
        for x in x_positions:
            visited = {x}  # set
            queue = [(x, 0)]
            while queue:
                (i, j), distance = queue.pop(0)
                if grid[i][j] == 'Y':
                    min_distance = min(min_distance, distance)
                    break
                for (ni, nj) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
                        visited.add((ni, nj))
                        queue.append(((ni, nj), distance + 1))

        return min_distance if min_distance != float('inf') else -1


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = map(int, input().split())
        grid = []
        for i in range(N):
            ch = list(map(str, input().split()))
            grid.append(ch)

        ob = Solution()
        print(ob.shortestXYDist(grid, N, M))
# } Driver Code Ends
