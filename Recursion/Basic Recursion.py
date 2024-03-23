
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

#----Write a function using recursion which tells  whether the array is sorted or not.You are given length of array as n---.

# def isSorted(arr , n):

#     if n == 0 or n == 1:
#         return True
    
#     if arr[n - 1] < arr[n -2]:
#         return False
    
#     return isSorted(arr , n - 1)

# array = [10 , 20 , 12 , 30 , 45]
# length = len(array)
# print(isSorted(array , length))#Output:False

# array2 =[1 , 4 , 5 ,78 , 78]
# length2 = len(array2)
# print(isSorted(array2 , length2))#Output:True

#----Write a function using recursion to  return the sum of the array----.

# def sumOfArray(array , n):
#     if n == 0:
#        return 0

#     return array[n - 1] + sumOfArray(array , n - 1) 
    
# array = [10 ,45 , 3 ,67]
# length = len(array)
# print(sumOfArray(array , length))#Output:125



#----Write a function using recursion to  perform linear search.The function should return the index of the target value.If it is not present then it should return -1----.

# def linearSearch(arr , n , k):
#     if n == 0:
#         return -1
    
#     if (arr[n - 1] == k):
#         return n - 1
    
#     return linearSearch(arr , n - 1 , k)


# array = [10 ,34 , 56 ,2 ,6]
# length = len(array)
# target_value = 34
# print(linearSearch(array , length , target_value))#Output:1

# array_2 = [45 , 6 , 79]
# length2 = len(array_2)
# target = 78
# print(linearSearch(array_2 , length2 , target))#Output:-1

#:-------Write a function which gives the minimum and maximum of input array in the result array

# def maxmin(array  , n):
#   ans = []
  
#   #:==Function for finding maximum
#   def  maximun(array  , n):
#     if n == 0:
#         return array[0]
    
#     maximum_in_rest = maximun(array , n - 1)

#     if (array[n - 1] > maximum_in_rest):
#        return array[n - 1]
#     else:
#        return maximum_in_rest

#   #:==Function for finding minimum
#   def minimum(array , n):
#      if n == 0:
#         return array[0]
     
#      minimum_in_rest = minimum(array , n - 1)

#      if(array[n - 1] < minimum_in_rest):
#         return array[n - 1]
#      else:
#         return minimum_in_rest
     
#   min_value = minimum(array , n)
#   ans.append(min_value)
#   max_value = maximun(array , n)
#   ans.append(max_value)

#   return ans

# array = [10  , 50 , 40 , 1]
# length = len(array)
# print(maxmin(array , length))#Output:[50 , 1]


#Q:===Write a function using rescurion to print sum first of n numbers

# def sum_N_Numbers(n):
#     if (n == 0):
#       return n
#     if (n == 1):
#       return n
    
#     return n + sum_N_Numbers(n - 1)

# print(sum_N_Numbers(3))#Output:6
# print(sum_N_Numbers(4))#Output:10
    
#:===Write a recursuve function to reverse an array.

# def reverseArray(arr , left , right):
#   if (left > right):
#     return arr
  
#   arr[left] , arr[right] = arr[right] , arr[left]
#   return  reverseArray(arr ,left +  1 , right - 1)

# array = [1 , 2 , 5 , 9]
# left = 0
# right = len(array) - 1
# print(reverseArray(array , left , right))


#===Write a function to check whether the string is palindrome or not

# def checkPalindrome(left , string , n):
#    if(left >= n):
#       return True
   
#    if(string[left] != string[n - left - 1]):
#       return False

#    return checkPalindrome(left + 1 , string , n)

# string = "radar"
# left = 0
# length = len(string)
# print(checkPalindrome(left , string , length))#Output:True

# string2 = "city"
# left = 0
# length = len(string2)
# print(checkPalindrome(left , string2 , length))#Output:False

#===Q:Write a function using recursion to sort an array.

def bubbleSort(arr , n):
  if n == 0 or n == 1:
    return arr
  
  for i in range(n - 1):
    if(arr[i] > arr[i + 1]):
      arr[i] , arr[i + 1] = arr[i+ 1] , arr[i]

  return bubbleSort(arr , n -1)

array = [10 , 45 , 3 , 2 , 1]
length = len(array)
print(bubbleSort(array , length))

  
    

    





        
      
       

    
       

















    














