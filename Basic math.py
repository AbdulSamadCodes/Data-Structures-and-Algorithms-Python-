
#Q:-------Given an integer n, return the number of prime numbers that are strictly less tahn n.

#-------------------Using Seive of Erastothenes---------------

# def countPrimes(n):
#     count = 0
#     primeNumbers = [True] * (n + 1) 

#     primeNumbers[0] = False
#     primeNumbers[1] = False
#     for i in range(2 , n):
#         if (primeNumbers[i]):
#              count+=1
#              j = (i * 2)
#              while j < n:
#                  primeNumbers[j] = False
#                  j = j + i
#     return count

# print(countPrimes(40))


#Q:----------Find the Greatest common divisor / Highest common factor of two numbers by iterative approach.---------------

# def findGDC(num1  , num2):
#     if num1==0:
#         return num2
#     if num2 == 0:
#         return num1
    
#     while (num1 is not  num2):
#         if num1 > num2:
#             num1 = num1 - num2
#         else:
#              num2 = num2 - num1

#     return num1

# print(findGDC(35 , 66))#Output:1
# print(findGDC(24 , 72))#Output:24


#Q:---------Given two integers a and b . Find a ^ b iteratively---------*

# def findPower(a , b):
#     result = 1
#     for i in range(0 , b):
#         result = result * a

#     return result

# print(findPower(2 , 3))#Output:8
# print(findPower(8 , 10))#Output:1073741824


#----------------------------------Modular arithemetic------------------------------------#

#----Some basic properties of modulo operator-----


#--a % m + b % m = (a + b) % m
#--a % m - b % m = (a - b) % m
#--a % m * b % m = (a * b) % m



#-------------------------Leetcode  question-----------------------------

#------------------------Modular exponentation--------------------

#:----You are given three integers 'X' , 'N' and  'M'.Your task is to find ('X' to the power of  'N') % M.

# def modularExponentation(X , N , M):
#     result = 1
#     while ((N) > 0):
#         if (N & 1):
#             result = ((result) % M * (X) % M) % M

#         X = ((X) % M *  (X) % M ) % M
#         N = (int)(N >> 1)

#     return result

# X = 2
# N = 9
# M = ((10 ** 7) + 7)
# print(modularExponentation(X , N , M))







      




            

    

    
