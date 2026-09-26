# 可以，我按我们前面实际做题时你 ** 真的卡过 / 写错过的地方 ** 来总结，不按教材目录死背。整体看下来，你的问题不是“完全不会”，而是有几个基础概念偶尔会串线。
#
# 我觉得你现在最值得补的是下面这些：
#
# 1. ** 变量类型容易混 **
# 这是你目前最常见的问题之一。
#
# 你有时候会把
# `list`、`dict`、字符串的方法混着用，比如刚才：
#
# ```python
# scores = [78, 92, 85]
# set(scores.values())  # ❌
# ```
#
# `scores`
# 是列表，没有
# `.values()
# `。
#
# 而字典：
#
# ```python
# students = {'Tom': 85}
# students.values()  # ✅
# students.items()  # ✅
# ```
#
# 建议你以后看到变量，先在脑子里问一句：
#
# > ** “这个东西现在是什么类型？” **
#
# `list / tuple / dict / set / str / int`
# 分清，很多错误自然就没了。
#
# 2. ** 缩进会直接改变程序逻辑 **
#
# 你不是不会
# ` if ` 和 `
# for `，而是有时候缩进一错，整个意思就变了。
#
# 比如找最大值：
#
# ```python
# biggest = numbers[0]
#
# for x in numbers:
#     if x > biggest:
#         biggest = x
#
# return biggest
# ```
#
# 你之前把：
#
# ```python
# biggest = numbers[0]
# ```
#
# 放进
# `
# for ` 里面，就导致它每次循环都重新初始化。
#
# 所以你以后看代码可以专门注意：
#
# ```text
# 谁在循环里面？
# 谁在 if 里面？
# 谁应该只执行一次？
# ```
#
# 3. ** `
# return ` 的意义还需要彻底形成直觉 **
#
# 这是函数章节你最明显的一个易错点。
#
# 你之前写：
#
# ```python
# return good_students
#
# total = 0
# for x in students.values():
#     ...
# ```
#
# 但
# `
# return ` 一执行：
#
# > ** 函数立刻结束。 **
#
# 后面的代码根本不会执行。
#
# 以后可以直接记：
#
# ```text
# print = 打印给我看
# return = 把结果交出去，并结束函数
# ```
#
# 一般先把函数里的事情全部做完，再
# `
# return `。
#
# 4. ** `
# for ` 循环不需要你提前知道次数 **
#
#     这个你刚才问了好几轮，值得专门巩固。
#
#     ```python
#     for x in numbers:
#         ```
#
#     意思不是“循环固定几次”，而是：
#
#     > `numbers`
#     里面有几个东西，就自动拿几个。
#
#     所以：
#
#     ```python
#     numbers = (2, 5, 8)
#     ```
#
#     自动
#     3
#     次；
#
#     ```python
#     numbers = (2, 5, 8, 9, 10, 20)
#     ```
#
#     自动
#     6
#     次。
#
#     ** 遍历 ≠ print。 **
#
#     ```python
#     for name, score in students.items():
#         ```
#
#     这一句本身就已经是在遍历了。
#
#     5. ** 容器的几个常用操作容易忘 **
#
#     这几个最好练到条件反射：
#
#     ```python
#     dict.items()  # key 和 value
#     dict.keys()  # key
#     dict.values()  # value
#
#     set(data)  # 去重
#
#     L.append(x)  # 往列表加入一个完整元素
#     len(L)  # 长度
#     ```
#
#     特别是你刚刚犯过：
#
#     ```python
#     result += name
#     ```
#
#     当
#     `name = "milk"
#     ` 时可能会拆成字符。
#
#     而：
#
#     ```python
#     result.append(name)
#     ```
#
#     才是把
#     `"milk"`
#     整个放进去。
#
#     6. ** 函数参数这一块基本懂了，但容易忘每种参数到底收到什么 **
#
#     普通参数：
#
#     ```python
#
#
#     def greet(name):
#         ```
#
#
#     一个变量接一个参数。
#
#     `*numbers`：
#
#     ```python
#
#
#     def average(*numbers):
#         ```
#
#
#     会把任意数量的位置参数收成一个 ** tuple **：
#
#     ```python
#     average(10, 20, 30)
#
#     numbers == (10, 20, 30)
#     ```
#
#     你之前还学到了
#     ` ** kwargs
#     `，它收的是：
#
#     ```python
#     key = value
#     ```
#
#     形式的参数，最后是一个
#     `dict`。
#
#     这里以后很容易考混：
#
#     ```python
#     *args      → tuple
#     ** kwargs   → dict
#     ```
#
# 7. ** 字符串、数字转换偶尔会混 **
#
# 你前面练习过：
#
# ```python
# age = input()
# ```
#
# `input()`
# 得到的默认是 ** 字符串 **。
#
# 如果要算：
#
# ```python
# age = int(input())
# ```
#
# 才变成整数。
#
# 而
# f - string：
#
# ```python
# print(f"年龄是 {age}")
# ```
#
# 能自动帮你把数字显示进字符串里，所以这里不需要手动转换成字符串。
#
# 8. ** 基础语法不是不会，而是容易忘“工具叫什么” **
#
# 这个其实非常明显，比如你做
# `dict`
# 题没有思路，后来发现只是忘了：
#
# ```python
# .items()
# ```
#
# 一提醒你马上就能往下写。
#
# 类似的还有：
#
# ```python
# max()
# min()
# len()
# append()
# set()
# int()
# ```
#
# 所以你目前其实不用疯狂学新语法，更应该做一些 ** 不告诉你该用哪个函数的综合题 **，逼自己从脑子里把工具调出来。
#
# 如果让我给你现在的薄弱点排一下优先级，我会放成：
#
# ** ① 类型判断 → ② 缩进 / 代码执行顺序 → ③ return → ④ for 遍历 → ⑤ 常用 list / dict 方法 → ⑥ 函数参数。 **
#
# 反而
# ` if / elif / else `、基本
# `
# for `、f-string、定义函数这些，你现在已经不算薄弱了。
#
# 下一次复习我建议不再给你“练
# `.items()
# `”这种明牌题，而是给你 ** 5
# 道诊断题，不告诉你该用哪个知识点 **。这样很容易看出上面这些坑到底补上没有。