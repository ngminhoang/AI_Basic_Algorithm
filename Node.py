class Node:
    def __init__(self, name):
        self.deep = 0
        self.name = name
        self.neighbors = []

    def add_neighbor(self, neighbor, weight=1):
        neighbor.deep = self.deep + 1
        self.neighbors.insert(0,[neighbor, weight])

    def get_neighbors(self):
        # Trả về danh sách các hàng xóm
        return [neighbor[0] for neighbor in self.neighbors]
    
    def get_neighbors_with_weight(self):
        # Trả về danh sách các hàng xóm
        return self.neighbors

    def get_weight(self, neighbor):
        for n, weight in self.neighbors:
            if n == neighbor:
                return weight
        return None

def Path(nodes, DICH):
    path = [DICH]
    point = DICH
    while point != nodes[0]:
        for node in nodes:
            if point in node.get_neighbors():
                path.append(node)
                point = node
                break
    return path[::-1]