# 组合总和

# 递归 + 备忘录

# 对于这类寻找所有可行解的题，我们都可以尝试用「搜索回溯」的方法来解决。

# 优化

# 1. 可不可以在搜索的时候就去重呢？答案是可以的。遇到这一类相同元素不计算顺序的问题，我们在搜索的时候就需要 按某种顺序搜索。
# 具体的做法是：每一次搜索的时候设置 下一轮搜索的起点 begin，请看下图。

# 2. 减枝 通过排序，提速。


def combinationSum(candidates, target):
    """
    回溯算法 + 剪枝
    :param candidates:
    :param target:
    :return:
    """
    book = {}   # target: res

    def filterList(lRes):
        lResult = []
        for l in lRes:
            l.sort()
            if l not in lResult:
                lResult.append(l)
        return lResult

    def trueCombination(iTarget):
        if iTarget in book:
            return book[iTarget]
        lRes = []
        for i in candidates:
            iSub = iTarget - i
            if iSub < 0:
                continue
            if iSub == 0:
                lRes.append([i])
                continue
            lRes1 = trueCombination(iSub)
            if not lRes1:
                continue
            for res in lRes1:
                res = list(res)
                res.append(i)
                lRes.append(res)
        book[iTarget] = filterList(lRes)
        return book[iTarget]

    return trueCombination(target)


if __name__ == '__main__':
    print(combinationSum([2, 3, 5, 6, 7], 8))
    print(combinationSum([2], 2))