def isValidPosition(rowIndex, colIndex, solution):
    for r in range(rowIndex):
        if colIndex == solution[r]:
            return False
        elif abs(colIndex-solution[r]) == abs(rowIndex - r):
            return False
    return True

def placeQueen(rowIndex, solution, n):
    if rowIndex == n:
        print(solution)
        return 1
    else:
        totalSol = 0
        for colIndex in range(n):
            if isValidPosition(rowIndex, colIndex, solution):
                solution[rowIndex] = colIndex
                totalSol = totalSol + placeQueen(rowIndex+1, solution, n)
        return totalSol

if __name__ == "__main__":
    n = 11
    solution = ['']*n
    rowIndex = 0
    print(placeQueen(rowIndex, solution, n))