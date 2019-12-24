start = 2
print(start)
limit = 100

while start <= limit:
    divider = 2
    while divider < start:
        print(str(start)+" divided by " + str(divider))
        if (start % divider == 0) :
            break
        elif (divider == start - 1):
            print("Tada ! " + str(start) + " is a Prime Number.")
        divider += 1
    start += 1
