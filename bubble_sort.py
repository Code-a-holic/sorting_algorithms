step_count = 0
def bubble_sort(array_input):
    global step_count

    for i in range(len(array_input)):
        for j in range(len(array_input)-1):
            #print(array_input)
            if array_input[j] > array_input[j+1]:
                temp = array_input[j+1]
                array_input[j+1] = array_input[j]
                array_input[j] = temp
            step_count += 1
    return array_input

