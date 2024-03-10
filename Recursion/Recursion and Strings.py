
#Q:======Write a  function to reverse a given string================.

# def reverseString(str):
#     if len(str) <= 1:
#         return str
    
#     return reverseString(str[1:]) + str[0]

# string = "Hello"
# print(reverseString(string))#Output:olleH
    

#Q:======Write a  function to check whether two  strings are palindrome or not.==============.

# def isPalindrome(str,left,right):
#     if left > right:
#         return True
    
#     if str[left] != str[right]:
#         return False
    
#     return isPalindrome(str , left+1 , right - 1)


# string = "radar"
# left = 0
# right = len(string) - 1
# print(isPalindrome(string , left , right ))
    

#Q:======Write a  function to perform bubble sort using recursion.==============.

# def bubbleSort(array , n):
#     if (n == 0 or n == 1):
#         return True
    
#     i = 1
#     for i in range(n - 1):
#         if(array[i] > array[i + 1]):
#             array[i] , array[i + 1] = array[i  + 1] , array[i]

#     #Recursively calling it by by decrementing the length
#     bubbleSort(array , n -1)


# array = [10,3,5,67,5]
# length = len(array)
# bubbleSort(array , length)
# print(array)


    

    




    
    

