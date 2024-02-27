
#=========Recursion is the concept when a function calls itself==========#

#=========Components of recursion==============*
#:Base case , #:Recursive relation , #:Processing

#:===When recursive relation is at the end , that recursion is called tail recursion and when recursive relation comes before processing it is called head recursion===.

#----Q:----Write a program to calculate factorial of a number n-------

# def factorial(n):
#     if n == 0:
#         return 1
#     ans = n * factorial(n - 1)

#     return ans


# print(factorial(5))#:Output:120
# print(factorial(6))#:Output:720

#----Q:----Write a program to calculate 2 power of n-------

# def powerof2(n):

#     if n == 0:
#         return 1
    
#     smallerProblem = powerof2(n - 1)
#     ans = 2 * smallerProblem

#     return ans


# print(powerof2(10))#Output:1024


#-----Q:-------Write a program to write reverse counting from n to 1-----.

# def reverseCounting(n):
#     if n == 0:
#         return
#     print(n , end = " ")
#     reverseCounting(n - 1)

# reverseCounting(10)#Output:10 9 8 7 6 5 4 3 2 1     

#-----Q:-------Write a program to give nth fibonnaci number----------.

# def nthFibonacciNumber(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     ans = nthFibonacciNumber(n - 2) + nthFibonacciNumber(n - 1)
#     return ans

# print(nthFibonacciNumber(9))#:Output:21
# print(nthFibonacciNumber(10))#:Output:34






