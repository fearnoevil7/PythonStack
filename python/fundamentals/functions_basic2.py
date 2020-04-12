# def countdown(num):
#     array = []
#     for i in range (num, -1, -1):
#         array.append(i)
#     return array

# b = countdown(5) 
# print(b)

# def print_and_return(array):
#     for i in range(0, len(array), 1):
#         print(array[i])
#         if i == 2:
#             return (array[i])

# b = print_and_return([7, 2])
# print(b)

# def first_plus_length(array):
#     for i in range(len(array)):
#         if i == 0:
#             array[i] += len(array)
#             return array[i]

# b = first_plus_length([1, 2, 3, 4, 5])
# print(b)

# def greater_than_second(array):
#     count = 0
#     newarray = []
#     for i in range(len(array)):
#         if array[i] > array[1]:
#             newarray.append(array[i])
#             count += 1
#         if len(array) == 2:
#             return "false"
#     print(count)
#     return newarray

# b = greater_than_second([5, 2, 3, 2, 1, 4])
# print(b)

# def dis_length_dat_value(a,b):
#     for i in range(0, a , 1):
#         print(b)

# d = dis_length_dat_value(6, 2)
# print(d)
