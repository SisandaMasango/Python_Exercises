from collections import defaultdict, deque

class Graph:
    def __init__(self):
        # adjacency list where each key is a host and value is a set of connected hosts
        self.graph = defaultdict(set)

    def add_edge(self, a, b):
        """Add an undirected edge between hosts a and b."""
        self.graph[a].add(b)
        self.graph[b].add(a)  # undirected means both ways

    def has_path(self, start, end):
        """Check if a path exists between start and end using BFS."""
        if start == end:
            return True

        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current == end:
                return True
            if current not in visited:
                visited.add(current)
                queue.extend(self.graph[current] - visited)

        return False


# --- Example usage ---
if __name__ == "__main__":
    g = Graph()
    g.add_edge("Host1", "Host2")
    g.add_edge("Host2", "Host3")
    g.add_edge("Host3", "Host4")

    print(g.has_path("Host1", "Host4"))  # True
    print(g.has_path("Host1", "Host5"))  # False
