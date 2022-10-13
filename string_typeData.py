from array import array


def sortData(array):
    # hitung panjang array
    n = len(array)
    # perulangan pertama
    for i in range(n):
        # perulangan kedua
        for j in range(n-i-1):
            # perbandingan
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    print(array)
    return array
sortData([4,5,3,5,7,1,3,5,0,11,22,21,12,44,33,5,6,5,4])