import numpy.random as npr


def sort(input_list):
    length = len(input_list)
    if length <= 1:
        return input_list
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if input_list[i-1] > input_list[i]:
                swap = input_list[i]
                input_list[i] = input_list[i-1]
                input_list[i-1] = swap
                swapped = True
        length -= 1
    return input_list


def test_sort():
    unsorted = npr.randint(0, 1000, 10)
    sorted = sort(unsorted)
    print(sorted)
    assert len(sorted) == len(unsorted)
    count = 0
    for i in sorted:
        assert i in unsorted
        if count >= 1:
            assert sorted[count] >= sorted[count-1]
        count += 1


if __name__ == '__main__':
    unsorted = npr.randint(0, 1000, 10)
    # print(unsorted)
    print(sort(unsorted))
