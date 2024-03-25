from timeit import timeit

import bubble_sort
import selection_sort
import insertion_sort
import quick_sort
import merge_sort

array_to_sort = [5, 4, 3, 2, 1, 10, 6, 34, 8, 7, 13]

# n = int(input("Enter total number of inputs: "))
#
# for k in range(n):
#     array_to_sort.append(input(f"Enter array value {k}: "))

print("\nUnsorted Array: ")
for i in range(len(array_to_sort)):
    print(array_to_sort[i], end=", ")

output_bubble_sort = bubble_sort.bubble_sort(array_to_sort)
end_bubble_sort = timeit()

output_selection_sort = selection_sort.selection_sort(array_to_sort)
end_selection_sort = timeit()

output_insertion_sort = insertion_sort.insertion_sort(array_to_sort)
end_insertion_sort = timeit()

output_quick_sort = quick_sort.quick_sort(array_to_sort)
end_quick_sort = timeit()

output_merge_sort = merge_sort.merge_sort(array_to_sort)
end_merge_sort = timeit()


print("\n\nSorted by bubble sort: ")
for i in range(len(output_bubble_sort)):
    print(output_bubble_sort[i], end=", ")

print(f"\n\nTotal Steps: {bubble_sort.step_count}")
print(f"Time taken: {end_bubble_sort}")

print("\nSorted by selection sort: ")
for i in range(len(output_selection_sort)):
    print(output_selection_sort[i], end=", ")

print(f"\n\nTotal Steps: {selection_sort.step_count}")
print(f"Time taken: {end_selection_sort}")


print("\nSorted by insertion sort: ")
for i in range(len(output_insertion_sort)):
    print(output_insertion_sort[i], end=", ")

print(f"\n\nTotal Steps: {insertion_sort.step_count}")
print(f"Time taken: {end_insertion_sort}")


print("\nSorted by quick sort: ")
for i in range(len(output_quick_sort)):
    print(output_quick_sort[i], end=", ")

print(f"\n\nTotal Steps: {quick_sort.step_count}")
print(f"Time taken: {end_quick_sort}")

print("\nSorted by merge sort: ")
for i in range(len(output_merge_sort)):
    print(output_merge_sort[i], end=", ")

print(f"\n\nTotal Steps: {merge_sort.step_count}")
print(f"Time taken: {end_merge_sort}")