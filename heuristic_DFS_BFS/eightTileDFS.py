import copy
import networkx as nx
import matplotlib.pyplot as plt
from queue import Queue

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

def DFS(currentState, path, visited, goalState):
    visited.add(tuple(map(tuple, currentState)))

    if goalState == currentState:
        return path
    
    positions = possiblePositions(currentState)
    for position in positions:
        if tuple(map(tuple, position)) not in visited:
            newPath = path.copy()
            newPath.append(position)
            G.add_edge(tuple(map(tuple, currentState)), tuple(map(tuple, position)))
            nextIteration = DFS(position, newPath, visited, goalState)
            if nextIteration is not None:
                return nextIteration
            
    return None

if __name__ == "__main__":
    initialState = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    
    goalState = [[2, 4, 3], [1, 0, 6], [7, 5, 8]]
    
    G = nx.Graph()
    visited = set()
    path = [initialState]

    resultPath = DFS(initialState, path, visited, goalState)

    print()
    print("Path para llegar a la solucion")
    print()

    if resultPath is not None:
        for state in resultPath:
            for row in state:
                print(row)
            print()

    print("Estados visitados: " + str(len(visited)))

    nx.draw_spring(G, with_labels=True)
    plt.savefig("DFS.png")


    

            

