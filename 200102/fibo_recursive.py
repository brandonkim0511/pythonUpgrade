import time

def fibo_recursive(n):
    if (n == 1 or n == 2):
        return 1
    return fibo_recursive(n-1) + fibo_recursive(n-2)

# for i in range(100):
#     print ( fibo_recursive(i+1) )

def fibo_iterative(n):
    first = 1
    second = 1
    count = 0
    while(count != n-2):
        if (n == 1 or n == 2):
            return 1
        else :
            temp = second
            second = first + second
            first = temp
            count = count + 1
    return second


# start = int(round(time.time() * 1000)) # expresses time in millisecond
#
# for i in range(35):
#     print(fibo_recursive(i+1))
#
# print(int(round(time.time() * 1000)) - start )


print("#######################")

start = int(round(time.time() * 1000)) # expresses time in millisecond

for i in range(35000):
    print(fibo_iterative(i+1))

print(int(round(time.time() * 1000)) - start )
