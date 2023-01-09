my_arr = [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
print(f'list lama : {my_arr}')

# variable untuk menampung list baru
new_arr = []

# Melakukan quicksorting pada setiap partisi yang telah dibagi
def partition(l, bwh, atas): 
    # print("List : ",l,"\n")
    pivot = l[atas]
    index = bwh
    current = bwh
    while (current < atas) :
        if l[current] <= pivot:
            l[index],l[current]=l[current],l[index] #Swapping antara value[index] dan value[current]
            index += 1
        current += 1
    l[index],l[atas] = l[atas],l[index] #Swapping antara value[pivot] dan value[index]
    # print("Partisi : ",l,"\n")
    return index

# Melakukan pembagian partisi
def quicksort(l, bwh, atas): 
  if bwh < atas:
    index = partition(l, bwh, atas) #mendapatkan index untuk membagi partisi
    quicksort(l, bwh, index-1) #quicksorting partisi kiri (lebih kecil dari pivot)
    quicksort(l, index+1, atas) #quicksorting partisi kanan (lebih besar dari pivot)
    return l

# mengiterasi item dalam my_arr untuk diubah menjadi 1D list, ditampung ke new_arr
for i in my_arr:

    if isinstance(i, int):
        new_arr.append(i)

    elif isinstance(i, list):

        for j in i:
            if isinstance(j, list):

                # cara baru menggabungkan list dengan list menggunakan * (Python 3.6+)
                new_arr = [*new_arr, *j]

            else:
                new_arr.append(j)
       
akhir = quicksort(new_arr, 0, len(new_arr)-1)
print("Setelah disort : ",akhir)
