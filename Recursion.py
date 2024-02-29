
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



#-----Q:-------------Important leetcode problems---------------------

#---Q:There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top.

# def countWays(n):
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     ans = countWays(n - 1) + countWays(n - 2)
#     return ans

# print(countWays(4))#:Output:5


#----Q:------Write a function sayDigit which takes an integer n and print its english  dsecription.e.g 412 : "four one two"

# def sayDigit(number):
#     mapArray = ["one" , "two" , "three" , "four" , "five" , "six" , "seven" , "eight" , "nine"]
#     if number == 0:
#         return
    
#     digit = number % 10
#     number = (int)(number / 10)
#     sayDigit(number)
#     print(mapArray[digit - 1] , end = " ")


# sayDigit(429)    











