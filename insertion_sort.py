step_count = 0

def insertion_sort(input_array):
    global step_count

    for i in range(1, len(input_array)):
        for j in range(i):
            if input_array[i] < input_array[j]:
                current_value = input_array.pop(i)
                input_array.insert(j, current_value)
            #print(str(input_array) + f"  i value: {i}, j: {j}")
            step_count += 1
    return input_array

