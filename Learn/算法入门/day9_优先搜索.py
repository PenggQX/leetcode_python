from collections import deque
import copy


# L542 01矩阵  多源广度搜索
def updateMatrix(mat: list) -> list:
    iMax_X, iMax_Y = len(mat), len(mat[0])
    lChange = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = deque()
    res = [[10001] * iMax_Y for _ in range(iMax_Y)]
    for x in range(iMax_X):
        for y in range(iMax_Y):
            if mat[x][y] == 0:
                res[x][y] = 0
                stack.append((x, y))

    while stack:
        x, y = stack.popleft()
        iStep = res[x][y] + 1
        for ix, iy in lChange:
            x1, y1 = x + ix, y + iy
            if x1 < 0 or x1 >= iMax_X:
                continue
            if y1 < 0 or y1 >= iMax_Y:
                continue
            if iStep < res[x1][y1]:
                res[x1][y1] = iStep
                stack.append((x1, y1))

    return res


# L994 腐烂的橘子
def orangesRotting(grid: list) -> int:
    # 0: 空格子, 1: 好橘子 2: 烂橘子
    iMax_X, iMax_Y = len(grid), len(grid[0])
    lChange = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack0 = deque()    # 1个stack代表1min
    stack1 = deque()
    stack = stack0
    stack_other = stack1
    iMin = 0
    iGood = 0
    for x in range(iMax_X):
        for y in range(iMax_Y):
            if grid[x][y] == 1:
                iGood += 1
            elif grid[x][y] == 2:
                stack.append((x, y))
    if iGood == 0:
        return 0

    while stack0 or stack1:
        while stack:
            x, y = stack.popleft()
            for ix, iy in lChange:
                x1, y1 = x + ix, y + iy
                if x1 < 0 or x1 >= iMax_X:
                    continue
                if y1 < 0 or y1 >= iMax_Y:
                    continue
                if grid[x1][y1] == 1:
                    iGood -= 1
                    grid[x1][y1] = 2
                    stack_other.append((x1, y1))
        iMin += 1
        stack, stack_other = stack_other, stack
        if iGood == 0:
            return iMin
    return -1



if __name__ == '__main__':
    print(updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(orangesRotting([[0, 2]]))

