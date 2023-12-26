# class Person:
#     # data
#     gender = 'female'
#     age = 20
#     skin_color = 'navy'
#     weight = 93.1
#     name = 'koki'
#     # functionality
#
#
# # class Human:
# #     # data
# #     # functionality
# #     pass
#
#
# # h= Human()
# p1 = Person()
# p2 = Person()
# # # print(type(p2))
# # # print(type(p1))
# # # print(p1)
# # # print(p2)
# # print(p1.name)
# # print(p2.name)
# #
# # p1.name = 'adele'
# #
# # print(p1.name)
# # print(p2.name)
#
# # p1.title = 'Dr'
# #
# # print(p1.title)
# # print(p2.title)
#
# del p1.name
# print(p1.name)


class Person:
    # data
    def __init__(self):
        print(f'haha new object self = {self}')
    # age = 20
    # skin_color = 'navy'
    # weight = 93.1
    # name = 'koki'
    # functionality


p3 = Person()  # class name ()
p4 = Person()

print(p3)
print(p4)