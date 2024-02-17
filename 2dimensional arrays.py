
import numpy as np

#------The formula for maping of 2d arrays with 1d arrays is C * i + j where C is number of columns.-----

#----------Creating a 2d array in numpy----------*

# array = np.array([[0 for i in range(5)] for j in range(4)])


#-------  Taking input of  2d array in numpy-----*


#-------Row wise input--------

# rows = 3
# cols = 4
# array = np.array([[0 for i in range(cols)] for j in range(rows)])
# for i in range(rows):
#     for j in range(cols):
#         array[i , j] = int(input(f" Enter element on row {i} and column{j}: "))

# print(array)        



#-------Column wise input--------1

# rows = 3
# cols = 4
# array = np.array([[0 for i in range(cols)] for j in range(rows)])
# for i in range(cols):
#     for j in range(rows):
#         array[j ,i] = int(input(f" Enter element on column {i} and row{j}: "))
# print(array)  


#Q:------------Given a 2d array give a list of the sum of all the rows in the 2d array-------------.


# def  rowWiseSum(array):
#     ans = []
#     for i in range(len(array)):
#         sum = 0
#         for j in range(len(array[0])):
#             sum+=array[i][j]
#         ans.append(sum)
#     return ans


# inputarray = np.array([
#     [1,5,7],
#     [67,4,6],
#     [4,5,6,]
# ])            

# print(rowWiseSum(inputarray))


#-----------------------Leetcode problem----------------

#Q:----For a given two dimensional array arr of size (n by  m) ,print the array in sine  wave form i.e print the first column top to bottom ,then next bottom to top------------.


# def sineWaveprint(array):
#     k = len(array[0]) - 1
#     for j in range(len(array[0])):
#         if j % 2 == 0:
#          for i in range(len(array)):
#             print(array[i][j] , end = " ")
#         else:
#            while k >= 0:
#                 print(array[k][j] , end = " ")
#                 k-=1
#         k = len(array[0])  - 1   


# inputarray = np.array([
#     [1,5,7],
#     [67,4,6],
#     [4,5,6,]
# ])  

# print(sineWaveprint(inputarray))



#----------------------------Important Leetcode  problem-------------------------

#:Write an efficient algoritm that seraches for a value in a n x m matrix.This matrix has following properties.
#:Integers in each row are sorted from left to right
#:The first integer of each row is greater than than last one of previous row.

# def matSearch(matrix , target):
#     row = len(matrix)
#     col = len(matrix[0])

#     start = 0
#     end = row * col - 1

#     mid = start + (end - start) // 2

#     while start <= end:
#         element = matrix[mid // col][mid % col]
         
#         if element == target:
#             return 1
#         elif element < target:
#             start = mid + 1
#         else:
#             end = mid - 1

#         mid = start + (end - start) // 2  

#     return 0

# matrix = [[1,4,5,6],
#           [20,23,24,27],
#           [29,31,34,36]]
# target = 5
# target2 = 30
# print(matSearch(matrix , target))#:Output:1
# print(matSearch(matrix,target2))#:Output:0



#----------------------------Important Leetcode  problem-------------------------

#:Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.

# def Search(matrix,M,N ,X):
#     rowIndex = 0
#     colIndex = M - 1

#     while(rowIndex < N and colIndex >= 0):
#         element = matrix[rowIndex][colIndex]
        
#         if element == X:
#             return 1
        
#         elif element > X:
#             colIndex-=1

#         else:
#             rowIndex+=1

#     return 0



# inputMatrix =  np.array([[1,4,7,11],
#                          [2,5,8,12],
#                          [3,6,9,21],
#                          [8,9,678,689]])      

# N = len(inputMatrix)
# M = len(inputMatrix[0])
# target = 9
# print(Search(inputMatrix, M , N , target)) 

















               

            
















