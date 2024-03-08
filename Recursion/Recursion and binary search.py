
#===========Write a function using recusrion to  perform binary Search============

# def  binarySearch(arr , start ,end , key):
      
#       #If start  gets greater than end return -1
#       if (start > end):
#             return -1
      
#       mid = start + (end - start) // 2

#       #If key is found return index which is mid
#       if (arr[mid] == key):
#             return mid

#       if(key > mid):
#            return binarySearch(arr , mid + 1 , end , key)

#       else:
#            return binarySearch(arr , start , mid - 1 , key)


# array  = [10 , 45 , 67 , 89 , 102 , 108]
# key = 102
# start = 0
# end = len(array) - 1
# print(binarySearch(array ,start , end , key))#Output:4


# #Q:----In a  monotic array , find the total no. of occurrences of a an element----

# def firstOccurrence(arr ,  start , end , key, occurrence):
#     if (start > end):
#         return occurrence
    
#     mid = start + (end - start) //  2

#     if (arr[mid] == key):
#         occurrence = mid
#         return firstOccurrence(arr  , start ,mid - 1,key, occurrence)
                        
#     elif(arr[mid] >  key):
#          return firstOccurrence(arr  , start ,  mid - 1 ,key, occurrence)
        
#     else:
#         return firstOccurrence(arr  , mid + 1 ,  end,key, occurrence)


# def lastOccurrence(arr , start , end  , key , occurrence):
#     if (start > end):
#         return occurrence
    
#     mid = start + (end - start) //  2

#     if (arr[mid] == key):
#         occurrence = mid
#         return lastOccurrence(arr  , mid + 1 ,  end ,key, occurrence)
          
#     elif(arr[mid] >  key):
#         return lastOccurrence(arr  , start ,  mid - 1 ,key, occurrence)

#     else:
#         return lastOccurrence(arr  , mid + 1 ,  end ,key, occurrence)
           

# def totalOccurrences(arr , start , end ,key, occurrences):
#     first_occurr_index = firstOccurrence(arr , start , end ,key, occurrences)        
#     last_occurr_index = lastOccurrence(arr , start , end ,key, occurrences)  

#     return last_occurr_index - first_occurr_index + 1

# array = [5 ,7, 7, 7 ,8 ,8, 8]
# start = 0
# end  = len(array) - 1
# key = 8
# initial_ocurrence= 0  
# print(totalOccurrences(array , start , end ,key , initial_ocurrence))#Output:3
    

#Q:-------------Find the peak index in a mountain array----------------.

# def peakIndex(arr , start , end):
#     if start >= end:
#        return start
    
#     mid = start +  (end - start) // 2

#     if(arr[mid] < arr[mid + 1]):
#         return peakIndex(arr ,  mid + 1 , end)
    
#     else:
#         return peakIndex(arr ,  start , mid)
    

# # array = [7 , 8 , 10  ,6 , 4]
# # start = 0
# # end = len(array) - 1
# # print(peakIndex(array, start , end))#Output:2 

# array2 = [10 , 32 , 67 , 100 , 4]
# start = 0
# end = len(array2) - 1
# print(peakIndex(array2 , start , end))#Output:3

#Q:-------------Find pivot in a  rotated sorted  array----------------.

# def pivot(arr, start , end):
#     if start >= end:
#         return start
    
#     mid = start + (end - start)  // 2

#     if(arr[0] < arr[mid]):
#         return pivot(arr , mid + 1 , end)
#     else:
#         return pivot(arr, start , mid )

# array = [32 , 28 , 17 , 16 , 15, 10 , 13]
# start = 0
# end = len(array) - 1
# print(pivot(array , start , end))







    
    





    
















