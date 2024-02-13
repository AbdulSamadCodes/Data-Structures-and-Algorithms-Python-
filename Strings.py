
#-----------------Important leetcode Question------

#-------------String Compression---------

def compress(charArray):

    i = 0
    ansIndex = 0
    n = len(charArray)

    while (i < n):

        j = i + 1

        while (j < n and charArray[i] == charArray[j]):
            j = j + 1
            
        charArray[ansIndex] = charArray[i]
        ansIndex = ansIndex + 1
        count = j - i
        
        if count > 1:
            stringCount = str(count)
            for k in range(len(stringCount)):
             characterArray[ansIndex] = stringCount[k]
             ansIndex = ansIndex + 1
      

        i = j
    return ansIndex        


characterArray = ['a' , 'a' , 'a' , 'b' , 'b' , 'c']
print(compress(characterArray))






         



 

        

        



