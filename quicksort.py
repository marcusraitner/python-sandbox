import numpy.random as npr


def quicksort(input_list):
    if len(input_list) <= 1:
        print("Rekursionsende")
        return input_list
    else:
        # get random pivot element
        length = len(input_list)
        rnd = npr.randint(0, length-1)
        pivot = input_list[rnd]
        lower = []
        higher = []
        for i in input_list:
            if i < pivot:
                lower.append(i)
            elif i > pivot:
                higher.append(i)
        # print(lower, "//", higher)
        return quicksort(lower) + [pivot] + quicksort(higher)


if __name__ == '__main__':
    unsorted = npr.randint(0, 100000, 100)
    # print(unsorted)
    print(quicksort(unsorted))
