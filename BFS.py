from Node import Node, Path

def BFS(DAU, DICH):
    MO = [DAU]
    DONG = []
    while MO:
        S = MO.pop(0)
        DONG.append(S)
        if S == DICH:
            data = Path(DONG, DICH)
            for x in data:
                print(x.name)
            return "Thanh cong"
        for child in S.get_neighbors():
            if child not in MO and child not in DONG:
                MO.append(child)
    return "Khong thanh cong"

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
A.add_neighbor(B)
A.add_neighbor(C)
A.add_neighbor(D)
B.add_neighbor(E)
C.add_neighbor(E)
C.add_neighbor(F)
D.add_neighbor(F)
F.add_neighbor(G)
G.add_neighbor(H)
print(BFS(A,H))
