
#Q===:Write a recursive function to reverse a string=======

# def reverse(str):
#    if len(str) <= 1:
#       return str
   
#    return reverse(str[1:]) + str[0]

# string = "Hello"
# print(reverse(string))#Output:olleH


#Q===Write a function to check whether the string is palindrome or not

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


    



