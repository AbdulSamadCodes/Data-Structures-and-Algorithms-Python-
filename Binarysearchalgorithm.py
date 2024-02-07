# Binary serach algorithm only works with monotic arrays.Its time complexity is O(log n).



#Q:Write a binary search algorithm to find a given key and return the index of  that key.If key is not present , return -1.

# def binarySearch(arr , key):
#     start = 0
#     end = len(arr) - 1
#     while start <= end:
#         midIndex = start + (end - start // 2)
#         midElement = arr[midIndex]
#         if  midElement == key:
#             return midIndex
#         elif key > midElement:
#             start = midIndex + 1
#         else:
#             end = midIndex - 1
#     return -1

# array = [10,13,15,17,19]
# key = 13
# print(binarySearch(array,key))#1


# #Q:In a  monotic array , find the total no. of occurrences of a an element


# def find( arr, n, x):
    
#     start = 0
#     end = n - 1
#     firstOccurrence = -1
#     lastOccurrence = -1
#     while start <= end:
#         midIndex = start + (end - start // 2)
#         if arr[midIndex] == x:
#             firstOccurrence = midIndex
#             end = midIndex - 1
#         elif arr[midIndex] >  x:
#             end = midIndex - 1
#         else:
#             start = midIndex + 1
            
#     start = 0
#     end = n - 1
#     lastOccurrence = -1
#     while start <= end:
#         midIndex = start + (end - start // 2)
#         if arr[midIndex] == x:
#             lastOccurrence = midIndex
#             start = midIndex + 1
#         elif arr[midIndex] >  x:
#             end = midIndex - 1
#         else:
#             start = midIndex + 1   
            
#     return lastOccurrence - firstOccurrence + 1    
                       
# arr = [5 ,7, 7, 7 ,8 ,8, 8]  
# n = len(arr)
# x = 8
# print(find(arr,n,x))


#Q:Find the peak index in a mountain array.

# def peakElement(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#      midIndex = start + (end - start ) // 2 
#      if arr[midIndex] < arr[midIndex + 1]:
#          start = midIndex + 1
#      else:
#          end = midIndex
#     return start 


# array = [0,1,0]
# print(peakElement(array))    
# 

#Q:Find pivot in a rotated sorted array.

# def Pivot(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         midIndex = start + (end - start ) // 2 
#         if arr[midIndex] > arr[0]:
#             start = midIndex + 1
#         else:
#             end = midIndex
#     return start

# array = [3 , 5 , 7 , 9 , 1]
# array2 = [7 , 9 ,1 , 2 , 3]
# print(Pivot(array))#Output:4 
# print(Pivot(array2))#Output:2          




#Q:Given a sorted and rotated array A of N distinct elements which are rotated at some point, and given an element K. The task is to find the index of the given element K in array A.

#:For Example:
#Input:
# N = 9
# A[] = {5,6,7,8,9,10,1,2,3}
# K = 10
# Output: 5
# Explanation: 10 is found at index 5.


# def  getPivot(arr , n):
#     start = 0
#     end = n -  1
#     while start < end:
#         mid = start + (end - start) // 2
#         if arr[mid] > arr[0]:
#             start = mid + 1
#         else:
#             end = mid
#     return start    
    
# def binarySearch(arr , s , e , k):
#     start = s
#     end = e
#     while start <= end:
#         midIndex = start + (end - start) // 2
#         midElement = arr[midIndex]
#         if  midElement == k:
#             return midIndex
#         elif k > midElement:
#             start = midIndex + 1
#         else:
#             end = midIndex - 1
#     return -1
    
# def Search(arr,n,k):
#     pivot = getPivot(arr,n)
#     if k >= arr[pivot] and k <= arr[n - 1]:
#         return binarySearch(arr , pivot ,n - 1 ,  k)
#     else:
#         return binarySearch(arr , 0 , pivot - 1 , k)
    

# arr = [5 , 6 ,  7,  8 ,  9, 10, 1 ,2, 3]
# n = len(arr)
# print(Search(arr , n))#OUTPUT:7


#:Given a non-integative integer  n , compute and return the floored square root of n.

# def binarySearch(n):
#     start = 0
#     end = n
#     ans = -1
#     while start <= end:
#         mid = start + (end - start) // 2
#         square = mid * mid
#         if  square == n:
#          return mid
#         if square < n:
#          ans = mid
#          start = mid + 1
#         else:
#           end = mid - 1    
#     return ans   

# def  squareRoot(n):
#     return binarySearch(n)


# print(squareRoot(4))#2
# print(squareRoot(50))#7


#:Given a non-integative integer  n , compute and return the exact  square root of n and the precision will be given in input.

# def squareRoot(n):
#     start = 0
#     end = n
#     ans = -1
#     while start <= end:
#         mid = start + (end - start) // 2
#         square = mid *  mid
#         if square == n:
#             return mid
#         elif square < n:
#             ans  = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ans

# def exactSquareRoot(n , precision ):
#     ans = float(squareRoot(n))
#     factor = 1.0
#     for i in range(precision):
#         factor  /= 10.0
#         j = ans
#         while j * j < n:
#             j += factor
#             ans = j
#     return ans
  
# print(exactSquareRoot(37,3))  
# print(exactSquareRoot(101 ,3))    


#-----------------LEETCODE PROBLEM---------------

#-----------------Book Allocation Problem------
       

# def isPossible(arr, n, m, mid):
#     studentCount = 1
#     pagesSum = 0
#     for i in range(n):
#         if pagesSum + arr[i] <= mid:
#             pagesSum += arr[i]
#         else:
#             studentCount += 1
#             if mid < arr[i] or studentCount > m:
#                 return False
#             pagesSum = arr[i]
#     return True


# def allocateBooks(arr, n, m):
#     start = 0
#     sum = 0
#     ans = -1
#     for i in range(n):
#         sum += arr[i]
#     end = sum    
#     while start <= end:
#         mid = (start + end) // 2
#         if isPossible(arr, n, m, mid):
#             ans = mid
#             end = mid - 1
#         else:
#             start = mid + 1
#     return ans

# array = [10, 20, 30, 40]
# n = len(array)
# no_of_students = 2
# print(allocateBooks(array, n, no_of_students)) 



#-----------------LEETCODE PROBLEM---------------

#-----------------Painter's Partition Problem------
       

# Dilpreet wants to paint his dog's home that has n boards with different lengths. The length of ith board is given by arr[i] where arr[] is an array of n integers. He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. 

# The problem is to find the minimum time to get this job done if all painters start together with the constraint that any painter will only paint continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.


# def minTime(arr , k , n):

#     #Function to check total no. of painters
#     def isPossible(mid):
#         painters = 1
#         time = 0
#         for i in range(n):
#             if time + arr[i] <= mid:
#                 time += arr[i]
#             else:
#                 painters += 1
#                 time = arr[i]
#         return painters
    
#     start  = max(arr)
#     end = sum(arr)
#     while start <= end:
#         mid = start + (end - start  2) // 2
#         if isPossible(mid) > k:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return start     


# arr = [5,10,30,20,15]
# n = len(arr)
# k = 3
# print(minTime(arr,k , n))


#---------------LeetCode Question---------------#

#-------------Aggressive Cows Problem------------------#

# def agressiveCows(arr , k ):

#     arr.sort()
#     def isPossible(mid):
#         cowsCounter = 1
#         lastPosition = arr[0]
#         for i in range(len(arr)):
#            if arr[i] - lastPosition >= mid:
#                cowsCounter+= 1
#                if cowsCounter == k:
#                    return True
#                lastPosition = arr[i]
#         return False       
                
    
#     start = 0
#     maxi = max(arr)
#     mini = min(arr)
#     end = maxi - mini
#     ans = 0

#     while start <= end:
#         mid = start + (end - start) // 2
#         if isPossible(mid):
#             ans = mid
#             start = mid + 1
#         else:
#             end = mid - 1
#     return ans        

# array = [4,2,1,3,6]
# k = 2
# print(agressiveCows(array , k))


#---------Important Leetcode problem------

#Q:A sorted(in ascending order) array A[ ] with distinct elements is rotated at some unknown point, the task is to find the minimum element in it.

# import sys
# def findMin(arr, n):
#     start = 0
#     end = n - 1
#     ans = sys.maxsize 
#     while start <= end:
#         mid = start + (end - start) // 2
#         if arr[start] <= arr[end]:
#             ans = min(ans , arr[start])
#             break
#         elif arr[mid] >= arr[start]:
#             ans = min(ans , arr[start])
#             start = mid + 1
#         else:
#             ans = min(ans  , arr[mid])
#             end = mid - 1
#         return ans   
# print(findMin([4,5,6,7,0,1,2],7))

















   




    






    












    



        
    












    

