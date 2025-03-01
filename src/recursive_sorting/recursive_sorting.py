# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    #elements = len(arrA) + len(arrB)
    merged_arr = []
    i = 0
    j = 0
    # TO-DO
    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr.append(arrA[i])
            i += 1
        else:
            merged_arr.append(arrB[j])
            j += 1

    merged_arr += arrA[i:]
    merged_arr += arrB[j:]

    return merged_arr


print(merge([9, 5, 6, 2, 9], [99, 10, 14, 2, 5]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    if(len(arr) <= 1):
        return arr
    mid = int(len(arr)/2)
    arrA = merge_sort(arr[:mid])
    arrB = merge_sort(arr[mid:])
    return merge(arrA, arrB)
   # return arr


print(merge_sort([9, 5, 6, 2, 9, 99, 10, 14, 2, 5]))
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
