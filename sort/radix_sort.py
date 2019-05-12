"""
radix sort
complexity: O(nk + n) . n is the size of input list and k is the digit length
of the number
"""


def radix_sort(arr: list, simulation=False):
    position = 1
    max_number = max(arr)

    iteration = 0
    if simulation:
        print("iteration", iteration, ":", *arr)

    while position < max_number:
        queue_list = [list() for _ in range(10)]

        for num in arr:
            digit_number = num // position % 10
            queue_list[digit_number].append(num)

        index = 0
        for numbers in queue_list:
            for num in numbers:
                arr[index] = num
                index += 1

        if simulation:
            iteration = iteration + 1
            print("iteration", iteration, ":", *arr)

        position *= 10
    return arr


if __name__ == '__main__':
    import random

    lst = random.sample(range(10 ** 4), k=10 ** 1)
    lst_sorted = radix_sort(lst, simulation=True)
    print(all(
        map(lambda x: x[0] <= x[1],
            zip(lst_sorted[:-1],
                lst_sorted[1:]
                )
            )
    )
    )
