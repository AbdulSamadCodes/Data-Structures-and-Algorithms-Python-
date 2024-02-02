
import numpy as np

#QFind the index of the given targetvalue in the sequence

# sequence = [10,78,76,56,43,89,90,89]
# targetvalue = 89

# def linearsearch(sequence,targetvalue):
#    i = 0
#    while i < len(sequence):
#       if sequence[i] == targetvalue:
#             return i
#       i = i + 1
#    return -1
# result = linearsearch(sequence,targetvalue)  
# print(result) 

#Q: Write a program that checks whether the given element is present in the array or not

# def check(array,value):
#     i = 0
#     for i in range(len(array)):
#         if array[i] == value:
#             return True
#     return False


# array = [10,20,56,78,75,43]
# value = int(input("Enter the value to search"))
# found = check(array,value)
# if(found):
#     print("Value is present")
# else:
#     print("Value is not found")    


#Q ----Lab question by Sir Akram----------------


# def resultarray(target,query,):

#     result = np.array([0 for i in range(len(query))])
#     for i in range(len(query)):
#         counter = 0
#         for j in range(len(target)):
#          if query[i] == target[j]:
#             counter  = counter + 1
#         result[i] = counter
#     print(result)

# target = [89,57,67]
# query = [89,34,56]
# resultarray(target,query)   
# 

#Given an array of numbers A and a target value x, return indices of two numbers such that they add up to x. 
# def checkindexsum(array,value):
#     for i in range(len(array)):
#         if array[i] + array[i + 1] == value:
#             return[i,i + 1]
#     return -1

# array =  [8,7,5,5,98]
# value = 15
# print(checkindexsum(array,value))   


#Write a program to reverse an array using Linaer Search

# def Reverse(array):
#     i  = 0
#     j = len(array) - 1
#     while i < j:
#         array[i] , array[j] = array[j] , array[i]
#         i = i + 1
#         j = j - 1
#     return array

# array = [8,43,6,9,87,45]
# print(Reverse(array))    






  


    













    









   




        
    
               



          
   
          









         