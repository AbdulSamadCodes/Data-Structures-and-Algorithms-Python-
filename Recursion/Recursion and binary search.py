
#Q===Write a recursive function to perform binary search====

# def binarySearch(arr , start , end , key):
#     if (start >  end):
#         return -1
   
#     mid = start + (end - start) // 2
    
#     if(arr[mid] == key):
#        return mid    
#     elif(arr[mid] < key):
#        return binarySearch(arr , mid + 1 , end , key)
#     else:
#        return binarySearch(arr , start, mid - 1,key)

# array = [10 , 14 , 18 , 23 , 25]
# start = 0
# end = len(array) - 1
# key = 23
# print(binarySearch(array,start,end,key))#Output:3


#Q=====:Find peak in a mountain array========

# def peak(arr , start,end ): 
#     if(start >= end):
#       return start
    
#     mid = start + (end - start) // 2 
    
#     if(arr[mid +  1] > arr[mid]):
#       return  peak(arr , mid + 1 , end)
#     else:
#       return  peak(arr,start,mid)
    

# array = [7 , 8, 10 , 6]
# start = 0
# end = len(array) - 1
# print(peak(array,start,end))     

# array2 = [0 , 1 , 0]
# start = 0
# end = len(array2) - 1
# print(peak(array2,start,end))     
        
        
        
  
     
       
       
    
    







    
    





    
















