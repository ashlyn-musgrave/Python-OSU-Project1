def rotate(arr: StaticArray, steps: int) -> StaticArray:
    '''
    Returns a new static array that shifts the position of the elements right (if positive) or left (if negative)
    '''

    size = arr.get_size()
    rotated_arr = StaticArray(size)

    for i in range(size):
        new_index = (i + steps) % size
        rotated_arr.set(new_index, arr.get(i))

    return rotated_arr

