def quick_sort(arr: list, simulation=False) -> list:
    """
    Quick sort \n
    Complexity: best O(n log(n), avg O(n log(n), worst O(n^2)
    """

    iteration = 0
    if simulation:
        print("iteration", iteration, ':', *arr)
    arr, _ = __quick_sort_recur(arr, 0, len(arr) - 1, iteration, simulation)
    return arr


def __quick_sort_recur(arr, first, last, iteration, simulation):
    if first < last:
        pos = __partition(arr, first, last)
        # Start our two recursive calls
        if simulation:
            iteration += 1
            print('iteration', iteration, ':', *arr)

        _, iteration = __quick_sort_recur(arr, first, pos - 1, iteration,
                                          simulation)
        _, iteration = __quick_sort_recur(arr, pos + 1, last, iteration,
                                          simulation)

    return arr, iteration


def __partition(arr, first, last):
    wall = first
    for pos in range(first, last):
        if arr[pos] < arr[last]:  # last is the pivot
            arr[pos], arr[wall] = arr[wall], arr[pos]
            wall += 1
    arr[wall], arr[last] = arr[last], arr[wall]
    return wall


if __name__ == '__main__':
    import random

    lst = random.sample(range(10 ** 5), k=10 ** 5)
    lst_sorted = quick_sort(lst)
    print(all(
        map(lambda x: x[0] <= x[1],
            zip(lst_sorted[:-1],
                lst_sorted[1:]
                )
            )
    )
    )
