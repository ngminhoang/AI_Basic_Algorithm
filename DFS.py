from Node import Node, Path

def DFS(DAU, DICH):
    MO = [DAU]
    DONG = []
    while MO:
        S = MO.pop(0)
        DONG.append(S)
        if S == DICH:
            data =Path(DONG, DICH)
            for x in data:
                print(x.name)
            return "Thanh cong"
        for child in S.get_neighbors():
            if child not in MO and child not in DONG:
                MO.insert(0,child)
    return "Khong thanh cong"


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
A.add_neighbor(B)
A.add_neighbor(C)
A.add_neighbor(D)
B.add_neighbor(E)
B.add_neighbor(F)
B.add_neighbor(G)
C.add_neighbor(G)
G.add_neighbor(H)
H.add_neighbor(I)

print(DFS(A,H))
