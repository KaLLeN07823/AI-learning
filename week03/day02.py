# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# for ch in 'ABC':
#      print(ch)
# from collections.abc import Iterable
# b = isinstance('abc',Iterable)
# print(b)
# a = isinstance([1,2,3],Iterable)
# print(a)
# c = isinstance(123,Iterable)
# print(c)
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i,value)
# for x, y in [(1, 1), (2,4), (3,9)]:
#     print(x,y)
# def findMinAndMax(L):
#     if not L:
#         return(None,None)
#     min = L[0]
#     max = L[0]
#     for i in L:
#             if max < i:
#                 max = i
#             if min > i:
#                 min = i
#     return(min,max)
#     # a = []
#     # if not L:
#     #     return(None,None)
#     # else:
#     #     for i in L:
#     #         a.append(i)
#     # return(min(a),max(a))
# if findMinAndMax([]) != (None,None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7,7):
#     print('测试失败!')
# elif findMinAndMax([7,1]) != (1,7):
#     print('测试失败!')
# elif findMinAndMax([7,1,3,9,5]) !=(1,9):
#     print('测试失败!')
# else:
#     print('测试成功!')
# L = [2,3,7,9,10]
# print(findMinAndMax(L))