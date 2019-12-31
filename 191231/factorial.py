# Recursion vs Iteration
# Loop : Iteration
# "To iterate is human, to recurse is divine"
# Function returning itself : Recursion
# Funcion calling / using itself within its scope : Recursion


def factorial(n) :
    if n == 1 :
        return 1
    return n * factorial(n-1)

print(factorial(5))
