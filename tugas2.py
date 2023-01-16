import os 
os.system('cls')

data = ['daiva', 'zaki', ['wahyu', 'zaki'], 'shafa', ['zaki', 'aji', 'wahyu'], 'zaki']
def jumpSearch(arr, x):

	n = len(arr)

	step = int(n ** 0.5)

	# Mencari block yang berisi elemen x (input)
	start = 0
	
	while arr[min(step, n) - 1] < x:
		start = step
		step += int(n ** 0.5)
		if start >= n:
			return -1

	# Melakukan linearing di block tersebut
	while arr[start] < x:
		start += 1

		if start == n:
			return -1

	# Cek apakah elemen yang dicari adalah elemen yang sesuai 
	if arr[start] == x:
		return start

	return -1

print(data)

x = 'zaki'
result = jumpSearch(data, x)
if result == -1:
	print(f"Elemen {x} tidak ditemukan")
else:
	print(f"{x} berada di array index ke - {result}")


for i in data:

	if isinstance(i, list):

		result = jumpSearch(i, x)
		if result == -1:
			print(f"Elemen {x} tidak ditemukan")
		else:
			print(f"{x} berada di array index ke - {result} kolom ke {data.index(i)}")



