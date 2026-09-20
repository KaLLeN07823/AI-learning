# n1 = 255
# n2 = 1000
# h = hex
# # new_n1 =h(n1)
# # new_n2 =h(n2)
# # print(f"{new_n1}\n{new_n2}")
# print(h(n1))
# print(h(n2))
# def my_abs(x):
#     if not isinstance(x,(int,float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(100))
# def nop()
#     pass
# if age >= 18:
#     pass
# import math
# def move(x,y,step,angle=0):
#     nx = x+step * math.cos(angle)
#     ny = y-step * math.sin(angle)
#     return nx, ny
import math
def quadratic(a,b,c):
    delta = b*b-4*a*c
    if delta <0:
        return "无实数解"
    elif delta ==0:
        return -b/(2*a)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        return x1,x2
a=3
b=4
c=5
print(quadratic(a,b,c))

# import math
# def quadratic(a,b,c):
#     pass
# print('quadratic(2,3,1) =', quadratic(2,3,1))
# print('quadratic(1,3,-4) =', quadratic(1,3,-4))
# if quadratic(2,3,1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1,3,-4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')