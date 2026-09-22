# def power(x):
#     return x * x
# n = 5
# print(power(n))
# s = 15
# print(power(s))
# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# a = 5
# b = 3
# print(power(a,b))
# c = 5
# d = 2
# print(power(c,d))
# def power(x,n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# a = 5
# print(power(a))
# def enroll (name,gender, age =7,city='Zhongshan'):
#     print('name:', name)
#     print('gender:',gender)
#     print('age:',age)
#     print('city:',city)
# name = input("请输入名字:")
# gender = input("请输入性别:")
# enroll(name,gender)
# enroll('Bob','M',7)
# enroll('Adam','M',city='Tianjin')
# def add_end(L=[]):
#     L.append('END')
#     return L
# L = [1,2,3]
# print(add_end())
# def add_end(L=None):
#     if L is None:
#         L = []
#     L.append('END')a
#     return L
# print(add_end())
# print(add_end())
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# t = (1,3,5,7)
# l = [1,2,3]
# print(calc(l))
# print(calc(t))
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# # print(calc(1,2,3))
# # print(calc(1,3,5,7))
# # print(calc())
# nums = [1,2,3]
# # print(calc(nums[0],nums[1],nums[2]))
# print(calc(*nums))
#
# def person(name,age, **kw):
# #     print('name:', name,'age:',age,'other:',kw)
# # person('Michael', 30)
# # person('Bob',35, city='Beijing')
# # person('Adam',45, gender='M',job='Engineer')
# # extra = {'city': 'Beijing','job':'Engineer'}
# # person('Jack',24,**extra)
# def person(name, age, **kw):
#     if 'city' in kw:
#         pass
#     if 'job' in kw:
#         pass
#     print('name:',name,'age:',age,'other:',kw)
# person('Jack', 24, city='Beijing',addr='Chaoyang',zipcode=123456)
# def person(name,age,*, city,job):
#     print(name,age,city,job)
# person('Jack', 24, city='Beijing',job='Engineer')
# def person(name,age, *args,city,job):
#     print(name,age,args,city,job)
# person('Jack',24, 'Beijing','Engineer')
# def person(name,age,*, city='Beijing',job):
#     print(name,age,city,job)
# person('Jack',24,job='Engineer')
# def f1(a,b,c=0, *args, **kw):
#     print('a =',a, 'b=', b, 'c=',c,'args=',args, 'kw =',kw)
# def f2(a,b,c=0,*,d, **kw):
#     print('a=', a, 'b=',b,'c=',c,'d=',d,'kw =',kw)
# # f1(1,2)
# # f1(1,2, c=3)
# # f1(1,2,3,'a','b')
# # f1(1,2,3,'a','b',x=99)
# # f2(1,2, d=99,ext=None)
# args =(1,2,3,4)
# kw = {'d': 99,'x': '#'}
# f1(*args, **kw)
# args = (1,2,3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)
import math
def mul(*numbers):
    if len(numbers) == 0:
        raise TypeError('至少输入一个数字')
    result=1
    for n in numbers:
        result = result * n
    return result
print('mul(5) =',mul(5))
print('mul(5,6) =', mul(5,6))
print('mul(5,6,7) =', mul(5,6,7))
print('mul(5,6,7,9) =', mul(5,6,7,9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5,6) != 30:
    print('mul(5,6)测试失败!')
elif mul(5,6,7) != 210:
    print('mul(5,6,7)测试失败!')
elif mul(5,6,7,9) != 1890:
    print('mul(5,6,7,9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')