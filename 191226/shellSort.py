def shellSort(input_list):

    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
                print(list)
            input_list[j] = temp
            print(list)

# Reduce the gap for the next element

        gap = gap//2

list = [19,2,31,45,30,11,121,27]

shellSort(list)
print(list)
