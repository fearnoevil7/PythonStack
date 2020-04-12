#1
# def a():
#     return 5
# print(a())

# my prediction = 5
# correct

#2
# def a():
#     return 5
# print(a()+a())

# my prediction = 10
# correct

#3
# def a():
#     return 5
#     return 10
# print(a())

# my prediction 5
# correct

#4
# def a():
#     return 5
#     print(10)
# print(a())

# my prediction 5
# correct

#5
# def a():
#     print(5)
# x = a()
# print(x)

# my prediction 5, 5
# actual answer = 5, none

# #6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))

# my prediction 3, 5, 8
# actual answer = 3, 5


#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

# my prediction = 7
# actual answer = 25

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

# my predition = 100, 10, 7
# actual answer = 100, 10

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

# my prediction = 7, 14, 21
# correct

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

# my prediction = 8
# correct

# #11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

# my prediction = 500, 500, 300, 500
# correct

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

# my prediction = 500, 500, 300, 500
# correct

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# # b=a()
# print(b)

# my prediction = 500, 500, 300
# actual answer = 500, 500, 300, 300

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

# my prediction = undefined
# correct

#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

# my prediction = 1, 3, 10
# actual answer = 1, 3, 5, 10