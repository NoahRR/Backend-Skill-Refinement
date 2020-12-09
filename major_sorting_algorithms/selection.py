def selection_sort(input_array):

    # iterate through input
    for i in range(len(input_array)):

        # get lowest value
        min_value = i
        for j in range(i, len(input_array)):
            if input_array[j] < input_array[min_value]:
                min_value = j

        # swap i with min
        input_array[i], input_array[min_value] = input_array[min_value], input_array[i]

    return input_array
