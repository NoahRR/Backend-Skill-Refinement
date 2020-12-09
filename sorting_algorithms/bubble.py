def bubble_sort(input_array):

    # iterate through input
    for i in range(len(input_array)):
        for j in range(1, len(input_array)):

            # swap if not in correct order
            if input_array[j-1] > input_array[j]:
                input_array[j-1], input_array[j] = input_array[j], input_array[j-1]

    return input_array
