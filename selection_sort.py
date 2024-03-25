step_count = 0

def selection_sort(input_array):
    count = 0
    global step_count

    for i in range(len(input_array)):

        index = count
        smallest_int = input_array[index]

        for j in range(count, len(input_array)):
            step_count += 1
            if smallest_int < input_array[j]:
                pass
            else:
                smallest_int = input_array[j]
                index = j

        input_array[index] = input_array[count]
        input_array[count] = smallest_int

        count += 1

    return input_array

