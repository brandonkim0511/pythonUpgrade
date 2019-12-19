
# def primeFunction():

start = 2

while start <= 100:
    divider = start - 1
    while divider > 1:
        if (start % divider != 0) and (divider == 3):
            print(start)
        divider -= 1
    start += 1
