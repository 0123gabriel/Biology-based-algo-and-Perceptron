import copy
import networkx as nx
import matplotlib.pyplot as plt
import heapq

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

def heuristic(state, goalState):
    wellLocTiles = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == goalState[i][j]:
                wellLocTiles = wellLocTiles + 1
    return (9 - wellLocTiles)

def bestFS(initialState, goalState, G):
    visited = set()
    priorityQueue = [(heuristic(initialState, goalState), initialState, [initialState])]

    while priorityQueue:
        h, currentState, path = heapq.heappop(priorityQueue)
        visited.add(tuple(map(tuple, currentState)))

        if goalState == currentState:
            return path, visited
        

        positions = possiblePositions(currentState)
        for position in positions:
            if tuple(map(tuple, position)) not in visited:
                newPath = path + [position]
                heapq.heappush(priorityQueue, (heuristic(position, goalState), position, newPath))
                G.add_edge(tuple(map(tuple,currentState)), tuple(map(tuple, position)))

    return None


if __name__ == "__main__":

    initialState = [[1, 2, 3], [0, 4, 6], [7, 5, 8]]
    
    goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    G = nx.Graph()

    resultPath, visited = bestFS(initialState, goalState, G)

    print()
    print("Path para llegar a la solucion")
    print()
    for state in resultPath:
        for row in state:
            print(row)
        print()

    print("Estados visitados: " + str(len(visited)))

    nx.draw_spring(G, with_labels=True)
    plt.savefig("BestFSNumBaldosas.png")

    

    
