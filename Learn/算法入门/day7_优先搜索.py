from collections import deque

# L733 图像渲染
def floodFill(image: list, sr: int, sc: int, newColor: int) -> list:
    # 1 1 1
    # 1 1 0
    # 1 0 1

    lRs = deque([(sr, sc)])
    iOldColor = image[sr][sc]
    lChange = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if iOldColor == newColor:
        return image
    while lRs:
        x, y = lRs.popleft() # 优化，不符合条件不要放进去
        if x < 0 or x >= len(image):
            continue
        if y < 0 or y >= len(image[0]):
            continue
        if image[x][y] != iOldColor:
            continue
        image[x][y] = newColor
        for ix, iy in lChange:
            lRs.append((x + ix, y + iy))
    return image


# L695 岛屿的最大面积
def maxAreaOfIsland(grid: list) -> int:
    lChange = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    iMaxX, iMaxY = len(grid), len(grid[0])
    def search(x, y):
        if grid[x][y] != 1:
            return 0
        stack = deque([(x, y)])
        iArea = 1
        while stack:
            x, y = stack.popleft()
            grid[x][y] = 0
            for ix, iy in lChange:
                x1, y1 = x + ix, y + iy
                if x1 < 0 or x1 >= iMaxX:
                    continue
                if y1 < 0 or y1 >= iMaxY:
                    continue
                if not grid[x1][y1]:
                    continue
                iArea += 1
                stack.append((x1, y1))
        return iArea
    iRes = 0
    for x in range(0, iMaxX):
        for y in range(0, iMaxY):
            iRes = max(iRes, search(x, y))
    return iRes


if __name__ == '__main__':
    print(floodFill( [[0, 0, 0],[0, 1, 1]], 1, 1, 1))
    print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))