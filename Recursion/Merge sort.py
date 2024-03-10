
#===Q:==You are given an array  arr ,sortit by using merge sort==================

def merge(array , s , e):

    mid = s + (e - s) // 2

    len_arr_1 = mid - s + 1
    len_arr_2 = e - mid

    array_1 = [0] * len_arr_1
    array_2 = [0] * len_arr_2

    #Filling the first array with left part
    i = 0
    right_element = s
    while(i < len_arr_1):
        array_1[i] = array[right_element]
        right_element+=1
        i+=1
    
    #Filling the second array with right part
    j = 0
    left_element = mid + 1
    while(j < len_arr_2):
        array_2[j] = array[left_element]
        j+=1
        left_element+=1


    #Now merging both sorted arrays
    index_1 = 0
    index_2 = 0
    main_Array_Index = s

    while(index_1 < len_arr_1  and index_2 < len_arr_2):
       
       if(array_1[index_1] <  array_2[index_2]):
           array[main_Array_Index] = array_1[index_1]
           main_Array_Index+=1
           index_1+=1
       else:
           array[main_Array_Index] = array_2[index_2]
           main_Array_Index+=1
           index_2+=1
    
    while(index_1 < len_arr_1):
        array[main_Array_Index] = array_1[index_1]
        main_Array_Index+=1
        index_1+=1

    while(index_2 < len_arr_2):
        array[main_Array_Index] = array_2[index_2]
        main_Array_Index+=1
        index_2+=1
    
def mergeSort(arr , start , end):
    if(start >= end):
        return
    
    mid = start + (end - start ) // 2
    
    #Recursive case for sorting left part
    mergeSort(arr , start , mid )

    #Recursive case for sorting right part
    mergeSort(arr , mid + 1 , end)

    merge(arr , start , end)


test_array = [10, 4 , 5 , 29 , 98]
start = 0
end = len(test_array) - 1
mergeSort(test_array , start , end)
print(test_array)

   




    

    



