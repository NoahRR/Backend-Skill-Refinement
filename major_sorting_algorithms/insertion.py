def insertion_sort(input_array):

    # iterate through array
    for i in range(1, len(input_array)):

        # iterate backwards to start of array
        for j in range(i, 0, -1):

            # bubble-like
            if input_array[j] < input_array[j-1]:
                input_array[j], input_array[j-1] = input_array[j-1], input_array[j]
            else:
                break

    return input_array
