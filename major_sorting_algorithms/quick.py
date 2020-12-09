
# my code for quick sort in place
def quick_sort(arr):

    #  quick_sort1(arr, 0, len(arr)-1)
    #  return arr

    def sort(input_array, start, end):
        # start = at pivot
        # end = # of elem + 1

        pivot = start
        border = start + 1

        if (end-start) < 2:
            return input_array

        for i in range(start+1, end):
            if input_array[i] <= input_array[pivot]:
                if i != border:
                    input_array[i], input_array[border] = input_array[border], input_array[i]
                border += 1

        input_array[pivot], input_array[border-1] = input_array[border-1], input_array[pivot]

        sort(input_array, start, border-1)
        sort(input_array, border, end)
        return input_array
        #  return sort( input_array, start, border-1 ) + [input_array[border]] + sort( input_array, border, end )

    result = sort(arr, 0, (len(arr)))
    return result


# my code for easy quick sort (not in place)
def quick_sort_using_arrays(input_array):
    # end case
    if len(input_array) <= 1:
        return input_array

    pivot =  input_array.pop()
    left = []
    right = []

    for item in input_array:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)

    return quick_sort_using_arrays(left) + [pivot] + quick_sort_using_arrays(right)



# the below is not my work.. just a copy of someone elses so i can test for speed
# mine is much quicker..
def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high

def quick_sort1(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort1(array, start, p-1)
    quick_sort1(array, p+1, end)


# run tests
#  if __name__ == '__main__':
    #  arr = [2,5,1,6,0,22,1,3]
    #  quick_sort1(arr, 0, len(arr)-1)
    #  print(arr)
