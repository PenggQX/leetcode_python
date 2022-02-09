# 专项练习

if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 3]
    b = set()
    for i in a:
        if i in b:
            print(i)
        b.add(i)

