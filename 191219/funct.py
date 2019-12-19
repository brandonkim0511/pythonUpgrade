def rangeMultiple(lowRange, highRange, divider):
    x = lowRange
    while x < highRange + 1:
        if x % divider == 0:
            print(x)
        x += 1
    return x

print(rangeMultiple(21, 49, 7))

def leastMultiple(start, answer, divider):





# def factorial (number):
#     if number > 0:
#         result = number * factorial(number - 1)
#     else : result = 1
#     return result
#
# print ( factorial (    int(input("Type in a number : "))    ) )
