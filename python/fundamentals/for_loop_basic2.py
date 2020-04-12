# def biggie_size(array):
#     for i in range(len(array)):
#         if array[i] > 0:
#             array[i] = "big"
#     return array

# b = biggie_size([-1, 3, 5, -5])
# print(b)

# def count_positives(arr):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             count += 1
#         if i == len(arr) -1:
#             arr[i] = count
#     return arr

# b = count_positives([-1, 1, 1, 1])
# print(b)

# def sum_total(arr):
#     sum = 0
#     for i in range(len(arr)):
#         sum += arr[i]
#     return sum

# a = sum_total([6, 3, -2])
# print(a)

# def average(array):
#     sum = 0
#     for i in range(len(array)):
#         sum += array[i]
#     average = sum / len(array)
#     return average

# c = average([1, 2, 3, 4])
# print(c)

# def minimum(arr):
#     min = 0
#     for i in range(len(arr)):
#         if len(arr) == 0:
#             return False
#         if arr[i] < min:
#             min = arr[i]
#     return min

# b = minimum([-3, 4])
# print(b)

# def maximum(arr):
#     max = 0
#     for i in range(len(arr)):
#         if len(arr) == 0:
#             return False
#         if arr[i] > max:
#             max = arr[i]
#     return max

# a = maximum([])

# print(a)

# def ultimate_analysis(array):
#     sum = 0
#     min = 0
#     max = 0
#     size = len(array)
#     for i in range(len(array)):
#         if array[i] > max:
#             max = array[i]
#         if array[i] < min:
#             min = array[i]
#         sum += array[i]
#     avg = sum / len(array)
#     ditcionary = {'sumTotal': sum, 'average': avg, 'minimum': min, 'maximum': max, 'length': len(array)}
#     return ditcionary

# z = ultimate_analysis([37, 2, 1, -9])
# print(z)

# def reverse_list(array):
#     temp = 0
#     for i in range(0, int(len(array) / 2), 1):
#         temp = array[i]
#         array[i] = array[len(array) - 1 - i]
#         array[len(array) - 1- i] = temp
#     return array

# b = reverse_list([37, 2, 1, -9])
# print(b)
