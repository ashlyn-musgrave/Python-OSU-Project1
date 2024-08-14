def count_sort(StaticArray) -> StaticArray:
    '''
    Receives a StaticArray and returns a new StaticArray with the same content sorted in non-ascending order
    '''

    # Find the minimum and maximum values in the array to determine the range
    min_val, max_val = StaticArray[0], StaticArray[0]

    for i in range(StaticArray.length()):
        value = StaticArray[i]
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    # Create a count array to store the frequency of each value within the range
    count = StaticArray(max_val - min_val + 1)

    for i in range(StaticArray.length()):
        value = StaticArray[i]
        count[value - min_val] += 1

    # Create a new StaticArray to store the sorted values
    sorted_array = StaticArray(StaticArray.length())

    index = 0
    for i in range(max_val, min_val - 1, -1):
        while count[i - min_val] > 0:
            sorted_array[index] = i
            count[i - min_val] -= 1
            index += 1

    return sorted_array