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

# Write a  function to insert a value at a given index in an array

# def insertion_in_array(array,n,index,value):
#     j = n - 1
#     while j >= index:
#         array[j + 1] = array[j]
#         j = j - 1
#     array[index] = value
#     n = n + 1

# array = [10,20,30,40,50,60,0]
# insertion_in_array(array,6,2,80)
# print(array)

# Write a  function to delete a value at a given index in an array

# def deletion_in_array(array,index,n):
#     value = array[index]
#     j = index
#     for i in range(j,n):
#         array[i] =  array[i + 1]
#     n = n - 1

# array = [10,56,78,97,45,1]
# deletion_in_array(array,2,5)
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

def findMin(arr, n):
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[0] < arr[mid]:
                start = mid + 1
            else:
                end = mid 
        return start  

print(findMin([4 ,5 ,1 ,2 ,3] , 5))





        



























                 
                







    



  










  


  






