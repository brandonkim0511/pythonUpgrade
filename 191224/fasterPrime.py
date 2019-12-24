##############################
# Backward Prime
# start = 2
# print(start)
#
# while start <= 50000:
#     divider = start - 1
#     while divider > 1:
#         # print(str(start)+" divided by " + str(divider))
#         if (start % divider == 0) :
#             break
#         elif (divider == 2):
#             print("Tada ! " + str(start) + " is a Prime Number.")
#         divider -= 1
#     start += 1

# Takes 232.17 sec

######################


# Forward Prime

# start = 2
# print(start)
# limit = 50000
#
# while start <= limit:
#     divider = 2
#     while divider < start:
#         if (start % divider == 0) :
#             break
#         elif (divider == start - 1):
#             print("Tada ! " + str(start) + " is a Prime Number.")
#         divider += 1
#     start += 1
#
# # Takes 43.82 sec

########################################

# Prime Only

start = 2
print(start)
primeList = [2]
limit = 50000

while start <= limit:
    for divider in primeList:
        if (start % divider == 0):
            break
        elif (divider == primeList[len(primeList) - 1]):
            print("Tada ! " + str(start) + " is a Prime Number.")
            primeList.append(start)
    start += 1

# # Takes 7.33 sec
