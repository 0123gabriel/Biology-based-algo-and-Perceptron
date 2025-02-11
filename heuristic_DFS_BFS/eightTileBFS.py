import copy
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue
from bigtree import Node

def possiblePositions(currentPos):
    x = 0
    y = 0
    pp = []
    for i in range(0,3):
        for j in range(0,3):
            if currentPos[i][j] == 0:
                x = i
                y = j

    if x-1 >= 0:
        pos1 = copy.deepcopy(currentPos)
        pos1[x][y], pos1[x-1][y] = pos1[x-1][y], pos1[x][y]
        pp.append(pos1)

    if x+1 <= 2:
        pos2 = copy.deepcopy(currentPos)
        pos2[x][y], pos2[x+1][y] = pos2[x+1][y], pos2[x][y]
        pp.append(pos2)

    if y-1 >=0:
        pos3 = copy.deepcopy(currentPos)
        pos3[x][y], pos3[x][y-1] = pos3[x][y-1], pos3[x][y]
        pp.append(pos3)

    if y+1 <= 2:
        pos4 = copy.deepcopy(currentPos)
        pos4[x][y], pos4[x][y+1] = pos4[x][y+1], pos4[x][y]
        pp.append(pos4)

    return pp


if __name__ == "__main__":
    initialState = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    print()
    print("Path para llegar a la solucion")
    print()

    for row in initialState:
        print(row)
    print()

    G = nx.Graph()
    visited = set()
    queue = Queue()
    qCopy = Queue()
    queue.put((initialState, []))
    qCopy.put((initialState, []))
    l = []
    i = 0

    while not queue.empty():
        currentState, path = queue.get()
        visited.add(tuple(map(tuple, currentState)))

        if i == 0:
            root = Node(currentState)
            i = i + 1

        if currentState == goalState:
            G.add_edge(tuple(map(tuple,currentState)), tuple(map(tuple, position)))
            for state in path:
                for row in state:
                    print(row)
                print()
            break

        positions = possiblePositions(currentState)
        for position in positions:
            if tuple(map(tuple, position)) not in visited:
                newPath = path.copy()
                newPath.append(position)
                queue.put((position, newPath))
                qCopy.put((position, newPath))

                while not qCopy.empty():
                    cs,p = qCopy.get()
                    l.append(cs)
                    if goalState not in l:
                        G.add_edge(tuple(map(tuple,currentState)), tuple(map(tuple, position)))

    else:
        print("No hay solucion")

    print("Estados visitados: " + str(len(visited)))

    nx.draw_spring(G, with_labels=True)
    plt.savefig("BFS.png")



    

            

