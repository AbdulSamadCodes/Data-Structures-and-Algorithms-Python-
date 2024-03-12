
#======Write a function to sort an array using quick sort algorithm======.

#Function to  compute the partition index
def partition(arr  , start , end):
    count  = 0
    for i in range(start + 1 , end + 1):
        if(arr[i] < arr[start]):
            count+=1
    pivot_index = start  + count
    arr[start] , arr[pivot_index] = arr[pivot_index] , arr[start]

    #Now we will place the elemenets smaller at the left and greater at the right
    left = start
    right = end

    while(left < pivot_index and right > pivot_index):
         while(arr[left] <= arr[pivot_index]):
             left+=1
         while(arr[right] > arr[pivot_index]):
             right-=1

         if(left  < pivot_index and right > pivot_index):    
           arr[left] , arr[right] = arr[right] , arr[left]
           left+=1
           right-=1

    return pivot_index       


def quickSort(array , start , end):
    #Base case when end is less than equal to start
    if start >= end:
        return
    
    #Now we will get the partition index
    p_index = partition(array , start , end)

    #Recursive call for sorting the left part
    quickSort(array , start , p_index)

    #Recursive call for sorting the right part
    quickSort(array , p_index + 1 , end)


array = [ 8, 7 ,89, 2, 1]
start = 0
end = len(array) - 1
quickSort(array , start , end)
print(array)#Output:[1, 2, 7, 8, 89]




