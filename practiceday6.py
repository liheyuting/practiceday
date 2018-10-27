#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/24 下午11:10
# @Author  : Dora
# @File    : practiceday6.py

# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

l = []
a = 0
b = 1

while a < 100000:
    c = a + b
    b = a
    a = c
    l.append(a)

print(l)


#参考答案

#方法一
#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
	return a

# 输出了第10个斐波那契数列
print(fib(10))


#方法二
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 使用递归
def fib(n):
	if n==1 or n==2:
		return 1
	return fib(n-1)+fib(n-2)

# 输出了第10个斐波那契数列
print (fib(10))

#方法三
#如果你需要输出指定个数的斐波那契数列，可以使用以下代码：

#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出前 10 个斐波那契数列
print (fib(10) )
