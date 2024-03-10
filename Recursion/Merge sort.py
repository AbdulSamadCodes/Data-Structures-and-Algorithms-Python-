
#===Q:==You are given an array  arr ,sortit by using merge sort==================

def merge(array , s , e):
    mid = s + (e - s // 2) 

    array_len_1 = mid - s + 1
    array_len_2 = e - mid

    array1 = []
    array2 = []

    #Filling elemnts in the left array
    left_element = s
    i = 0
    while i < array_len_1:
          array1[i] = array[left_element]
          left_element+=1
          i+=1
    
    #Filling elemnts in the right array
    right_element = mid + 1
    j = 0
    while j < array_len_2:
        array2[j] = array[right_element]
        right_element+=1
        j+=1

    #Merging both  array  in sorted order

    index_1 = 0
    index_2 = 0

    mainArrayIndex = s
    while(index_1 < array_len_1 and index_2 < array_len_2):
        if(array1[index_1] < array2[index_2]):
            array[mainArrayIndex]  = array1[index_1]
            mainArrayIndex+=1
            index_1+=1
        else:
            array[mainArrayIndex]  = array1[index_2]
            mainArrayIndex+=1
            index_2+=1

    while(index_1 < array_len_1):
        array[mainArrayIndex] = array1[index_1]
        mainArrayIndex+=1
        index_1+=1

    while(index_2 < array_len_2):
        array[mainArrayIndex] = array2[index_2]
        mainArrayIndex+=1
        index_2+=1

def mergeSort(arr , start , end):
    if(start >= end):
        return
    
    mid = start + (end  - start // 2) 

    #Recursive case for left part
    mergeSort(arr , start , mid)

    #Recursive  case for right part
    mergeSort(arr , mid + 1 , end)

    #Now merging them 
    merge(arr , start , end)


test_array = [12,5,7,2,19,20]
start = 0
end = len(test_array) - 1
mergeSort(test_array , start , end)
print(test_array)





    

    



