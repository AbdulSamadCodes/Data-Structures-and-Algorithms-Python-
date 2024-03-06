
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

# print(factorial(5))#Output:120
# print(factorial(6))#Output:720

#---Q:----Given an integer N, recursively sum digits of N until we get a single digit----

# def repeatedSumOfDigits (N):
#     if N < 10:
#         return N
        
#     sum = 0
#     while N > 0:
#         remainder = (int)(N % 10)
#         sum+=remainder
#         N = (int)(N / 10)
#     return repeatedSumOfDigits(sum)

# result = repeatedSumOfDigits(456)
# print(result)#Output:6


#---Q:----Given an integer n and x, find n to the power of x using recursion----

# def calcPower(n , x):
#     if x == 0:
#        return 1

#     ans = n * calcPower(n , x - 1)
#     return ans

# print(calcPower(8 , 2))#Output:64 
# print(calcPower(2 , 10))#Output:1024


#---Q:----Given an integer n and x, find n to the power of x using recursion (stackheight = O(logn)))---

# def calcPowerLogn(n , x):
#     if x == 0:
#         return 1
    
#     else:
#         if (x % 2 != 0):
#             return calcPowerLogn(n , x // 2 ) * calcPowerLogn(n , x // 2) *  n
#         else:
#             return calcPowerLogn(n , x // 2 ) * calcPowerLogn(n , x // 2) 
        
 
# print(calcPowerLogn(8 , 2))#Output:64 
# print(calcPowerLogn(2 , 10))#Output:1024       

#---Q:----Write to function which prints integers n to 1-------

# def reversePrinting(n):
#     if n == 0:
#         return
    
#     print(n)
#     reversePrinting(n - 1)

# reversePrinting(5)

#--Q:Suppose you are at a point a and you want to go to point b.Write a function which prints your steps which you took to reach at point b from a---.

# def reachDestination(a , b):
#     if (a == b):
#         print("I reached at  point:" , a)
#         return 
    
#     print("I reached at  point:" , a)
#     return reachDestination(a + 1 , b)

# reachDestination(1, 10)


#---------------Important leetcode  question-----------------

#---Q:You are benn given a number of stairs.Initially you are at 0th stair and you have to reach nth stair.You can wither climb one stair ot two stair at a time.Return the number of distinct ways you can climb stairs.

# def climbStairs(n):
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1

#     ans = climbStairs(n - 1) + climbStairs(n - 2)
#     return ans

# print(climbStairs(5)) 
# print(climbStairs(2))

#---Q:--Write a function to print nth fibonnaci number(0 based indexing)-----------

# def fibonnaci(n):
#    if n == 0:
#       return 0
#    if n == 1:
#       return 1
#    ans = fibonnaci(n - 1) + fibonnaci(n - 2)
#    return ans

# print(fibonnaci(8))#Output:21


#------------leetcode  question------------

#Q:-------Write a  function which given an integer  n say its digits in english description.for e.g 243 "two four three"----

# mapArray = ["one" , "two" , "three", "four" , "five" , "six" , "seven" , "eight" , "nine"]

# def sayDigit(n):
#     if n < 10:
#         print(mapArray[n - 1])
#         return 
    
#     rem = n % 10
#     n = n // 10

#     sayDigit(n)
#     print(mapArray[rem - 1]) 


# sayDigit(243)    
# sayDigit(967)

       





    














