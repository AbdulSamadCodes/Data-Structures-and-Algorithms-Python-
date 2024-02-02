#Pattern1

# i = 1
# n = 5
# while i <= n:
#     i = i + 1
#     j = 1
#     while j <= n:
#         print("*",end="")
#         j = j + 1
#     print()

#pattern2

# i = 1
# n = 3
# while i <= n:
#     j = 1
#     while j <= n:
#         print(i,end="")
#         j = j + 1    
#     print()
#     i = i + 1

#pattern3

# i = 1
# n = 4

# while i <= n:
#     j = 1
#     while j <= n:
#         print(j,end=" ") 
#         j = j + 1
#     print()    
#     i = i + 1


#pattern4 

# 3 2 1
# 3 2 1
# 3 2 1

# i = 1
# n = 3

# while i <= n:
#     j = 1
#     while  j <= n:
#         print(n - j + 1,end=" ")
#         j = j + 1
#     print()    
#     i = i + 1  

#pattern 5  

# 1 2 3
# 4 5 6
# 7 8 9

# i = 1
# n = 3
# count = 1
# while i <= n:
#     j = 1
#     while j <= n:
#         print(count,end="")
#         count = count + 1
#         j = j + 1
#     print()    
#     i = i + 1


#pattern 6
# *
# **
# ***
# ****
# *****

# i = 1
# n = 5

# while i<=n:
#     j = 1
#     while j<=i:
#         print("* ",end="")
#         j = j + 1
#     print()
#     i = i + 1

#pattern7

# 1
# 2 3 
# 4 5 6 
# 7 8 9 10

# i = 1
# n = 4
# count = 1

# while i <= n:
#     j = 1
#     while j <= i:
#         print(count,end=" ")
#         count = count + 1
#         j = j + 1
#     print()
#     i = i + 1   

#pattern8

# 1
# 2 3
# 3 4 5
# 4 5 6 7

# i = 1
# n = 4


# while i <= n:
#     j = 1
#     count = i
#     while j <= i:
#         print(count,end=" ")
#         count = count +  1
#         j = j + 1
#     print()
#     i = i + 1

#pattern 9

# 1 
# 2 1
# 3 2 1
# 4 3 2 1

# i = 1
# n = 4
# while i<=n:
#     j = 1
#     count = i
#     while j <= i:
#         print(count,end=" ")
#         count = count - 1
#         j = j + 1
#     print()
#     i = i + 1    

# pattern10

# i = 1
# n = 4
# while i <= n:
#     j = 1
#     while j <= i:
#      print(j + n -i,end = "")
#      j = j + i 
#     print()


#pattern 11
  
# A A A
# B B B
# C C C

# characters  = ['A','B','C']
# for i in range(len(characters)):
#     for character in characters:
#         print(characters[i],end = "")
#     print()    

#pattern11

# A B C
# A B C
# A B C

# characters  = ['A','B','C']
# for i in range(len(characters)):
#     for j in characters:
#         print(j,end=" ")
#     print()    


#pattern 12

# A B C
# D E F 
# G H I

# characters  = ['A','B','C','D','E','F','G','H','I']

# count = 0
# for i in range(3):
#     for j in range(3):
#         print(characters[count] ,end= " " )
#         count = count + 1
#     print()    

#pattern 13

# A 
# B C
# D E F 
# G H I J

# characters =  ['A','B','C','D','E','F','G','H','I','J']

# count = 0
# for i in range(4):
#     for j in range(i + 1):
#         print(characters[count],end=" ")
#         count = count + 1
#     print()    

#pattern 14

#      *
#     **
#    ***
#   ****
# ******

# for i in range(1,6):
#     for j in range(i  + 1,6):
#         print(" ",end="")
#     for k in range(i):
#         print("*", end="")
#     print()            










































