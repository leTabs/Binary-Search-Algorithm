# the Binary Search Algorithm

def binary_search(arr, target):
    starting_index = 0
    ending_index = len(arr) - 1
    if target not in arr:
        return (f'The target "{target}" is not in the array')
        # informs the user if the target is stored in the array
    while True:
        # while loop so that we have as many iterations as needed
        middle_index = (starting_index + ending_index) // 2
        # calculate the middle index of the array at the beggining of each iteration

        if target < arr[middle_index]:
            ending_index = middle_index - 1
            # if the condition is true then the array is sliced and the right half is discarded

        if target > arr[middle_index]:
            starting_index = middle_index + 1
            # if the condition is true then the array is sliced and the left half is discarded

        if target == arr[middle_index]:
            # the iterations keep hapening until this condition is true
            return middle_index
            # the desired index is being return and the function terminates


array_00 = [1, 3, 4, 7, 8, 9, 11, 15, 17, 20]
array_01 = ["apple", "banana", "cherry", "grape", "kiwi", "orange", "pear", "pineapple"]
print(binary_search(array_00, 11))
print(binary_search(array_01, 'kiwi'))
# note: the array must be sorted in order for the binary search algorithm to work...
array_02 = sorted([4,6,1,8,9])
print(binary_search(array_02, 8))
