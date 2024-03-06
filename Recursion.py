
#=========Recursion is the concept when a function calls itself==========#

#=========Components of recursion==============*
#:Base case , #:Recursive relation , #:Processing

#:===When recursive relation is at the end , that recursion is called tail recursion and when recursive relation comes before processing it is called head recursion===.

#----Q:----Write a program to calculate factorial of a number n-------

def factorial(n):
    if n == 0:
        return 1
    
    ans = n * factorial(n - 1)
    return ans

print(factorial(5))
print(factorial(6))

    












