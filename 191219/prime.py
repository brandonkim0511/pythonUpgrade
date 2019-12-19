
# def primeFunction():

start = 2

while start <= 100:
    divider = start - 1
    while divider > 1:
        if (start % divider != 0) and (divider == 2):
            # break
            print(start)
        divider -= 1
    start += 1
