def HanoiCount(n):
    # return 2 ** n -1
    if(n==1):
        return 1
    return 2 * HanoiCount(n-1) + 1

print(HanoiCount(10))
