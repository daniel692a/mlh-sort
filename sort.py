def sort_array(array):
    length = len(array)
    for i in range(length-1):
        for j in range(length-i-1):
            if array[j] < array[j+1]:
                flag = array[j]
                array[j] = array[j+1]
                array[j+1] = flag
    return array

def main():
    print(sort_array([9, 78.6, 100.6, 4, 0.6]))

if __name__ == '__main__':
    main()