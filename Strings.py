#-----------------Important leetcode Question------

#-------------String Compression---------

# def compress(charArray):

#     i = 0
#     ansIndex = 0
#     n = len(charArray)

#     while (i < n):

#         j = i + 1

#         while (j < n and charArray[i] == charArray[j]):
#             j = j + 1
            
#         charArray[ansIndex] = charArray[i]
#         ansIndex = ansIndex + 1
#         count = j - i
        
#         if count > 1:
#             stringCount = str(count)
#             for k in range(len(stringCount)):
#              characterArray[ansIndex] = stringCount[k]
#              ansIndex = ansIndex + 1
      

#         i = j
#     return ansIndex        


# characterArray = ['a' , 'a' , 'a' , 'b' , 'b' , 'c']
# print(compress(characterArray))

#----------Given two strings s1 and s2 , return true if s2 contains a pernutation of s1 , or false otherwise.

# def checkPermutation(s1 , s2):

#     #Method for checking if windows are equal

#     def isEqual(array1 , array2):
#         for i in range(26):
#             if array1[i] != array2[i]:
#                 return False
#         return True    
    
#     #Counting the characters in s1
#     count1 = [0] * 26
#     for i in range(len(s1)):
#         index = ord(s1[i]) - ord('a')
#         count1[index]+=1

#     #Counting the characters in s2 and traversing the firstwindow
#     i = 0
#     windowSize = len(s1)
#     count2 = [0] * 26    
        
#     while i < windowSize and i < len(s2):
#         index = ord(s2[i]) - ord('a')
#         count2[index]+=1
#         i+=1
    
#     if isEqual(count1 , count2):
#         return 1
    
#     #Now traversing for remainin windows

#     while(i < len(s2)):
#         newChar = s2[i]
#         index = ord(newChar) - ord('a')
#         count2[index]+=1

#         oldChar = s2[i - windowSize]
#         index = ord(oldChar) - ord('a')
#         count2[index]-=1

#         i+=1

#         if isEqual(count1 , count2):
#             return 1

#     return 0    


# string1 = "ab"
# string2 = "eidbaooo"
# print(checkPermutation(string1 , string2))






















         



 

        

        



