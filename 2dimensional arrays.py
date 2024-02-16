
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


               

            
















