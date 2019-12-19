def rangeMultiple(lowRange, highRange, divider):
    x = lowRange
    while x < highRange + 1:
        if x % divider == 0:
            print(x)
        x += 1
    # return x

rangeMultiple(3, 9, 3)
# print(     )
#
# def leastMultiple(start, answer, divider):





# def factorial (number):
#     if number > 0:
#         result = number * factorial(number - 1)
#     else : result = 1
#     return result
#
# print ( factorial (    int(input("Type in a number : "))    ) )

# def plus (plus1, plus2):
#     # print(plus1 + plus2)
#     plus1 -= 3
#     x = plus1 + plus2
#     return x
#     # return(plus1 + plus2)
#     # print("sdgfhdsa")
#
# print ( plus (5,3) )
#
# print(plus(plus(5, 3),8))
