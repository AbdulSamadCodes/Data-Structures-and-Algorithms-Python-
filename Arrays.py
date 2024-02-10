# import numpy as np

#Q Write a function program to reverse an array or a list

# def reverse(array):
#   start = 0
#   end = len(array) - 1
#   while(start < end):
#    temp = array[start]
#    array[start] = array[end]
#    array[end] = temp
#    start = start + 1
#    end = end - 1
#   print(array)

# array = [9,7,4,78,3,67,345,0]
# reverse(array)

#Q Write a function program to find unique element in an array

# def uniqueelem(array):
#     for i in range(len(array)):
#         if array[i] != array[i - 1]:
#             unique = array[i]
#             return [unique,i]
#     return -1  
 
# array = [10,10,10,10,10,20,10]
# print(uniqueelem(array)) 

# Write a  function to insert a value at a given position in an array
 
# def insertion(arr , pos , item , n , filled):
#      j = filled - 1
#      while (pos - 1 <= j):
#           arr[j + 1] = arr[j]
#           j = j - 1
#      arr[pos - 1]   = item
#      n = n + 1  

# array = [1 ,2 , 3 , 0 , 0 , 0]
# n = len(array) - 1
#insertion(array ,2, 45 , n , 3)
# print(array)           


# Write a  function to delete a value at a given position in an array

# def deletion(arr , n , pos):
#     value = arr[pos - 1]
#     j = pos - 1
#     while j < n - 1:
#         arr[j] = arr[j + 1]
#         j = j + 1
#     n = n - 1

# array = [34 , 56 ,67, 0]
# n = len(array)
# deletion(array , n , 2)
# print(array)        
   

   
#Q Wrie a function program to find a single  duplicate value in an array

# def duplicatevalues(array):
#     for i in range(len(array)):
#         for j in range(i + 1,len(array)):
#             if array[i] == array[j]:
#                 duplicate = array[i]

#     return duplicate

# array = [30,40,30,50,70,60,50]
# print(duplicatevalues(array)) 


#Q Write a  function program to swap neighbouring elements in the array

# def swapneighbours(array):
#     for i in range(0,len(array),2):
#         temp = array[i]
#         array[i] = array[i + 1]
#         array[i + 1] = temp
#     print(array)

# array= [7,3,5,4,8,11]
# swapneighbours(array)        

#Same question with while loop

# def swapneighbours(array):
#         i = 0
#         while i < len(array):
#          temp = array[i]
#          array[i] = array[i + 1]
#          array[i + 1] = temp
#          i = i + 2
#         print(array)
# array= [6,5,37,19,50,48]
# swapneighbours(array)     

#Q You have been given an integer arraylist of size N.Where N is equal to 2M + 1.Now in the list 'M' Numbers are present  twice  and one number is present only once.You need to find that number which is unique

# def unique(array):
#     ans = 0
#     for i in range(len(array)):
#         ans = ans ^ array[i]
#     return ans

# array = [45,67,98,6,98,45,67]
# result = unique(array)
# print(result) 

#Leetcode Problem
# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

# def checkoccurrence(array):
#    cdict = {}
#    for num in array:
#       if num in cdict:
#          cdict[num] += 1
#       else:
#          cdict[num] = 1

#    count_set = set()
#    for count in cdict.values():
#       if count in count_set:
#          return False
#       count_set.add(count)
#    return True

# array = [2,5,5,6,6,6,6]
# result = checkoccurrence(array)
# print(result)


#--Q:You are  given an array of numbers.Swap the alternate elemnets.

# def  swapAlternate(array):
#     n = len(array)
#     i = 0
#     while i <= n - 2:
#         array[i] , array[i + 1] = array[i + 1] , array[i]
#         i = i + 2
#     return array


# array = [1,2,5,7,9]
# array2 = [1 , 3 , 2 , 7 , 11 , 8]
# print(swapAlternate(array))    
# print(swapAlternate(array2))



#-------Q:You have been an integer arraylist of size N.Where N is equal to  (2M + 1).You need to find and return number which is unique.

# def uniqueNumber(array):
#     n = len(array)
#     unique = 0
#     for i in range(n):
#         unique ^= array[i]
#     return unique


# array = [3 , 7 , 2 , 2 , 3 ,7 , 4]
# array2 = [5 , 5 , 100 , 7 , 7 ,9 ,9]
# print(uniqueNumber(array))
# print(uniqueNumber(array2))


#-------Q:Given an array of integer arr , return true if the number of ocurrences  of each element is unique,false otherwise.

# def haveUniqueOccurrences(arr):
#     n = len(arr)
#     countDict =  dict()
#     for i in range(n):
#         if countDict.get(arr[i]):
#             countDict[arr[i]] += 1
#         else:
#             countDict[arr[i]] = 1    
#     return len(countDict) == len(set(countDict.values()))   

# array = [1 , 2 , 2 , 1 , 1 , 3]    
# array2 = [2,1,3]
# print(haveUniqueOccurrences(array))  
# print(haveUniqueOccurrences(array2))


#-----------------------Leetcode Question--------------#/

#Q:You are given an array of inetegrs containing each number from 1 to n-1.Where n is the length of array.But there is one number which is present twice.Find and return that number.

# def findDuplicate(array , n):
#     ans = 0
#     for i in range(n):
#         ans = ans ^ array[i]
#     for j in range(1,n):
#         ans = ans ^ j
#     return ans

# array = [1,2,3,5,6,4,6]
# n = len(array)
# print(findDuplicate(array , n))



#Q:-----------You are  given two sorted  arrays arr1 and arr2 both of them are in non-decreaasing order.You need to find the return a list of instersected elements,if there is no such return -1.

# def arrayIntersection(arr1 , arr2):
#     n = len(arr1)
#     m = len(arr2)
#     i = 0
#     j = 0
#     ans = []

#     while i < n and j < m:
#         if arr1[i]  <  arr2[j]:
#             i+=1
#         elif arr1[i] == arr2[j]:
#             ans.append(arr1[i])  
#             i += 1          
#             j += 1
#         else:
#             j+=1
#     if not ans:        
#       return -1
#     else:
#         return ans



# array1 = [1,2,2,2,3,4]
# array2 = [2,2,3,3]

# array3 = [10,20,48,7]
# array4 = [12,2,4,9]
# print(arrayIntersection(array1 , array2))
# print(arrayIntersection(array3,array4))


#--------------------Important Question------------------


# Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the intersection (or common elements) of the two arrays.
# For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

# def NumberofElementsInIntersection(a, b, n, m):
#     a = sorted(a)
#     b = sorted(b)
#     count = 0
#     i = 0
#     j = 0
#     while i < n and j < m:
#         if i > 0 and a[i] == a[i - 1]:
#             i+=1
#         if b[j] > a[i]:
#             i+=1
#         elif a[i] == b[j]:
#             i+=1
#             j+=1
#             count+=1
#         else:
#             j+=1
#     return count 
    

# array1 = [89, 24, 75, 11, 23]
# array2 = [89, 2, 4]
# print(NumberofElementsInIntersection(array1 , array2 , 5 , 3))


#Q:You are given an array of integer array of size N and ineteger S.Your task is to return the list  of all element pair whose sum is equal to S.It should return pairs of sum in a sorted order

# def pairSum(arr , n , S):
#     ans = []
#     for i in range(len(arr)):
#         for j in range(i + 1 , len(arr)):
#             if arr[i] + arr[j] == S:
#                 ans.append([arr[i] , arr[j]])
                    
#     for i in range(len(ans)):
#         ans[i].sort()
#     return ans    


# array = [11,5,12,45,6,17,0]
# S = 17
# n = len(array)
# print(pairSum(array , n , S))


#Q:---You have been array of 0s and 1s . Sort it such that all 0s come to left and all 1s come to right.

# def sort(arr , n):
#     left = 0
#     right = n - 1

#     while left < right:
#         while arr[left] == 0 and left < right:
#             left+=1
#         while arr[right] == 1 and left < right:
#             right-=1
#         if arr[left] == 1 and arr[right] == 0 and left < right:       
#             arr[left] , arr[right] = arr[right] , arr[left]
#             left+=1
#             right-=1
    
#     return arr

# array = [0,0,1,1,0,0,0,1,1,0,0]
# n = len(array)
# print(sort(array, n))        
                    

#Q:---Reverse the given array.

# def reverseArray(array , n):
#     left = 0
#     right = n - 1
#     while (left < right):
#         array[left] , array[right] = array[right]  , array[left]
#         left+=1
#         right-=1
#     return array


# arr = [10,23,45,67,89,9]
# n = len(arr)
# print(reverseArray(arr , n))

#-----------------Leetcode Prolem-----------


#Q:Given two sorted arrays mege them in a third array in a sorted order.

# def mergeSortedArrays(arr1 , arr2 , n , m):
#     i = 0
#     j = 0
#     ans = []
#     while (i < n and j < m):
#         if arr1[i] < arr2[j]:
#             ans.append(arr1[i])
#             i+=1
#         else:
#             ans.append(arr2[j])
#             j+=1
#     while i < n:
#         ans.append(arr1[i])
#         i+=1
#     while j < m:
#         ans.append(arr2[j])
#         j+=1
#     return ans

# array1 = [70,89,1000]
# array2 = [2 , 6 , 9] 
# n = len(array1)
# m = len(array2)

# print(mergeSortedArrays(array1 , array2 , n , m))


#Q:You are given two sorted arrays.Merge ten such that the result should be stored in first array itsef.The empty spaces in the first array will be equal to the length m of second array.






#Q:You are given an array of integer,move all zeroes in it to the end and you have to do it while mantaining the relative order of non-zero elements.

# def moveZeroes(arr , n):
#     i = 0
#     for j in range(n):
#         if arr[j] != 0:
#             arr[i] , arr[j] = arr[j] , arr[i]
#             i+=1
#     return arr

# array = [1,2,0,34,45,0,0,0]
# n = len(array)
# print (moveZeroes(array , n))        

#------------------------Important Leetcode Question----------------

#Q:--------Given an array , rotate the array by x steps 


# def rotateArray(arr , n  , k):
#     temp = [0] * n
#     for i in range(n):
#        temp[(i + k) % n] = arr[i]
#     arr = temp
#     return arr 

# array = [11,12,45,67]
# n = len(array)
# k = 2
# print(rotateArray(array , n , k))









               
               
    








        



























                 
                







    



  










  


  






