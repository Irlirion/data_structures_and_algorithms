def merge_sort(arr: list) -> list:
    """
    Merge Sort
    Complexity: O(n log(n))
    """
    # Our recursive base case
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # Perform merge_sort recursively on both halves
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Merge each side together
    return __merge(left, right, arr.copy())


def __merge(left: list, right: list, merged: list) -> list:
    """
    Merge helper
    Complexity: O(n)
    """

    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        # Sort each one and place into the result
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    # Add the left overs if there's any left to the result
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    # Add the left overs if there's any left to the result
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    # Return result
    return merged


if __name__ == '__main__':
    import random

    lst = random.sample(range(10**5), k=10**5)
    lst_sorted = merge_sort(lst)
    print(all(
        map(lambda x: x[0] <= x[1],
            zip(lst_sorted[:-1],
                lst_sorted[1:]
                )
            )
    )
    )
