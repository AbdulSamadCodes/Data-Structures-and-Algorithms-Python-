#-----------------------------------Prime numbers and factors---------------------------------

#Q:-------Given an integer n, Check if the number is prime or not.

def checkPrime(n):
    count = 0
    i = 1
    while i * i <= n:
        if (n % i) == 0:
            count+=1
            if ((n / i) != i):
                count+=1
        i+=1        
    return count == 2


print(checkPrime(4))#:Output:True


#Q:---------Given an integer n, return the sum of its factors.

# def factorsSum(n):
#     sum = 0
#     i = 1
#     while i * i <= n:
#         if (n % i == 0):
#             sum+=i
#             if ((n/ i) != i):
#                 sum+= (int)(n / i)
#         i+=1        
#     return sum


# print(factorsSum(38))#Output:60
# print(factorsSum(46))#Output:72             

#Q:-----------------Code forces problem-----------------

#----You are given one integer number n. Find three distinct integers a,b,c such that 2≤a,b,c and a⋅b⋅c=n or say that it is impossible to do it-----.
# def threeIntegersProduct(n):
#     a = n
#     b = n
#     c = n
  
# #:---Loop for finding a-----  
#     i= 2
#     while i * i <= n:
#         if n % i == 0:
#             a = i
#             break
#         i = i + 1

# #:---Loop for finding b-----

#     n = n / a

#     j = 2
#     while j * j <= n:
#         if (n % j == 0 and a != j):
#             b = min(b , j)
#         j = j + 1    

#     c = (int)(n / b)

#     if (a != b and b!= c and c > 1):
#         print("Yes possible")
#         print(a , b , c) 
#     else:
#         print("Not pissible")


# threeIntegersProduct(64)#:Output(2 , 4 , 8)
# threeIntegersProduct(90)#:Output:(2 , 3 , 15)
# threeIntegersProduct(32)#:Output:Not possible



#Q:-------Given an integer n, return the number of prime numbers that are strictly less than n.

#-------------------Using Seive of Erastothenes---------------

# def countPrimes(n):
# #     count = 0
# #     primeNumbers = [True] * (n + 1) 
# #     primeNumbers[0] = False
# #     primeNumbers[1] = False
# #     for i in range(2 , n):
# #         if (primeNumbers[i]):
# #              count+=1
# #              j = (i * 2)
# #              while j <= n:
# #                  primeNumbers[j] = False
# #                  j = j + i
# #     return count

# # print(countPrimes(40))


#-------------------More optimize algorithm of  Seive of Erastothenes---------------

#Q:------------Write a method to check if a number n is prime or not.

# def checkPrimes(n):
#     primeNumbers = [True] * (n + 1)
#     i = 2
#     while i * i <= n:
#         if(primeNumbers[i]):
#             j = i * i
#             while j <= n:
#                 primeNumbers[j] = False
#                 j = j + i
#         i = i + 1
#     if primeNumbers[n]:
#         return True
#     else:
#         return False
       
    
# print(checkPrimes(31))#:Output:True
# print(checkPrimes(13))#:Output:True
# print(checkPrimes(99))#:Output:False



#Q:--------------You are given an integer k , Find the kth prime number .Constrain is that k >= 5 * 10^6.

# def findKthPrime(k):

#     #---First Generating a sieve up to 10^8 because this is the highest we can store in an array in most programming languages.

#     n = 100000000
#     Sieve = [True] * (n + 1)
#     i = 2
#     while i * i <= n:
#         if Sieve[i]:
#             j = i * i
#             while j <= n:
#                 Sieve[j] = False
#                 j += i
#         i += 1

#     # Once the sieve is generated, we need to find the last 5 * 10^6th prime number
        
#     limit = 5 * 1000000
#     size = 1
#     count = 0
#     i = 2  # Reset i for the second loop
#     while i <= n:
#         if Sieve[i]:
#             count += 1

#         if count == limit:
#             size = i
#             break
#         i += 1
    
#     # Now we have the size , we can store all the primes in a data structure.
        
#     result = [] 
#     l = 2
#     while l <= size:
#         if Sieve[l]:
#             result.append(l)

#     #Now we can simply return the kth prime value which will at k - 1 index.

#     return result[k - 1]        

# print(findKthPrime(5))


#:----------------Return an array containingg  the prime factorization of integer  n in O(n) worst case time complexity.----------------

# def primeFactorization(n):
#     ans = []
#     i = 2
#     while i <= n:
#         while ( n % i== 0):
#             ans.append(i)
#             n = (int)(n / i)
#         i+=1
#     return ans


# print(primeFactorization(48))
# print(primeFactorization(13))

#----We can modify the above algorithm in 0(sqrt(n)) complexity.

# def primeFactorization(n):
#     ans = []
#     i = 2
#     while i * i <= n:
#         while(n % i == 0):
#             ans.append(i)
#             n = n / i
#         i+=1
#     if (n > 1):
#         ans.append(n)    

#     return ans

# print(primeFactorization(100))
# print(primeFactorization(19)) 



#--------------------------Euclid algorithm--------------------

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









      




            

    

    
