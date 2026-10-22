# L =list(range(1,11))
# print(L)
# L = []
# for x in range(1,11):
#     L.append(x*x)
# print(L)
# L = [x * x for x in range(1,11)]
# print(L)
# L = [x * x for x in range(1,11) if x % 2 == 0]
# print(L)
# L = [m + n for m in 'ABC' for n in 'XYZ']
# print(L)
# import os
# L = [d for d in os.listdir('.')]
# print(L)
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# a =[k + '=' + v for k, v in d.items()]
# print(a)
# L = ['Hello','World', 'IBM', 'Apple']
# a = [s.lower() for s in L]
# print(a)
# L = [x for x in range(1,11) if x % 2 == 0 else 0]
# print(L)
L1 = ['Hello', 'World', 18, 'Apple',None]
L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)
if L2 == ['hello','world','apple']:
    print('测试通过!')
else:
    print('测试失败!')