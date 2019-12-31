# 1 1 2 3 5 8 13 21

# limit = 50000
# first = 1
# second = 1
#
# print(first)
# print(second)
#
# while second <= limit:
#     temp = second
#     second = first + second
#     first = temp
#     print(second)

def fiboIteration(n):
    first = 1
    second = 1

    print(first)
    print(second)
    count = 2

    while count < n :
        temp = second
        second = first + second
        first = temp
        print(second)
        count = count  + 1

fiboIteration(10)

def fiboRecursion(first, second, n, count = 1):
    if( count == 2 ):
        print(first)
        print(second)
    elif (count >= n) :
        return second
    else:
        print(second)
    return fiboRecursion(second, first + second, n, count + 1)


fiboRecursion(1,1, 10)
