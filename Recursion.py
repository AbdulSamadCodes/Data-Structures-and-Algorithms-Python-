
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


#-----Q:-------Write a program which gives the sum of natural numbers from 1 to n.----

# def sumOfNaturalNumbers(n , sum):
#     if n == 0:
#         print(sum)
#         return
    
#     sum+=n
#     sumOfNaturalNumbers(n - 1 , sum)

# sumOfNaturalNumbers(6 , 0)#:Output:21


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

#-----Q:-------Write a program to print fibonnaci series till nth term----------.

# def printFibonacci(n , a , b):
#     if n == 0:
#         return
#     c = a + b
#     print(c )
#     printFibonacci(n - 1 , b , c)

# a = 0
# b = 1
# print(a)
# print(b)
# n = 7
# printFibonacci(n - 2 , a , b)








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


#----Q:------Write a function using recursion which tells whether the array  s sorted or not.You will be given the length of array as n.

# def  isSorted(arr , n):
#     count = 0
#     count+=1
#     if (n == 0 or n == 1):
#         return True
#     if (arr[0] > arr[1]):
#         return False
#     else:
#         ans = isSorted(arr[count:] , n - 1)
#         return ans
    
    
# array = [1, 4 ,5 ,9 ,9]
# size = len(array)

# array2 = [23,56,34,3200]
# size2 = len(array2)

# print(isSorted(array , size))#Output:True
# print(isSorted(array2 , size2))#Output:False


#----Q:------Write a program using recursion to find sum of an array------------.

# def sumOfArray(arr , n):
#   if n == 0:
#     return 0
#   if n == 1:
#     return arr[0]
  
#   count = 0
#   count+=1

#   remaining =  sumOfArray(arr[count:] , n -1)
#   sum = arr[0] + remaining
#   return sum

# array = [1, 4 ,5 ,9 ,9]
# size = len(array)
# print(sumOfArray(array , size))#Output:28


#----Q:------Write a program using recursion to find x to the power of n(stack height == n)------------.

# def calcpower(x , n):
#     if n == 0:
#         return 1
#     if x == 0:
#         return 0
    
#     ans = x * calcpower(x , n - 1)
#     return ans

# base = 8
# power  = 3
# print(calcpower(base , power))


#----Q:------Write a program using recursion to find x to the power of n(stack height == log(n))------------.

# def calcPowerLogn(x , n):
#     if n == 0:
#         return 1
#     if x == 0:
#         return 0
    
#     if (n % 2 == 0):
#         return calcPowerLogn(x , (int)(n / 2)) * calcPowerLogn(x , (int)(n / 2))
#     else:
#         return calcPowerLogn(x , (int)(n / 2)) * calcPowerLogn(x , (int)(n / 2)) * x
    

# base = 16
# power = 3
# print(calcPowerLogn(base , power))#Output:4096









  











