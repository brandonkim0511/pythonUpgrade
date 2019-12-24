
# # def primeFunction():
# OLD code (notfunctioning)
# start = 2
#
# while start <= 100:
#     divider = start - 1
#     while divider > 1:
#         if (start % divider != 0) and (divider == 2):
#             # break
#             print(start)
#         divider -= 1
#     start += 1

# backward
start = 2
print(start)

while start <= 50000:
    divider = start - 1
    while divider > 1:
        # print(str(start)+" divided by " + str(divider))
        if (start % divider == 0):
            break
        elif (divider == 2):
            print("Tada ! " + str(start) + " is a Prime Number.")
        divider -= 1
    start += 1
