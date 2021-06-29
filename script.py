from icecream import ic


def sort_list(array):
    length = len(array)
    for i in range(0, length-1):
        is_swap = False
        for j in range(0, length-i-1):
            if array[j] > array[j+1]:
                flag = array[j]
                array[j] = array[j+1]
                array[j+1] = flag
                is_swap = True
                if is_swap == False:
                    break
    ic(array)

def main():
    sort_list([60, 50, 95, 80, 70])
    sort_list([6, 8, 1, 7])

if __name__ == '__main__':
    main()