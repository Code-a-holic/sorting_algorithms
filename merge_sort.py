step_count = 0

def merge_sort(input_array):
    global step_count
    step_count += 1
    if len(input_array) <= 1:
        return input_array

    pivot_index = len(input_array) // 2

    left = input_array[:pivot_index]
    right = input_array[pivot_index:]

    left_element = merge_sort(left)
    right_element = merge_sort(right)

    return sort_the_array(left_element, right_element)

def sort_the_array(left, right):
    global step_count

    step_count += 1

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result