def snail(snail_map):

    for i in range(len(snail_map)):
        print(snail_map[i])

    output = []
    line_length = len(snail_map) 
    h_pointer = 0 # horizontal
    v_pointer = 0 # vertical
    alternating = False

    if snail_map == [[]]:
        return []
    if len(snail_map) == 1:
        return snail_map[0]

    # add the first line
    while h_pointer < line_length:
        output.append(snail_map[0][h_pointer])
        h_pointer += 1
    h_pointer -= 1
    v_pointer += 1
    line_length -= 1

    # loop to add rest of snail map
    while line_length > 0:

            # DOWN
            for i in range(line_length):
                output.append(snail_map[v_pointer][h_pointer])
                v_pointer += 1
            v_pointer -= 1
            h_pointer -= 1


            # LEFT
            for i in range(line_length):
                output.append(snail_map[v_pointer][h_pointer])
                h_pointer -= 1
            h_pointer += 1
            v_pointer -= 1

            # update line length
            line_length -= 1
            if line_length < 1:
                break

            # UP
            for i in range(line_length):
                output.append(snail_map[v_pointer][h_pointer])
                v_pointer -= 1
            v_pointer += 1
            h_pointer += 1

            # RIGHT
            for i in range(line_length):
                output.append(snail_map[v_pointer][h_pointer])
                h_pointer += 1
            h_pointer -= 1
            v_pointer += 1

            # update line length
            line_length -= 1

    return output

