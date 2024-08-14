# Name: Ashlyn Musgrave
# Course: CS261 - Data Structures
# Assignment: Assignment 1 : Python Fundamentals Review
# Due Date: October 23, 2023
# Description: This assignment consists of 10 individual problems that need to be solved using Python


import random
from static_array import *

# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr) -> tuple[int, int]:
    '''
    Returns a tuple with two values, the min and max of the input array
    '''

    # Set the initial min and max equal to the array at index of 0
    min_value = arr[0]
    max_value = arr[0]

    # Iterate through the elements of the array by their indices
    for index in range(arr.length()):
        num = arr[index]

        # If the num is < or > than the min or max value, it becomes the new min or max value
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num

    # Return a tuple with the minimum and maximum values
    return (min_value, max_value)

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(static_array) -> StaticArray:
    '''
    Returns the words: fizzbuzz, fizz, and buzz based on the user's input array using the parameters below
    '''

    # Find the length of the static_array function using the length function
    n = static_array.length()

    # Create a new array containing the same number of elements (n) as static_array
    result = StaticArray(n)

    # Iterate through static_array by checking each number and updating the result with the appropriate value
    for i in range(n):
        num = static_array[i]
        if num % 3 == 0 and num % 5 == 0:
            result[i] = 'fizzbuzz'
        elif num % 3 == 0:
            result[i] = 'fizz'
        elif num % 5 == 0:
            result[i] = 'buzz'
        else:
            result[i] = num

    return result

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(static_array) -> None:
    '''
    Returns the reverse order of the elements given in the array in-place (it directly modifies the input)
    '''

    #Initialize the left and right pointers
    # Set to 0 as the leftmost index
    left = 0
    # Take the length of the array and subtract 1 to obtain the rightmost index
    right = static_array.length() - 1

    # Loop continues while left pointer is less than the right pointer
    while left < right:
        # Reverse order by swapping elements at the left and right pointers
        static_array[left], static_array[right] = static_array[right], static_array[left]
        # After swapping, left pointer is moved one step to the right
        left += 1
        # After swapping, right pointer is moved one step to the left
        right -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(static_array, steps: int) -> StaticArray:
    '''
    Returns a new static array that shifts the position of the elements right (if positive) or left (if negative)
    '''

    # Check that a is within the range of [0, static_array.length()'
    # Reduce the value of steps to an equivalent rotation within the array's bounds
    a = steps % static_array.length()

    # Rotate to the right
    if steps > 0:
        new_array = static_array[-a:] + static_array[:-a]
    # Rotate to the left
    else:
        new_array = static_array[a:] + static_array[:a]

    return new_array

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
def sa_range(start, end) -> StaticArray:
    '''
    Returns a static array that contains the consecutive integers between the given start and end points
    '''

    # Case handling where the start is greater than end
    if start > end:
        n = start - end + 1
        result = StaticArray(n)
        for i in range(n):
            result[i] = start - i
    else:
        n = end - start + 1
        result = StaticArray(n)
        for i in range(n):
            result[i] = start + i

    return result

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------
def is_sorted(arr):
    '''
    Returns an integer that describes whether the array is sorted
    '''

    # An array with one or zero elements is considered sorted in ascending order.
    if arr.length() <= 1:
        return 1

    # Initialize flags for ascending and descending order
    ascending = descending = True

    for i in range(1, arr.length()):
        if arr[i] > arr[i - 1]:
            descending = False  # If we find an element greater than the previous, it's not descending
        elif arr[i] < arr[i - 1]:
            ascending = False  # If we find an element less than the previous, it's not ascending

    if ascending and not descending:
        return 1  # Array is sorted in ascending order
    elif descending and not ascending:
        return -1  # Array is sorted in descending order
    else:
        return 0  # Array is not sorted

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
def find_mode(static_array) -> tuple[object, int]:
    '''
    Returns the mode of the array and its frequency
    '''

    # Find the length of the static_array function using the length function
    n = static_array.length()

    current_element = static_array[0]
    current_count = 1
    max_element = current_element
    max_count = current_count

    for i in range(1, n):
        if static_array[i] == current_element:
            current_count += 1
        else:
            if current_count > max_count:
                max_element = current_element
                max_count = current_count
            current_element = static_array[i]
            current_count = 1

    # Check the last element
    if current_count > max_count:
        max_element = current_element
        max_count = current_count

    return max_element, max_count

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(static_array) -> StaticArray:
    '''
    Returns a new StaticArray with all duplicate values removed without modifying the original array
    '''

    # Find the length of the static_array using the length() method
    n = static_array.length()

    # Create a new StaticArray to store the unique values
    unique_values = StaticArray(n)

    # Initialize with the first element
    unique_values[0] = static_array[0]

    # Initialize an index for the unique_values array
    unique_index = 1

    for i in range(1, n):
        if static_array[i] != static_array[i - 1]:
            unique_values[unique_index] = static_array[i]
            unique_index += 1

    # Create a new StaticArray with the correct length.
    return unique_values[:unique_index]

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------
def count_sort(static_array) -> StaticArray:
    '''
    Receives a StaticArray and returns a new StaticArray with the same content sorted in non-ascending order
    '''

    # Find the minimum and maximum values in the array to determine the range
    min_val, max_val = static_array[0], static_array[0]

    for i in range(static_array.length()):
        value = static_array[i]
        if value < min_val:
            min_val = value
        if value > max_val:
            max_val = value

    # Create a count array to store the frequency of each value within the range
    count = StaticArray(max_val - min_val + 1)

    for i in range(static_array.length()):
        value = static_array[i]
        count[value - min_val] += 1

    # Create a new StaticArray to store the sorted values
    sorted_array = StaticArray(static_array.length())

    index = 0
    for i in range(max_val, min_val - 1, -1):
        while count[i - min_val] > 0:
            sorted_array[index] = i
            count[i - min_val] -= 1
            index += 1

    return sorted_array

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(static_array) -> StaticArray:
    '''
    Returns a new StaticArray with squares of the values from the original array, sorted in non-descending order
    '''

    n = static_array.length()
    result = StaticArray(n)  # Initialize result as a StaticArray

    left, right = 0, n - 1
    index = n - 1  # Start filling from the end

    while left <= right:
        left_sq = static_array[left] ** 2
        right_sq = static_array[right] ** 2

        if left_sq > right_sq:
            result[index] = left_sq
            left += 1
        else:
            result[index] = right_sq
            right -= 1

        index -= 1

    return result

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
