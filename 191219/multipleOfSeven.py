# x = 500000
# while x < 2000001:
#     x += 1
#     if x%199 == 0:
#         print(x)

# x = 199
# while x < 399:
#     if x%199 == 0:
#         print(x)
#     x += 1

# x = 2000000
# while x < 2000199:
#     if x%199 == 0:
#         print(x)
#     x += 1

start = 2000000
answer = 0
divider = 38976

while answer == 0:
    if start % divider == 0:
        answer = start
        print(answer)
    x += 1
