def FindNumber(arr):
    if not arr:
        return -1
    iMaxCol, iMaxRow = len(arr), len(arr[0])
    iCol, iRow = 0, iMaxRow - 1
    while iCol < iMaxCol and iRow >= 0:
        pass