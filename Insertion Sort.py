#Insertion sort is simple  and efficient sorting algorithm.Its time complexity is O(n^2) where n is the size of the array.

#Q:Sort the array arr using insertion sort algorithm where n is the length of the array--------

# def insertionSort(arr , n):
#     for i in range(1,n):
#         temp = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > temp:
#             arr[j + 1] = arr[j]
#             j = j - 1
#         arr[j + 1] = temp
#     return arr

# array = [56 ,  6 , 7 , 87 , 9]
# n = len(array)
# print(insertionSort(array,n))    

def insert(alist, index, n):
        temp = alist[index]
        j = index - 1
        while j >= 0 and alist[j] > temp:
            alist[j + 1] = alist[j]
            j = j -1 
        return j    

def insertionSort(alist, n):
    for i in range(n):
        position = insert(alist , i , n)
        alist[position + 1] = alist[i]
    return alist   
    

array = [56 ,  6 , 7 , 87 , 9]
n = len(array)
print(insertionSort(array,n))   










