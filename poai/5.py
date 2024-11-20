class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list[node]

    def heuristic(self, node):
        # Static heuristic values for nodes
        heuristic_values = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return heuristic_values[node]

    def a_star(self, start, goal):
        # Open list to store nodes to explore
        open_list = set([start])
        # Closed list to store explored nodes
        closed_list = set()

        # Costs to reach each node
        g_cost = {start: 0}
        # Parents to reconstruct the path
        parents = {start: None}

        while open_list:
            # Find the node in the open list with the lowest f-cost
            current_node = min(open_list, key=lambda node: g_cost[node] + self.heuristic(node))

            # If the goal is reached, reconstruct and return the path
            if current_node == goal:
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = parents[current_node]
                path.reverse()
                print(f"Path found: {path}")
                return path

            # Move current node from open to closed list
            open_list.remove(current_node)
            closed_list.add(current_node)

            # Explore neighbors
            for neighbor, weight in self.get_neighbors(current_node):
                if neighbor in closed_list:
                    continue

                # Calculate tentative g-cost for the neighbor
                tentative_g_cost = g_cost[current_node] + weight

                # If neighbor is not in open_list or has a better g-cost
                if neighbor not in open_list or tentative_g_cost < g_cost.get(neighbor, float('inf')):
                    g_cost[neighbor] = tentative_g_cost
                    parents[neighbor] = current_node
                    open_list.add(neighbor)

        print("Path does not exist!")
        return None


# Example graph
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}

graph = Graph(adjacency_list)
graph.a_star('A', 'D')
