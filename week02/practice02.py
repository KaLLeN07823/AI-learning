# L = [3,7,2,9,5]
# sum = 0
# for x in L:
#     sum = sum + x
# print(sum)


# students = {
#     'Tom': 85,
#     'Jack': 92,
#     'Amy' : 78,
#     'Bob' : 92
# }
# for name,score in students.items():
#     if score >= 90:
#         print(name)
# set(students.values())
# print(set(students.values()))


# scores = [78,92,85,66,95]
# high=max(scores)
# low = min(scores)
# students = len(scores)
# print(f"最高分:{high}")
# print(f"最低分:{low}")
# print(f"学生人数:{students}")


# def greet(name):
#     print(f"Hello, {name}!")
# greet('Tom')
# greet('Amy')


# def calc(a,b,operation):
#     if operation == 'add':
#         print(a+b)
#     else:
#         print(a-b)
# calc(10,5,'add')
# calc(10,5,'sub')


# def average(*numbers):
#     if len(numbers) == 0:
#         raise TypeError('请至少输入一个数字')
#     sum = 0
#     for x in numbers:
#         sum = sum +x
#     length=len(numbers)
#     result = (sum/length)
#     return result
# print(average(10,20,30))


# 9
# scores = [78,92,85,66,95,92,78]
# def analyze_scores(scores):
#     max_score=max(scores)
#     print(f"最高分是:{max_score}")
#     total = 0
#     for x in scores:
#         total = total + x
#     extent = len(scores)
#     average = total/extent
#     print(f"平均分是:{average}")
#     new_scores=set(scores)
#     print(new_scores)
# analyze_scores(scores)
# 9
# students = {
#     'Tom':85,
#     'Jack': 92,
#     'Amy': 78,
#     'Bob': 96
# }
# def check_students(students):
#     for name,score in students.items():
#         if score >=90:
#             print(f"{name}优秀")
#         else:
#             print(f"{name}继续努力")
# check_students(students)
# def find_max(*numbers):
#     if len(numbers) == 0:
#         return"没有数据"
#     biggest = numbers[0]
#     for x in numbers:
#         if x > biggest:
#             biggest = x
#     return biggest
# print(find_max())
# print(find_max(3,7,2,9,5))
# products = {
#     'apple': 5,
#     'banana': 3,
#     'milk' : 8,
#     'bread': 6
# }
# def expensive_products(products):
#     result=[]
#     for name,price in products.items():
#         if price >= 6:
#             result.append(name)
#     return result
# print(expensive_products(products))
# students = {
#     'Tom': 85,
#     'Jack': 92,
#     'Amy' : 78,
#     'Bob' : 96,
#     'Lucy' : 88
# }
# def analyze_students(students):
#     good_students=[]
#     for name,score in students.items():
#         if score >= 90:
#             good_students.append(name)
#     total = 0
#     for x in students.values():
#         total = total + x
#         length = len(students)
#         average = total/length
#     return good_students,average
# good_sutdents, average = analyze_students(students)
# print(good_sutdents)
# print(average)



