step_count = 0
def quick_sort(input_array):
    global step_count

    if len(input_array) <= 1:  # -->exit clause
        return input_array

    pivot = input_array[0]
    left = [x for x in input_array[1:] if x < pivot]
    right = [x for x in input_array[1:] if x >= pivot]
    step_count += 1

    return quick_sort(left) + [pivot] + quick_sort(right)
