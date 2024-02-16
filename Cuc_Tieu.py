from Node import Node, Path

def Cuc_Tieu(DAU, Tap_DICH):
    MO = [[DAU,0]]
    DONG = []
    while MO:
        S = MO.pop(0)
        DONG.append(S)
        if S[0] in Tap_DICH:
            dong = [neighbor[0] for neighbor in DONG]
            data =Path(dong, S[0])
            for x in data:
                print(x.name)
            return "Thanh cong"
        for child in S[0].get_neighbors_with_weight():
            if child not in MO and child not in DONG:
                child[1]+=S[1]
                MO.insert(0,child)
        #MO.sort()
        MO.sort(key=lambda x: x[1])
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
A.add_neighbor(B,1)
A.add_neighbor(C,3)
A.add_neighbor(D,6)
C.add_neighbor(G,2)
C.add_neighbor(F,5)
D.add_neighbor(H,1)
D.add_neighbor(I,7)

print(Cuc_Tieu(A,[H,F]))
