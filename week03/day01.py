# L = ['Michael','Sarah','Tracy','Bob','Jack']
# # print(L[0],L[1],L[2])
# # r = []
# # n = 3
# # for i in range(n):
# #     r.append(L[i])
# # print(r)
# # print(L[0:3])
# # print(L[:3])
# # print(L[1:3])
# # print(L[-2:])
# # print(L[-2:-1])
# # L = list(range(100))
# # # print(L)
# # print(L[:10])
# # print(L[-10:])
# # print(L[10:20])
# # print(L[:10:2])
# # print(L[::5])
# # print(L[:])
# # T = tuple(range(5))
# # print(T[:3])
# str = 'ABCDEFG'
# print(str[:3])
# print(str[::2])
# s = 'hello'
# print(s[1:])
# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[:-1]
#     return s
# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') !='hello':
#     print('测试失败!')
# elif trim('  hello  ') !='hello':
#     print('测试失败!')
# elif trim(' hello  world') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('   ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')
# strTest='   hello,world  '
# print(trim(strTest))