##环境类操作##
# 添加新的路径到 sys.path
sys.path.append('C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\lib\\site-packages')
import sys
print(sys.path)

import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

#!/usr/bin/python3
 
# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
#计算回车符的个数
变量.count('\n')

print ("Hello, Python!")

if True:
    print ("True")
else:
    print ("False")

    if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
  print ("False")    # 缩进不一致，会导致运行错误

total = item_one + \
        item_two + \
        item_three  #多行语句    
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five'] #多行语句 
    

# 数字类型
int (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
bool (布尔), 如 True。
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j

#!/usr/bin/python3
 
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第六个（不包含第六个）的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
print(str[2:3]) 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

#!/usr/bin/python3
#整个代码片段的作用是让用户在脚本执行过程中停下来，并在按下 Enter 键后退出。
input("\n\n按下 enter 键后退出。")

#Python 可以在同一行中使用多条语句，语句之间使用分号 ;
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

import sys
sys.stdout.write(" hi ")    # hi 前后各有 1 个空格

x="a"
y="b"
# 换行输出
print( x )
print( y )
 
print('---------')

# 不换行输出
name = "John"
age = 30
print("Name:", name, end=" ")
print("Age:", age, end=" ")
print("Gender: Male", end=" ")

import sys  #导入 sys 模块
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

from sys import argv,path  #  导入特定的成员
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

#!/usr/bin/python3

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串

print (counter)
print (miles)
print (name)

a = b = c = 1 #多个变量赋值
a, b, c = 1, 2, "runoob" #多个对象指定多个变量

a, b, c, d = 20, 5.5, True, 4+3j  # type() 函数查询变量对象类型
print(type(a), type(b), type(c), type(d))

a = 111 #用 isinstance 来判断
isinstance(a, int)

class A:
     pass
class B(A):
     pass
isinstance(A(), A)
type(A()) == A 
isinstance(B(), A)
type(B()) == A
#isinstance 和 type 的区别在于：
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。

#Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加，
#True==1、False==0 会返回 True，但可以通过 is 来判断类型。
issubclass(bool, int) 
True==1
False==0
True+1
False+1

var1 = 1
var2 = 10
del var1, var2 #del语句删除单个或多个对象
print(var1) 
print(var2)  

var1 = [1, 2, 3, 4, 5]
var2 = 2
del var1[var2]#删除列表中指定位置（var2=2 第三个）的元素
del var1[3]#删除列表中指定位置（3 第四个）的元素
print(var1) 

var1 = [1, 2, 3, 4, 5]
var1.remove(1)  #删除列表中的特定值1
print(var1)  # 输出：[2, 3, 4, 5]

17%5#取余
2**5#乘方
2//4#除法得整
2/4#除法得浮点数

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])

#Tuple（元组）
tup = (1, 2, 3, 4, 5, 6)
print(tup[0])
print(tup[1:5])
tup[0] = 11  # 修改元组元素的操作是非法的
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
#string、list 和 tuple 都属于 sequence（序列）。

#Set（集合）
#Python 中的集合（Set）是一种无序、可变的数据类型，用于存储唯一的元素。
#集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
parame = {value01,value02,...}
或者
set(value)

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)   # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites :
    print('Runoob 在集合中')
else :
    print('Runoob 不在集合中')


# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

#Dictionary（字典）
#列表是有序的对象集合，字典是无序的对象集合。
#两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
#键(key)必须使用不可变类型。在同一个字典中，键(key)必须是唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
{x: x**2 for x in (2, 4, 6)} #{2: 4, 4: 16, 6: 36}

x = b"hello"
y = x[1:3]  # 切片操作，得到 b"el"
z = x + b"world"  # 拼接操作，得到 b"helloworld"

#隐形转换
num_int = 123
num_flo = 1.23
num_new = num_int + num_flo

print("num_int 数据类型为:",type(num_int))
print("num_flo 数据类型为:",type(num_flo))
print("num_new 值为:",num_new)
print("num_new 数据类型为:",type(num_new))

#显式类型转换
#int() 强制转换为整型：
x = int(1)   # x 输出结果为 1
y = int(2.8) # y 输出结果为 2
z = int("3") # z 输出结果为 3

#float() 强制转换为浮点型：
x = float(1)     # x 输出结果为 1.0
y = float(2.8)   # y 输出结果为 2.8
z = float("3")   # z 输出结果为 3.0
w = float("4.2") # w 输出结果为 4.2

#str() 强制转换为字符串类型：
x = str("s1") # x 输出结果为 's1'
y = str(2)    # y 输出结果为 '2'
z = str(3.0)  # z 输出结果为 '3.0'

#整型和字符串类型进行运算，就可以用强制类型转换来完成：
num_int = 123
num_str = "456"

print("num_int 数据类型为:",type(num_int))
print("类型转换前，num_str 数据类型为:",type(num_str))

num_str = int(num_str)    # 强制转换为整型
print("类型转换后，num_str 数据类型为:",type(num_str))

num_sum = num_int + num_str

print("num_int 与 num_str 相加结果为:",num_sum)
print("sum 数据类型为:",type(num_sum))

#int(x [,base])将x转换为一个整数
#float(x)将x转换到一个浮点数
#complex(real [,imag])创建一个复数
#str(x)将对象 x 转换为字符串
#repr(x)将对象 x 转换为表达式字符串
#eval(str)用来计算在字符串中的有效Python表达式,并返回一个对象
#tuple(s)将序列 s 转换为一个元组
#list(s)将序列 s 转换为一个列表
#set(s)转换为可变集合
#dict(d)创建一个字典。d 必须是一个 (key, value)元组序列。
#frozenset(s)转换为不可变集合
#chr(x)将一个整数转换为一个字符
#ord(x) 将一个字符转换为它的整数值
#hex(x) 将一个整数转换为一个十六进制字符串
#oct(x) 将一个整数转换为一个八进制字符串

a = 21
b = 10
c = 0
 
c = a + b
print ("1 - c 的值为：", c)

#成员运算
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
 
if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")
 
if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")

#身份运算
a = 20
b = 20
 
if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")

#is 与 == 区别：
#is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

a = [1, 2, 3, 4]
b = a[:]
b is a
b == a

#字符串更新
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!')

print('\'Hello, world!\'')  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  # 输出：Hello, world!
                                        #       How are you?

print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
                           # Hello,
                           #  world!

print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a

#更新列表
list = ['Google', 'Runoob', 1997, 2000]

print ("第三个元素为 : ", list[2])
list[2] = 2001
print ("更新后的第三个元素为 : ", list[2])

list1 = ['Google', 'Runoob', 'Taobao']
list1.append('Baidu')
print ("更新后的列表 : ", list1)

#删除列表元素 del 语句
list = ['Google', 'Runoob', 1997, 2000]
print ("原始列表 : ", list)
del list[2]
print ("删除第三个元素 : ", list)

#嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0]
['a', 'b', 'c']
x[0][1]
'b'

#列表比较
#operator.lt(a, b) 与 a < b 相同
#operator.le(a, b) 与 a <= b 相同
#operator.eq(a, b) 与 a == b 相同
#operator.ne(a, b) 与 a != b 相同
#operator.gt(a, b) 与 a > b 相同
#operator.ge(a, b) 与 a >= b 相同。

# 导入 operator 模块
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))

#Python列表函数
len(list)列表元素个数
max(list)返回列表元素最大值
min(list)返回列表元素最小值
list(seq)将元组转换为列表
#Python列表方法
list.append(obj)在列表末尾添加新的对象
list.count(obj)统计某个元素在列表中出现的次数
list.extend(seq)在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)将对象插入列表
list.pop([index=-1])移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)移除列表中某个值的第一个匹配项
list.reverse()反向列表中元素
list.sort( key=None, reverse=False)对原列表进行排序
list.clear()清空列表
list.copy()复制列表

#Python元组
tup1 = (50)
type(tup1)     # 不加逗号，类型为整型
<class 'int'>

tup1 = (50,)
type(tup1)     # 加上逗号，类型为元组
<class 'tuple'>

tup3 = "a", "b", "c", "d"   #  不需要括号也可以
type(tup3)
<class 'tuple'>

#修改元组  元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

#删除元组
#元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
tup = ('Google', 'Runoob', 1997, 2000)
 
print (tup)
del tup
print ("删除后的元组 tup : ")
print (tup)

len(tuple)计算元组元素个数。	
tuple1 = ('Google', 'Runoob', 'Taobao')
len(tuple1)

max(tuple)返回元组中元素最大值。	
tuple2 = ('5', '4', '8')
max(tuple2)


min(tuple)返回元组中元素最小值。	
tuple2 = ('5', '4', '8')
min(tuple2)


tuple(iterable)将可迭代系列转换为元组。	
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')

#字典 键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字。
d = {key1 : value1, key2 : value2, key3 : value3 }

# 使用大括号 {} 来创建空字典
emptyDict = {}

#使用内建函数 dict() 创建字典：
emptyDict = dict()

# 查看字典的数量
print("Length:", len(emptyDict))
 
# 查看类型
print(type(emptyDict))

#访问字典里的值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print ("tinydict['Name']: ", tinydict['Name'])

#修改字典
#向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"  # 添加信息
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

#删除字典元素
#使用 del 语句删除字典元素
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
del tinydict['Name'] # 删除键 'Name'
print ("删除 'Name' 后的字典: ", tinydict)
tinydict.clear()     # 清空字典
del tinydict         # 删除字典

#集合 集合（set）是一个无序的不重复元素序列。
#集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。

parame = {value01,value02,...}
或者
set(value)
#创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

a = set('abracadabra')
b = set('alacazam')
a                                  
{'a', 'r', 'b', 'c', 'd'}
a - b                              # 集合a中包含而集合b中不包含的元素
{'r', 'd', 'b'}
a | b                              # 集合a或b中包含的所有元素
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
a & b                              # 集合a和b中都包含了的元素
{'a', 'c'}
a ^ b                              # 不同时包含于a和b的元素
{'r', 'd', 'b', 'm', 'z', 'l'}

a = {x for x in 'abracadabra' if x not in 'abc'}
a
{'r', 'd'}

#添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset) #{'Taobao', 'Facebook', 'Google', 'Runoob'}

thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({1,3})
print(thisset)#{1, 3, 'Google', 'Taobao', 'Runoob'}
thisset.update([1,4],[5,6])  
print(thisset)#{1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}

#移除元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset) #{'Google', 'Runoob'}

thisset = set(("Google", "Runoob", "Taobao"))
thisset.discard("Facebook")  # 不存在不会发生错误
print(thisset)
{'Taobao', 'Google', 'Runoob'}

#设置随机删除集合中的一个元素
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()
print(x)

#清空集合
thisset = set(("Google", "Runoob", "Taobao"))
thisset.clear()
print(thisset) #set()

#判断元素是否在集合中存在
thisset = set(("Google", "Runoob", "Taobao"))
"Runoob" in thisset #True


var1 = 100
if var1:
    print ("1 - if 表达式条件为 true")
    print (var1)
 
var2 = 0
if var2:
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")

#条件控制

#!/usr/bin/python3
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
### 退出提示
input("点击 enter 键退出")

#操作符
# 使用数字
print(5 > 6)
# 使用变量
x = 5
y = 8
print(x == y)

# 该实例演示了数字猜谜游戏
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

#if 嵌套
# !/usr/bin/python3
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

#match...case语句
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
#输出 HTTP 状态码实例 
#def 用于定义函数，此处定义名为http_error的函数
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=404
print(http_error(mystatus))
#一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开，例如：
#case 401|403|404:
#return "Not allowed"

#循环语句
#while 循环

n= 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))

#无限循环
#通过设置条件表达式永远不为 false 来实现无限循环
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
print ("Good bye!")
#CTRL+C 来退出当前的无限循环。

#while 循环使用 else 语句
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>

#实例 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

flag = 1
while (flag): print ('欢迎访问菜鸟教程!')
print ("Good bye!")

#for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串。
#实例
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

#用于打印字符串中的每个字符
word = 'runoob'
for letter in word:
    print(letter)

#整数范围值可以配合 range() 函数使用：
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

#for...else 
#语句用于在循环结束后执行一段代码。
for item in iterable:
    # 循环主体
   else:
    # 循环结束后执行的代码

#实例 
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#break 语句，break 语句用于跳出当前循环体，不会执行 else 子句：
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

#range() 函数
#如果你需要遍历数字序列，可以使用内置 range() 函数。它会生成数列
#实例
for i in range(5):
    print(i)
#指定区间的值
for i in range(5,9) :
    print(i)
#步长
for i in range(0, 10, 3) :
    print(i)
#负数步长  
for i in range(-10, -100, -30) :
    print(i)
#结合 range() 和 len() 函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
     print(i, a[i])

#range() 函数来创建一个列表
list(range(5))
[0, 1, 2, 3, 4]

#pass 语句
#pass是空语句，是为了保持程序结构的完整性。pass 不做任何事情，一般用做占位语句
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")
#缩进理解
#for letter in 'Runoob': 是循环的开始，它应该在第一层缩进。
#if letter == 'o': 是条件判断语句，它应该在第二层缩进。
#pass 和 print('执行 pass 块') 是 if 语句的代码块，它们应该在第三层缩进。
#print('当前字母 :', letter) 是 for 循环的代码块，它应该在第二层缩进。
#这样，代码的逻辑结构就清晰了：
#对于字符串 'Runoob' 中的每一个字符 letter，首先检查是否等于 'o'。
#如果等于 'o'，则执行 pass 语句和 print('执行 pass 块')。
#无论是否等于 'o'，都会执行 print('当前字母 :', letter)。

#break 和 continue 语句及循环中的 else 子句
#实例 while 中使用 break：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')
# break实例
for letter in 'Runoob':     # 第一个实例
   if letter == 'b':
      break
   print ('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print ('当前变量值为 :', var)
   var = var -1
   if var == 5:
      break
#实例 while 中使用 continue：
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
 
print ("Good bye!")

#continue实例 
for letter in 'Runoob':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print ('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print ('当前变量值 :', var)
print ("Good bye!")

#else 子句
#它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行
#但循环被 break 终止时不执行。
#实例
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
DStr (Date (),'YYYY/MM/DD')&' '&TStr (Time (),'HH:MM:SS')

a=5
isinstance(a,int) #True
a=5;b=4.5
isinstance(a,(int,float)) #True
isinstance(b,(int,float)) #True

#字符串不可修改
#通过str函数转换为字符串
a = 5.6
s=str(a)
print(s)
#日期和时间
from datetime import datetime,date,time
dt=datetime(2011,10,11,10,30,20)
dt.data()
dt.time()
#两个不同的datetime对象会产生一个timedelta对象
dt2=datetime(2010,10,12,10,40,20)
delta=dt2-dt
delta
type(delta)
delta.days
delta.seconds

#range函数 等差整数序列
range(5) #生成0到4的整数序列
range(1,5) #生成1到4的整数序列
range(1,10,2) #生成1到9的奇数序列
range(10,0,-1) #生成10到1的整数序列，步长为-1
#range常用于索引遍历序列
a = [1,2,3,4]
for i in range(len(a)):
    Val=a[i]
    print(Val)
    
#tuple函数 用于将序列转换为元组
tup=tuple("string")
tup

#*rest
#*rest表示可变参数，可以传入0个或多个参数，它会被组装成一个tuple
Values=(1,2,3,4)
a,b,*rest=Values
print(a,b,rest) #1 2 (3, 4)

a,b,*_=Values #*rest可以不用赋值，表示抛弃剩余参数
print(a,b) #1 2

#元组方法
#count() 方法用于统计某个元素在元组中出现的次数
tup=("apple","banana","cherry","apple","cherry")
tup.count("apple") #2
tup.count("grape") #0

#index() 方法用于查找某个元素在元组中首次出现的索引位置
tup=("apple","banana","cherry","apple","cherry")
tup.index("apple") #0
tup.index("banana") #1

#len() 方法用于获取元组的长度
tup=("apple","banana","cherry","apple","cherry")
len(tup) #5

#max() 方法用于获取元组中最大的元素
tup=("apple","banana","cherry","apple","cherry")
max(tup) #cherry

#min() 方法用于获取元组中最小的元素
tup=("apple","banana","cherry","apple","cherry")
min(tup) #apple

#sorted() 方法用于对元组进行排序
tup=("apple","banana","cherry","apple","cherry")
sorted(tup) #['apple', 'apple', 'banana', 'cherry']

#sum() 方法用于求和
tup=("apple","banana","cherry","apple","cherry")
sum(tup) #10

#zip() 函数用于将多个序列压平为一个序列
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
zipped = zip(a,b,c)
list(zipped) #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
#拆分序列
a,b,c = zip(*zipped)
print(a) #[1, 2, 3]
print(b) #[4, 5, 6]
print(c) #[7, 8, 9]
list(zip(range(5)))#[(0,), (1,), (2,), (3,), (4,)]

#列表方法
#append() 方法用于在列表末尾添加元素
lst = [1,2,3,4,5]
lst.append(6)
print(lst) #[1, 2, 3, 4, 5, 6]

#clear() 方法用于清空列表
lst = [1,2,3,4,5]
lst.clear()
print(lst) #[]

#copy() 方法用于复制列表
lst = [1,2,3,4,5]
lst2 = lst.copy()
print(lst2) #[1, 2, 3, 4, 5]


#count() 方法用于统计某个元素在列表中出现的次数
lst = [1,2,3,4,5,4,3,2,1]
lst.count(3) #2
lst.count(6) #0


#insert() 方法用于将指定对象插入列表
lst = [1,2,3,4,5]
lst.insert(2,6)
print(lst) #[1, 2, 6, 3, 4, 5]


#pop() 方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
lst = [1,2,3,4,5]
lst.pop() #5
print(lst) #[1, 2, 3, 4]
lst.pop(3)
print(lst) #[1, 2, 3]

#remove() 方法用于移除列表中某个值的第一个匹配项
lst = [1,2,3,4,5,4,3,2,1]
lst.remove(3)
print(lst) #[1, 2, 4, 5, 4, 3, 2, 1]

#in关键字 用于判断元素是否在列表中
lst = [1,2,3,4,5]
3 in lst #True
6 in lst #False

#排序#
#reverse() 方法用于反向排列列表
lst = [1,2,3,4,5]
lst.reverse()
print(lst) #[5, 4, 3, 2, 1]
#reverse() 方法与sort() 方法配合使用，可以实现列表的排序
#reversed() 函数可以返回一个反转的迭代器
list(reversed(lst))#[5, 4, 3, 2, 1]

#sort() 方法用于对原列表进行排序(无需创建新对象)
lst = [5,2,4,6,1]
lst.sort()
print(lst) #[1, 2, 4, 5, 6] 

b=['apple','watermalon','banana','cherry']#传递二级排序key=len
b.sort(key=len)
print(b) #['apple', 'banana', 'cherry', 'watermalon']

###连接和联合列表###
#+ 运算符用于连接两个列表
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2
print(lst3) #[1, 2, 3, 4, 5, 6]

#extend() 方法用于在列表末尾
#一次性追加另一个序列中的多个值(无需创建新对象)
lst = [1,2,3]
lst.extend([4,5,6])
print(lst) #[1, 2, 3, 4, 5, 6]

#二分搜索算法
import bisect
lst = [1,3,5,7,9]
bisect.bisect_left(lst, 4) #2 #找到元素插入位置
bisect.bisect_right(lst, 6) #4 #
bisect.bisect(lst, 8) #4
bisect.insort_left(lst, 4) #[1, 3, 4, 4, 5, 7, 9] #将元素插入相应位置
bisect.insort_right(lst, 6) #[1, 3, 4, 4, 5, 6, 7, 9]
bisect.insort(lst, 8) #[1, 3, 4, 4, 5, 6, 7, 8, 9]

#列表推导式
#列表推导式是一种创建列表的简便方法
#语法格式：[表达式 for 变量 in 可迭代对象 if 条件]
#表达式：表达式可以是任意表达式
#变量：变量是可迭代对象中的元素，可以是任意变量名
#可迭代对象：可以是列表、元组、字符串、字典等可迭代对象
#条件：可选的条件表达式，只有满足条件的元素才会被包含在结果列表中

#实例
lst = [1,2,3,4,5,6,7,8,9]
lst2 = [x for x in lst if x % 2 == 0]
print(lst2) #[2, 4, 6, 8]

lst3 = [x**2 for x in lst if x % 2 == 0]
print(lst3) #[4, 16, 36, 64]


#嵌套列表推导式
#列表推导式可以嵌套，即列表中包含列表
#语法格式：[[表达式 for 变量 in 可迭代对象 if 条件] for 变量 in 可迭代对象 if 条件]
#表达式：表达式可以是任意表达式 
#变量：变量是可迭代对象中的元素，可以是任意变量名
#可迭代对象：可以是列表、元组、字符串、字典等可迭代对象
#条件：可选的条件表达式，只有满足条件的元素才会被包含在结果列表中

#简单实例
matrix = [[1,2,3],[4,5,6],[7,8,9]]
lst = [num for row in matrix for num in row]
print(lst) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
#第一次外层循环：row = [1, 2, 3]
#内层循环：num = 1, num = 2, num = 3 lst 变为 [1, 2, 3]
#第二次外层循环：row = [4, 5, 6]
#内层循环：num = 4, num = 5, num = 6 lst 变为 [1, 2, 3, 4, 5, 6]
#第三次外层循环：row = [7, 8, 9]
#内层循环：num = 7, num = 8, num = 9 lst 变为 [1, 2, 3, 4, 5, 6, 7, 8, 9]


#切片
#切片操作符[ ]用于从列表中取出一部分元素，语法格式如下：
#lst[start:end:step]
#start: 起始索引，默认为0
#end: 结束索引，默认为列表长度
#step: 步长，默认为1
#如果start为负数，表示从列表末尾开始算起的第几个元素
#如果end为负数，表示从列表末尾开始算起的第几个元素
#如果step为负数，表示逆序切片
#如果start、end、step中有某个值为None，表示相应的索引值使用默认值
#如果step为0，表示切片包含0个元素，即空列表
#如果step大于列表长度，表示切片包含0个元素，即空列表
#如果start大于或等于end，表示切片包含0个元素，即空列表
#如果start、end、step都为None，表示复制整个列表
#如果start、end、step都为整数，表示切片包含start到end-1的元素，步长为step
#如果start为None，表示从列表末尾开始算起的第几个元素
#如果end为None，表示从列表末尾开始算起的第几个元素
#如果step为None，表示切片包含1个元素，即原列表的子序列
#如果start、end、step都为负数，表示逆序切片
#如果start为None，表示从列表末尾开始算起的第几个元素
#如果end为None，表示从列表末尾开始算起的第几个元素
#如果step为None，表示切片包含1个元素，即原列表的子序列

#实例
lst = [1,2,3,4,5,6,7,8,9]
print(lst[0:5:2]) #[1, 3, 5]
print(lst[::2]) #[1, 3, 5, 7, 9]
print(lst[::-1]) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
print(lst[5:0:-1]) #[6, 5, 4, 3, 2]
print(lst[5:0:-2]) #[6, 4, 2]
print(lst[5:0:-3]) #[6, 3]
print(lst[5:0:-4]) #[6]
print(lst[5:0:-5]) #[6]


###字典###
#实例
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(d['name']) #Alice
print(d['age']) #25
print(d.get('gender')) #None
print(d.get('gender', 'unknown')) #unknown


#keys() 方法用于获取字典所有键
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(d.keys()) #dict_keys(['name', 'age', 'city'])

#values() 方法用于获取字典所有值
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(d.values()) #dict_values(['Alice', 25, 'Beijing'])

#items() 方法用于获取字典所有键值对
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
print(d.items()) #dict_items([('name', 'Alice'), ('age', 25), ('city', 'Beijing')])

#pop() 方法用于删除字典中指定键的值，并返回该值
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
d.pop('name') #Alice
print(d) #{'age': 25, 'city': 'Beijing'}


#popitem() 方法用于随机删除字典中的一对键值对，并返回该对键值对
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
d.popitem() #随机删除一对键值对
print(d) #{'name': 'Alice', 'age': 25}

#update() 方法用于更新字典，将指定字典中的键值对添加到当前字典中
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
d2 = {'gender': 'female', 'occupation': 'engineer'}
d.update(d2)
print(d) #{'name': 'Alice', 'age': 25, 'city': 'Beijing', 'gender': 'female', 'occupation': 'engineer'}

#将两个序列在字典中按元素配对
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Beijing']
d = dict(zip(keys, values))
print(d) #{'name': 'Alice', 'age': 25, 'city': 'Beijing'}

#setdefault() 方法用于设置字典中指定键的值，如果该键不存在，则添加该键值对
d = {'name': 'Alice', 'age': 25, 'city': 'Beijing'}
d.setdefault('gender', 'female')
print(d) #{'name': 'Alice', 'age': 25, 'city': 'Beijing', 'gender': 'female'}

words = ['apple', 'banana', 'cherry', 'orange', 'bar', 'atom']
by_letter = {}
for word in words:
    letter=word[0]
    by_letter.setdefault(letter, []).append(word)
by_letter

from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)
by_letter

#字典推导式
#字典推导式是一种创建字典的简便方法
#语法格式：{键表达式:值表达式 for 变量 in 可迭代对象 if 条件}
#键表达式：键表达式可以是任意表达式，但结果必须是一个可哈希的对象
#值表达式：值表达式可以是任意表达式
#变量：变量是可迭代对象中的元素，可以是任意变量名
#可迭代对象：可以是列表、元组、字符串、字典等可迭代对象
#条件：可选的条件表达式，只有满足条件的元素才会被包含在结果字典中

#实例
#求字典的平方，但只保留奇数
squares = {x:x**2 for x in range(1, 11) if x**2 % 2 == 1}
print(squares) #{1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

#求字典的平方，但只保留偶数，且值小于100
squares = {x:x**2 for x in range(1, 11) if x**2 % 2 == 0 and x**2 < 100}
print(squares) #{4: 16, 16: 256, 36: 1296, 64: 4096}

##集合##
#集合是一个无序不重复元素的集   
#创建集合
s = set()
s = {1, 2, 3, 3, 2, 1} #集合中只包含唯一的元素
s = set([1, 2, 3, 3, 2, 1]) #集合中只包含唯一的元素

#add() 方法用于向集合中添加元素
s = {1, 2, 3}
s.add(4)
print(s) #{1, 2, 3, 4}

#remove() 方法用于从集合中删除元素
s = {1, 2, 3}
s.remove(2)
print(s) #{1, 3}

#discard() 方法用于从集合中删除元素，如果元素不存在，则不报错
s = {1, 2, 3}
s.discard(2)
print(s) #{1, 3}

#pop() 方法用于随机删除集合中的一个元素，并返回该元素
s = {1, 2, 3}
s.pop() #随机删除一个元素
print(s) #{1, 2}

#clear() 方法用于清空集合
s = {1, 2, 3}
s.clear()
print(s) #set()

#union() 方法用于求两个集合的并集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
s3 = s1|s2 #等价于s3 = s1.union(s2)``
print(s3) #{1, 2, 3, 4, 5}

#intersection() 方法用于求两个集合的交集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
s3 = s1&s2 #等价于s3 = s1.intersection(s2)
print(s3) #{3}

#difference() 方法用于求两个集合的差集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)
print(s3) #{1, 2}

#symmetric_difference() 方法用于求两个集合的对称差集
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)
print(s3) #{1, 2, 4, 5}

#issubset()/issuperset()方法用于判断一个集合是否是另一个集合的子集或超集
s1 = {1, 2, 3}
s2 = {1, 2, 3, 4, 5}
print(s1.issubset(s2)) #True
print(s2.issubset(s1)) #False
print(s1.issuperset(s2)) #False
print(s2.issuperset(s1)) #True

#isdisjoint() 方法用于判断两个集合是否有交集
s1 = {1, 2, 3}
s2 = {4, 5, 6}
print(s1.isdisjoint(s2)) #True
s3 = {1, 2, 3}
s4 = {3, 4, 5}
print(s3.isdisjoint(s4)) #False

#集合推导式
#集合推导式是一种创建集合的简便方法
#语法格式：{表达式 for 变量 in 可迭代对象 if 条件}
#表达式：表达式可以是任意表达式，但结果必须是一个可哈希的对象
#变量：变量是可迭代对象中的元素，可以是任意变量名
#可迭代对象：可以是列表、元组、字符串、字典等可迭代对象
#条件：可选的条件表达式，只有满足条件的元素才会被包含在结果集合中

#实例
#求集合的平方，但只保留奇数
squares = {x**2 for x in range(1, 11) if x**2 % 2 == 1}
print(squares) #{1, 9, 25, 49, 81}
#求集合的平方，但只保留偶数
squares = {x**2 for x in range(1, 11) if x**2 % 2 == 0}
print(squares) #{4, 16, 36, 64, 100}

###numpy基础###
import numpy as np
#生成一个随机数组
s = np.random.randn(2, 3)#生成的是服从标准正态分布（均值为 0，标准差为 1）的随机数。
print(s) #[0.57142857 0.71428571 0.64285714]
#数组维度
print(s.shape) #(2, 3)
#数组元素个数
print(s.size) #6
#数组元素数据类型
print(s.dtype) #float64
print(s.ndim)#2行
print(s.itemsize) #8字节


#创建数组
a = np.array([1, 2, 3])
print(a) #[1 2 3]

#创建二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b) 

#创建三维数组
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c) 


#创建全0数组
d = np.zeros(3)
print(d) #[0. 0. 0.]

#创建全1数组
e = np.ones(3)
print(e) #[1. 1. 1.]
#这里的1.表示浮点数1.0，因为NumPy默认生成浮点数数组。

#创建指定范围的数组
f = np.arange(1, 10, 2)
print(f) #[1 3 5 7 9]
f = np.arange(10)
print(f)

#创建等差数组
g = np.linspace(1, 10, 5)
print(g) #[ 1.   3.25 5.5  7.75 10.  ]

#创建随机数组
h = np.random.rand(3, 3)
print(h)

#布尔索引
#布尔索引是一种访问数组元素的一种方式
#语法格式：数组[数组>条件]
#数组：数组对象
#条件：条件表达式，返回布尔值

#实例
#访问数组中大于3的元素
a = np.array([1, 2, 3, 4, 5])
print(a[a>3]) #[4 5]

#访问数组中大于3的元素，并修改为10
a = np.array([1, 2, 3, 4, 5])
a[a>3] = 10
print(a) #[1 2 3 10 10]

#访问数组中大于3的元素，并修改为10
a = np.array([1, 2, 3, 4, 5])
a[a>3] = 10
print(a) #[1 2 3 10 10]

#用布尔值选择数据
#在索引数组传入布尔值数组，可以访问数组中满足条件的元素
#语法格式：数组[布尔数组]
#数组：数组对象
#布尔数组：布尔值数组，元素个数必须与数组元素个数相同

#实例
#访问数组中大于3的元素
a = np.array([1, 2, 3, 4, 5])
b = np.array([True, False, True, False, True])
print(a[b]) #[1 3 5]

#访问数组中大于3的元素，并修改为10
a = np.array([1, 2, 3, 4, 5])
b = np.array([True, False, True, False, True])
a[b] = 10
print(a) #[10  2 10  4 10]

#访问数组中大于3的元素，并修改为10
a = np.array([1, 2, 3, 4, 5])
b = np.array([True, False, True, False, True])
a[b] = 10
print(a) #[1 2 10 4 10]

#多个布尔值联合选择数据 
#在索引数组传入多个布尔值数组，可以访问数组中满足多个条件的元素
#语法格式：数组[布尔数组1 & 布尔数组2]
#数组：数组对象
#布尔数组：布尔值数组，元素个数必须与数组元素个数相同

#实例 and or
a = np.array([1, 2, 3, 4, 5])
b = np.array([True, False, True, False, True])
c = np.array([True, True, False, False, True])
d = a[b & c]
print(d) #[3 5]


#实例 and or
a = np.array([1, 2, 3, 4, 5])
b = np.array([True, False, True, False, True])
c = np.array([True, True, False, False, True])
d = a[b | c]
print(d) #[1 2 3 5]

#any和all函数
#any() 函数用于判断数组中是否有元素为真
#all() 函数用于判断数组中是否所有元素为真
#实例
a = np.array([True, True, False, False, True])
a.any()
a.all()

#sort() 方法用于对数组进行排序
a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
a.sort()
print(a) #[1 1 2 3 3 4 5 5 5 6 9]


#argsort() 方法用于返回数组排序后的索引
a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
b = a.argsort()
print(b) #[1 3 7 0 9 5 2 8 4 6 10]

import matplotlib.pyplot as plt 
import matplotlib.pyplot as plt




#数组属性
#shape属性用于获取数组的形状
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape) #(2, 3)


#dtype属性用于获取数组元素的数据类型
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.dtype) #int64

#size属性用于获取数组元素的总个数
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.size) #6

#ndim属性用于获取数组的维度
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim) #2

#itemsize属性用于获取数组元素的字节大小
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.itemsize) #8

#数据类型转换
#astype() 方法用于将数组元素转换为指定类型
a = np.array([[1, 2, 3], [4, 5, 6]])
a.dtype
b = a.astype(np.float32)
b.dtype


#数组切片
#切片操作是访问数组元素的一种方式
#语法格式：数组[起始:终止:步长]
#起始：起始索引，默认为0
#终止：终止索引，默认为数组长度
#步长：步长，默认为1


#实例
#访问数组的第一个元素
a = np.array([1, 2, 3, 4, 5])
print(a[0]) #1

#访问数组的最后一个元素
a = np.array([1, 2, 3, 4, 5])
print(a[-1]) #5

#访问数组的第二个到第三个元素
a = np.array([1, 2, 3, 4, 5])
print(a[1:3]) #[2 3]

#访问数组的第三个到第五个元素，每隔两个元素取一个
a = np.array([1, 2, 3, 4, 5])
print(a[2:5:2]) #[3 5]

#访问数组的倒数第二个元素
a = np.array([1, 2, 3, 4, 5])
print(a[-2]) #4

#访问数组的倒数第二个到最后一个元素
a = np.array([1, 2, 3, 4, 5])
print(a[-2:]) #[4 5]

#神奇索引
#神奇索引是一种访问数组元素的一种方式
#语法格式：数组[索引数组]
#索引数组：整数数组，元素个数必须与数组元素个数相同


#实例
#访问数组的第一个元素
a = np.array([1, 2, 3, 4, 5])
print(a[[0]]) #[1]


#访问数组的第二个到第三个元素
a = np.array([1, 2, 3, 4, 5])
print(a[[1, 2]]) #[2 3]


#访问数组的第三个到第五个元素，每隔两个元素取一个
a = np.array([1, 2, 3, 4, 5])
print(a[[2, 4]]) #[3 5]


#访问数组的倒数第二个元素
a = np.array([1, 2, 3, 4, 5])
print(a[[-2]]) #[4]


#访问数组的倒数第二个到最后一个元素
a = np.array([1, 2, 3, 4, 5])
print(a[[-2, -1]]) #[4 5]

#二维神奇索引
#二维神奇索引是一种访问数组元素的一种方式
#语法格式：数组[行索引数组, 列索引数组]
#行索引数组：整数数组，元素个数必须与数组行数相同
#列索引数组：整数数组，元素个数必须与数组列数相同

#实例
#访问数组的第一个元素
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[[0], [0]]) #[1]

#访问数组的第二行的第二个到第三个元素
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[[1], [1, 2]]) #[5 6]


arr=np.empty((8,4))
for i in range(8):
   arr[i]=i
print(arr)
arr[[4,3,0,6]]

arr=np.arange(32).reshape(8,4)
print(arr)
arr[[4,3,0,6],[0,1,2,3]]
arr[[1,5,7,2]][:,[0,3,1,2]]
#神奇索引与切片不同，他总是将数据复制到一个新数组中，而不是引用原数组的元素。


#数组维度变换
#reshape() 方法用于改变数组的形状
#语法格式：数组.reshape(行数, 列数)
#实例
#将一个一维数组变换为二维数组
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b) #[[1 2 3]
 [4 5 6]]

#将一个二维数组变换为一维数组
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(6)
print(b) #[1 2 3 4 5 6]

arr=np.arange(16).reshape(2,2,4)
#将一维数组重塑为一个三维数组，形状为 (2, 2, 4)。
#这意味着数组有2个二维子数组，每个二维子数组有2行和4列。
arr.transpose(1,0,2)
arr.swapaxes(1,2)

#通用函数
#通用函数是对数组元素进行操作的一种方式
#语法格式：np.函数名(数组, 参数)
#函数名：可以是sum、mean、max、min、argmin、argmax等函数
#参数：可以是axis、keepdims等参数


#实例
#求一个一维数组的和
a = np.array([1, 2, 3, 4, 5])
b = np.sum(a)
print(b) #15

#求一个二维数组的和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a)
print(b) #10

#求一个二维数组的行和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a, axis=1)
print(b) #[4 6]

#求一个二维数组的列和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a, axis=0)
print(b) #[3 7]

#通用函数
#通用函数是对数组元素进行操作的一种方式
#语法格式：np.函数名(数组, 参数)
#函数名：可以是sum、mean、max、min、argmin、argmax等函数
#参数：可以是axis、keepdims等参数

#实例
#求一个一维数组的和
a = np.array([1, 2, 3, 4, 5])
b = np.sum(a)
print(b) #15

#求一个二维数组的行和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a, axis=1)
print(b) #[4 6]

#sqrt 用于计算输入数组或标量的平方根。
a = np.array([1, 2, 3, 4, 5])
b = np.sqrt(a)
print(b) #[1. 1.41421356 1.73205081 2. 2.23606798]

#exp 用于计算输入数组或标量的指数。
a = np.array([1, 2, 3, 4, 5])
b = np.exp(a)
print(b) #[ 2.71828183  7.3890561  20.08553692 54.59815003 148.4131591 ]

#mean均值
a = np.array([1, 2, 3, 4, 5])
b = np.mean(a)
print(b) #3.0

#modf 用于将输入数组的小数和整数部分分离。
a = np.array([1.5, 2.3, 3.7, 4.2, 5.1])
b = np.modf(a)
print(b) #([0.5 0.3 0.7 0.2 0.1], [1. 2. 3. 4. 5.])

#argmax 用于返回输入数组中最大值的索引。
a = np.array([1, 2, 3, 4, 5])
b = np.argmax(a)
print(b) #4

#argmin 用于返回输入数组中最小值的索引。
a = np.array([1, 2, 3, 4, 5])
b = np.argmin(a)
print(b) #0

#dot 用于计算两个数组的点积。
a = np.array([1, 2, 3])
b = np.array([4, 5, 6]) 
c = np.dot(a, b)

arr=np.random.randn(5,4)
arr.mean(1)
#多维数组的轴及其操作
#创建三维数组 这个数组的形状是 (3, 2, 3)，
#表示它有 3 个二维数组，每个二维数组有 2 行，每行有 3 列。
array_3d = np.array([[[1, 2, 3], 
                      [4, 5, 6]],

                     [[7, 8, 9], 
                      [10, 11, 12]],

                     [[13, 14, 15], 
                      [16, 17, 18]]])
#沿轴 0 进行操作，如果我们沿轴 0 求和：
sum_axis_0 = np.sum(array_3d, axis=0)
sum_axis_0 = [[21, 24, 27], 
              [30, 33, 36]]
#这里，我们对每个位置的值进行相加，沿着 3 个二维数组的方向。例如：
#第一个位置：[1, 4] + [7, 10] + [13, 16] = [21, 30]
#第二个位置：[2, 5] + [8, 11] + [14, 17] = [24, 33]
#第三个位置：[3, 6] + [9, 12] + [15, 18] = [27, 36]

#沿轴 1 进行操作,如果我们沿轴 1 求和：
sum_axis_1 = np.sum(array_3d, axis=1)
sum_axis_1 = [[ 5,  7,  9],
              [17, 19, 21],
              [29, 31, 33]]
#第一个二维数组：[1, 2, 3] + [4, 5, 6] = [5, 7, 9]
#第二个二维数组：[7, 8, 9] + [10, 11, 12] = [17, 19, 21]
#第三个二维数组：[13, 14, 15] + [16, 17, 18] = [29, 31, 33]

#沿轴 2 进行操作 如果我们沿轴 2 求和：
sum_axis_2 = np.sum(array_3d, axis=2)
sum_axis_2 = [[ 6, 15],
              [24, 33],
              [42, 51]]
#第一个二维数组的第一行：1 + 2 + 3 = 6
#第一个二维数组的第二行：4 + 5 + 6 = 15
#第二个二维数组的第一行：7 + 8 + 9 = 24
#第三个二维数组的第一行：13 + 14 + 15 = 42
#第三个二维数组的第二行：16 + 17 + 18 = 51

#条件逻辑数组
#where() 函数用于根据条件创建数组
xarr = np.array([1, 2, 3, 4, 5])
yarr = np.array([4, 2, 1, 5, 3])
condition = np.array([True, False, True, False, True])
result = np.where(condition, xarr, yarr)
print(result) #[1 2 3 5 5]

#第二个和第三个参数分别是条件为True和False时的返回值。
#他们可以是数组也可以是标量，也可以混合
arr=np.random.randn(4,4)
arr>0
np.where(arr>0,2,-2)

#数组拆分
#split() 方法用于分割数组
#语法格式：np.split(数组, 切割位置, axis=0)
#切割位置：指定分割位置，可以是整数或整数数组
#axis：指定分割方向，默认为0，即竖直方向


#实例
#分割一个一维数组
a = np.array([1, 2, 3, 4, 5, 6])
b, c = np.split(a, [3, 5])
print(b) #[1 2 3]
print(c) #[4 5 6]


#分割一个二维数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b, c = np.split(a, [2], axis=1)
print(b) #[[1 2]
 [4 5]]
print(c) #[[3]
 [6]
 [9]]

#数组拼接
#concatenate() 方法用于拼接两个或多个数组
#语法格式：np.concatenate((数组1, 数组2), axis=0)
#axis：指定拼接方向，默认为0，即竖直方向


#实例
#拼接两个一维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6]) 
c = np.concatenate((a, b))
print(c) #[1 2 3 4 5 6]

#拼接两个二维数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b), axis=0)
print(c) #[[1 2]
 [3 4]
 [5 6]
 [7 8]]


#数组堆叠
#stack() 方法用于堆叠数组
#语法格式：np.stack((数组1, 数组2), axis=0)
#axis：指定堆叠方向，默认为0，即竖直方向


#实例
#堆叠两个一维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6]) 
c = np.stack((a, b))
print(c) #[[1 2 3]
 [4 5 6]]


#数组分割   
#split() 方法用于分割数组
#语法格式：np.split(数组, 切割位置, axis=0)
#切割位置：指定分割位置，可以是整数或整数数组
#axis：指定分割方向，默认为0，即竖直方向


#实例
#分割一个一维数组
a = np.array([1, 2, 3, 4, 5, 6])
b, c = np.split(a, [3, 5])
print(b) #[1 2 3]
print(c) #[4 5 6]


#分割一个二维数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b, c = np.split(a, [2], axis=1)
print(b) #[[1 2]
 [4 5]
 [7 8]]
print(c) #[[3]
 [6]
 [9]]


#数组迭代
#迭代是访问数组元素的一种方式
#语法格式：for 变量 in 数组:
#变量：迭代变量，可以是任意变量名
#数组：数组对象


#实例
#迭代一个一维数组
a = np.array([1, 2, 3, 4, 5])
for i in a:
    print(i) #1 2 3 4 5


#迭代一个二维数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in a: 
    print(i) #[1 2 3] [4 5 6] [7 8 9]


#数组运算
#运算是对数组元素进行操作的一种方式
#语法格式：运算符(数组1, 数组2)
#运算符：可以是加减乘除、求模、幂、矩阵乘法等运算符


#实例
#求两个一维数组的和
a = np.array([1, 2, 3])
b = np.array([4, 5, 6]) 
c = a + b
print(c) #[5 7 9]


#求两个二维数组的乘积
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = a * b
print(c) #[[ 5 12]
 [21 32]]


#数组统计
#统计是对数组元素进行汇总的一种方式
#语法格式：np.sum(数组, axis=None)
#axis：指定统计方向，默认为None，即所有方向


#实例
#求一个一维数组的和
a = np.array([1, 2, 3, 4, 5])
b = np.sum(a)
print(b) #15


#求一个二维数组的和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a)
print(b) #10


#求一个二维数组的行和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a, axis=1)
print(b) #[4 6]


#求一个二维数组的列和
a = np.array([[1, 2], [3, 4]])
b = np.sum(a, axis=0)   
print(b) #[3 7]


#数组排序
#排序是对数组元素进行排列的一种方式
#语法格式：np.sort(数组, axis=None)
#axis：指定排序方向，默认为None，即所有方向


#实例
#对一个一维数组进行排序
a = np.array([3, 1, 4, 2])
b = np.sort(a)
print(b) #[1 2 3 4]


#对一个二维数组进行排序
a = np.array([[3, 1], [4, 2]])
b = np.sort(a)
print(b) #[[1 2]
 [3 4]]


#数组搜索
#搜索是查找数组元素的一种方式
#语法格式：np.where(条件表达式)
#条件表达式：布尔表达式，返回True或False的数组


#实例
#查找一个一维数组中大于3的元素的索引
a = np.array([1, 2, 3, 4, 5])
b = np.where(a > 3)
print(b) #(array([3, 4, 5], dtype=int64),)


#查找一个二维数组中大于3的元素的索引
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.where(a > 3)
print(b) #(array([0, 1, 1, 1], dtype=int64), array([1, 1, 0, 1], dtype=int64))


#数组过滤
#过滤是删除数组元素的一种方式
#语法格式：np.extract(条件表达式, 数组)
#条件表达式：布尔表达式，返回True或False的数组
#数组：数组对象


#实例
#删除一个一维数组中大于3的元素
a = np.array([1, 2, 3, 4, 5])
b = np.extract(a > 3, a)
print(b) #[4 5]


#删除一个二维数组中大于3的元素
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.extract(a > 3, a)
print(b) #[[4 5]
 [5 6]]


#数组拷贝
#拷贝是创建数组的一种方式
#语法格式：np.copy(数组)


#实例
#拷贝一个一维数组
a = np.array([1, 2, 3])
b = np.copy(a)
print(b) #[1 2 3]


#拷贝一个二维数组
a = np.array([[1, 2], [3, 4]])
b = np.copy(a)
print(b) #[[1 2]
 [3 4]]


#数组保存与读取
#保存是将数组保存到磁盘的一种方式
#语法格式：np.save(文件名, 数组)
#文件名：指定保存的文件名
#数组：数组对象


#实例
#保存一个一维数组
a = np.array([1, 2, 3])
np.save('my_array', a)


#读取一个一维数组
b = np.load('my_array.npy')
print(b) #[1 2 3]


#保存一个二维数组
a = np.array([[1, 2], [3, 4]])
np.save('my_array', a)


#读取一个二维数组
b = np.load('my_array.npy')
print(b) #[[1 2]
 [3 4]]


#保存多个数组
#语法格式：np.savez(文件名, 数组1=数组1, 数组2=数组2, ...)
#文件名：指定保存的文件名
#数组1=数组1, 数组2=数组2, ...：指定多个数组


#实例
#保存多个数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.savez('my_arrays', a=a, b=b)


#读取多个数组
data = np.load('my_arrays.npz')
print(data['a']) #[1 2 3]
print(data['b']) #[4 5 6]


#数组压缩
#压缩是删除数组元素的一种方式
#语法格式：np.compress(条件表达式, 数组, axis=None)
#条件表达式：布尔表达式，返回True或False的数组
#数组：数组对象
#axis：指定压缩方向，默认为None，即所有方向


#实例
#压缩一个一维数组
a = np.array([1, 2, 3, 4, 5])
b = np.compress(a > 3, a)
print(b) #[4 5]


#压缩一个二维数组
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.compress(a > 3, a, axis=0)
print(b) #[[4 5]
 [5 6]]


#数组填充
#填充是对数组元素进行填充的一种方式
#语法格式：np.pad(数组, 填充宽度, 填充方式, axis=None)
#数组：数组对象
#填充宽度：元组，指定填充的宽度
#填充方式：字符串，指定填充方式，可以是'constant', 'edge', 'linear_ramp', 'maximum', 'mean', 'median', 'minimum', 'reflect', 'symmetric', 'wrap'
#axis：指定填充方向，默认为None，即所有方向


#实例
#填充一个一维数组
a = np.array([1, 2, 3, 4, 5])
b = np.pad(a, (2, 3), 'constant', constant_values=(4, 6))
print(b) #[4 4 1 2 3 4 5 6 6]


#填充一个二维数组
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.pad(a, ((2, 3), (1, 2)), 'edge')
print(b) #[[0 0 0 0 0]
 [0 0 1 2 0]
 [0 0 3 4 0]
 [0 0 5 6 0]
 [0 0 0 0 0]]


#数组切块
#切块是将数组分割成小块的一种方式
#语法格式：np.array_split(数组, 切块数, axis=0)
#数组：数组对象
#切块数：整数，指定切块数
#axis：指定切块方向，默认为0，即竖直方向


#实例
#切块一个一维数组
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.array_split(a, 3)
print(b) #[[1 2 3]
 [4 5 6]
 [7 8 9]]


#切块一个二维数组
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array_split(a, 2, axis=1)
print(b) #[[[1 2]
  [4 5]
  [7 8]]

 [[3 6]
  [5 8]
  [7 9]]]


#数组合并
#合并是将多个数组合并成一个数组的一种方式
#语法格式：np.concatenate((数组1, 数组2), axis=0)
#axis：指定合并方向，默认为0，即竖直方向


#实例
#合并两个一维数组
a = np.array([1, 2, 3])
b = np.array([4, 5, 6]) 
c = np.concatenate((a, b))
print(c) #[1 2 3 4 5 6]


#合并两个二维数组
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.concatenate((a, b), axis=0)
print(c) #[[1 2]
 [3 4]
 [5 6]
 [7 8]]


#数组重复
#重复是将数组元素重复的一种方式
#语法格式：np.repeat(数组, 重复次数, axis=None)
#数组：数组对象
#重复次数：整数，指定重复次数
#axis：指定重复方向，默认为None，即所有方向


#实例
#重复一个一维数组
a = np.array([1, 2, 3])
b = np.repeat(a, 2)
print(b) #[1 1 2 2 3 3]


#重复一个二维数组
a = np.array([[1, 2], [3, 4]])
b = np.repeat(a, 2, axis=0)
print(b) #[[1 2]
 [1 2]
 [3 4]
 [3 4]]


#数组转置
#转置是将数组的行列互换的一种方式
#语法格式：np.transpose(数组)


#实例
#转置一个二维数组
a = np.array([[1, 2], [3, 4]])
b = np.transpose(a)
print(b) 
a.T 




#dot函数
#dot函数是矩阵乘法的一种方式
#语法格式：np.dot(数组1, 数组2)

#实例
#矩阵乘法
#两个矩阵 ( A ) 和 ( B )，结果矩阵 ( C ) 的第 ( i ) 行第 ( j ) 列的
#元素 ( C_{ij} ) 是 ( A ) 的第 ( i ) 行与 ( B ) 的第 ( j ) 列对应元素的乘积之和。
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
c = np.dot(a, b)
print(c) #[[19 22]
 [43 50]]
#例如( C_{11} = 1 x 5 + 2 x 7 = 5 + 14 = 19 )

#dot函数的另一种用法
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.dot(a, b)
print(c) #32
#点积1 x 4 + 2 x 5 + 3 x 6 = 4 + 10 + 18 = 32



#数组随机数
#随机数是由随机数生成器产生的数字序列
#语法格式：np.random.rand(shape)
#shape：元组，指定生成数组的形状


#实例
#生成一个3x3的随机数组
a = np.random.rand(3, 3)
print(a) #[[0.57142857 0.71428571 0.64285714]
 [0.42857143 0.85714286 0.92857143]
 [0.35714286 0.14285714 0.07142857]]


#生成一个2x4的随机数组
a = np.random.rand(2, 4)
print(a) #[[0.57142857 0.71428571 0.64285714 0.42857143]
 [0.85714286 0.92857143 0.35714286 0.14285714]]


#数组随机数种子
#随机数种子是随机数生成器的初始状态
#语法格式：np.random.seed(seed)
#seed：整数，指定随机数种子


#实例
#设置随机数种子
np.random.seed(1)
a = np.random.rand(3, 3)
print(a) #[[0.5488135  0.71518937 0.60276338]
 [0.54488318 0.4236548  0.64589411]
 [0.43758721 0.891773 0.96366276]]


#实例
#设置随机数种子
np.random.seed(1)
a = np.random.rand(2, 4)
print(a) #[[0.5488135  0.71518937 0.60276338 0.54488318] 
[0.4236548  0.64589411 0.43758721 0.891773  ]]


#数组随机数范围
#随机数范围是随机数生成器产生的数字的取值范围
#语法格式：np.random.rand(shape)
#shape：元组，指定生成数组的形状


#实例
#生成一个3x3的随机数组，取值范围为0到1
a = np.random.rand(3, 3)
print(a) 
#[[0.57142857 0.71428571 0.64285714]
#[0.42857143 0.85714286 0.92857143]
#[0.35714286 0.14285714 0.07142857]]


#数组随机数整数
#随机数整数是随机数生成器产生的整数序列
#语法格式：np.random.randint(low, high, size)
#low：整数，指定随机数的最小值
#high：整数，指定随机数的最大值
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机整数数组，取值范围为0到10
a = np.random.randint(0, 10, (3, 3))
print(a) #[[7 3 9]
 [1 9 6]
 [4 2 1]]


#生成一个2x4的随机整数数组，取值范围为0到10
a = np.random.randint(0, 10, (2, 4))
print(a) #[[5 9 2 8]
 [0 4 7 1]]


#数组随机数标准正态分布
#随机数标准正态分布是随机数生成器产生的符合标准正态分布的随机数序列
#语法格式：np.random.randn(shape)
#shape：元组，指定生成数组的形状


#实例
#生成一个3x3的随机标准正态分布数组
a = np.random.randn(3, 3)
print(a) #[[ 1.54309995 -0.19920096 -0.46490446]
 [ 0.18232156  0.87460945  0.36424925]
 [-0.97728459 -0.66882411 -0.12202801]]


#生成一个2x4的随机标准正态分布数组
a = np.random.randn(2, 4)
print(a) #[[-0.36758851  0.26018139 -0.92231829 -0.13102235]
 [ 0.58838895 -0.16240026  0.18118915  0.76710615]]


#数组随机数指数分布
#随机数指数分布是随机数生成器产生的符合指数分布的随机数序列
#语法格式：np.random.exponential(scale, size)
#scale：浮点数，指定随机数的缩放因子
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机指数分布数组，取值范围为0到1
a = np.random.exponential(1, (3, 3))
print(a) #[[0.36787944 0.73575888 0.53938221]
 [0.26969111 0.81061462 0.50602615]
 [0.13533528 0.2401581  0.08336624]]


#生成一个2x4的随机指数分布数组，取值范围为0到1
a = np.random.exponential(1, (2, 4))
print(a) #[[0.36787944 0.73575888 0.53938221 0.26969111]
 [0.81061462 0.50602615 0.13533528 0.2401581 ]]


#数组随机数对数正态分布
#随机数对数正态分布是随机数生成器产生的符合对数正态分布的随机数序列
#语法格式：np.random.lognormal(mean, sigma, size)
#mean：浮点数，指定随机数的期望值
#sigma：浮点数，指定随机数的标准差
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机对数正态分布数组
a = np.random.lognormal(0, 1, (3, 3))
print(a) #[[ 0.8824969  0.98207142  0.94280904]
 [ 0.95872034  0.99526231  0.9736551 ]
 [ 0.93400655  0.89973003  0.86545357]]


#生成一个2x4的随机对数正态分布数组
a = np.random.lognormal(0, 1, (2, 4))
print(a) #[[ 0.8824969  0.98207142  0.94280904  0.95872034]
 [ 0.99526231  0.9736551   0.93400655  0.89973003]]


#数组随机数均匀分布
#随机数均匀分布是随机数生成器产生的符合均匀分布的随机数序列
#语法格式：np.random.uniform(low, high, size)
#low：浮点数，指定随机数的最小值
#high：浮点数，指定随机数的最大值
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机均匀分布数组，取值范围为0到1
a = np.random.uniform(0, 1, (3, 3))
print(a) #[[0.5488135  0.71518937 0.60276338]
 [0.54488318 0.4236548  0.64589411]
 [0.43758721 0.891773 0.96366276]]


#生成一个2x4的随机均匀分布数组，取值范围为0到1
a = np.random.uniform(0, 1, (2, 4))
print(a) #[[0.5488135  0.71518937 0.60276338 0.54488318]
 [0.4236548  0.64589411 0.43758721 0.891773  ]]


#数组随机数正态分布
#随机数正态分布是随机数生成器产生的符合正态分布的随机数序列
#语法格式：np.random.normal(loc, scale, size)
#loc：浮点数，指定随机数的均值
#scale：浮点数，指定随机数的标准差
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机正态分布数组
a = np.random.normal(0, 1, (3, 3))
print(a) #[[ 1.54309995 -0.19920096 -0.46490446]
 [ 0.18232156  0.87460945  0.36424925]
 [-0.97728459 -0.66882411 -0.12202801]]


#生成一个2x4的随机正态分布数组
a = np.random.normal(0, 1, (2, 4))
print(a) #[[-0.36758851  0.26018139 -0.92231829 -0.13102235]
 [ 0.58838895 -0.16240026  0.18118915  0.76710615]]


#数组随机数泊松分布
#随机数泊松分布是随机数生成器产生的符合泊松分布的随机数序列
#语法格式：np.random.poisson(lam, size)
#lam：浮点数，指定随机数的lambda值
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机泊松分布数组
a = np.random.poisson(1, (3, 3))
print(a) #[[0 0 0]
 [0 0 0]
 [0 0 0]]


#生成一个2x4的随机泊松分布数组
a = np.random.poisson(1, (2, 4))
print(a) #[[0 0 0 0]
 [0 0 0 0]]


#数组随机数布朗运动
#随机数布朗运动是随机数生成器产生的符合布朗运动的随机数序列
#语法格式：np.random.binomial(n, p, size)
#n：整数，指定随机数的实验次数
#p：浮点数，指定随机数的成功概率
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机布朗运动数组，实验次数为10，成功概率为0.5
a = np.random.binomial(10, 0.5, (3, 3))
print(a) #[[5 5 4]
 [5 5 5]
 [4 5 5]]


#生成一个2x4的随机布朗运动数组，实验次数为10，成功概率为0.5
a = np.random.binomial(10, 0.5, (2, 4))
print(a) #[[5 5 4 5]
 [5 5 5 5]]


#数组随机数超几何分布
#随机数超几何分布是随机数生成器产生的符合超几何分布的随机数序列
#语法格式：np.random.hypergeometric(ngood, nbad, nsample, size)
#ngood：整数，指定随机数的好样本数
#nbad：整数，指定随机数的坏样本数
#nsample：整数，指定随机数的总样本数
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机超几何分布数组，好样本数为5，坏样本数为3，总样本数为8
a = np.random.hypergeometric(5, 3, 8, (3, 3))
print(a) #[[3 3 0]
 [2 2 3]
 [1 2 3]]


#生成一个2x4的随机超几何分布数组，好样本数为5，坏样本数为3，总样本数为8
a = np.random.hypergeometric(5, 3, 8, (2, 4))
print(a) #[[3 3 0 0]
 [2 2 3 3]]


#数组随机数卡方分布
#随机数卡方分布是随机数生成器产生的符合卡方分布的随机数序列
#语法格式：np.random.chisquare(df, size)
#df：整数，指定随机数的自由度
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机卡方分布数组，自由度为5
a = np.random.chisquare(5, (3, 3))
print(a) #[[ 2.30890142  1.04899723  0.8824969 ]
 [ 0.73575888  0.53938221  0.42857143]
 [ 0.26969111  0.14285714  0.07142857]]


#生成一个2x4的随机卡方分布数组，自由度为5
a = np.random.chisquare(5, (2, 4))
print(a) #[[ 2.30890142  1.04899723  0.8824969  0.73575888]
 [ 0.53938221  0.42857143  0.26969111  0.14285714]]


#数组随机数韦伯分布
#随机数韦伯分布是随机数生成器产生的符合韦伯分布的随机数序列
#语法格式：np.random.weibull(a, size)
#a：浮点数，指定随机数的形状参数
#size：元组，指定生成数组的形状


#实例
#生成一个3x3的随机韦伯分布数组，形状参数为1
a = np.random.weibull(1, (3, 3))
print(a) #[[0.86466472 0.95885404 0.93206312]
 [0.81325296 0.90699156 0.88020112]
 [0.7618412  0.85058954 0.82380866]]


#生成一个2x4的随机韦伯分布数组，形状参数为1
a = np.random.weibull(1, (2, 4))
print(a) #[[0.86466472 0.95885404 0.93206312 0.81325296]
 [0.90699156 0.88020112 0.7618412  0.85058954]]

#pandas中的Series对象
#Series对象是pandas中最基本的数据结构，它可以看作是一维数组，类似于一维数组的字典。

#Series
#Series对象可以包含不同的数据类型，包括整数、浮点数、字符串、布尔值等。

#创建Series对象
import pandas as pd
obj=pd.Series([4,7,-5,3])
obj.values
#array([ 4,  7, -5,  3])
obj.index
#创建索引序列
obj2=pd.Series([ 4,  7, -5,  3],index=['a','b','c','d'])
obj2
obj2.index
#索引序列为['a', 'b', 'c', 'd']
#访问Series对象
obj[0]
#4
obj2['a']
#4
#Series对象可以进行算术运算
obj3=obj2+obj
obj3
#索引序列为['a', 'b', 'c', 'd']
#数据为[ 8, 10, -2,  6]
#Series对象可以进行逻辑运算
obj4=obj2>0
obj4
#索引序列为['a', 'b', 'c', 'd']
#数据为[ True,  True, False,  True]
#Series对象可以进行统计运算
obj2*2
import numpy as np
np.exp(obj2)
obj2.mean()
#2.5
obj2.std()
#1.5811388300841898
obj2.describe()
#count    4.000000
#mean     2.500000
#std      1.581139
#min      4.000000
#25%      2.250000
#50%      2.500000
#75%      2.750000
#max      4.000000
#dtype: float64
#Series对象可以进行数据选择
obj2[obj2>0]
#索引序列为['a', 'b', 'd']
#数据为[ 4,  7,  3]
#Series对象可以进行数据过滤
obj2[obj2>2]
#索引序列为['a', 'b', 'd']
#数据为[ 4,  7,  3]
#Series对象可以进行数据排序
obj2.sort_values()
#索引序列为['d', 'c', 'b', 'a']
#数据为[ 3, -5,  4,  7]
#Series对象可以进行数据分组
obj2.groupby(obj2>2)
#<pandas.core.groupby.generic.SeriesGroupBy object at 0x000001F2F7F2D240>
#可以通过.groups查看分组结果
obj2.groupby(obj2>2).groups
#{True: ['a', 'b', 'd'], False: ['c']}

#用字典生成Series对象
d={'a':1,'b':2,'c':3}
obj3=pd.Series(d)
obj3
#索引序列为['a', 'b', 'c']
#数据为[1, 2, 3]

#生成预想的索引顺序
obj4=pd.Series(d,index=['s','c','a'])
obj4
#NaN是因为没有找到索引为's'的元素，所以用NaN填充
#isnull()方法可以查看缺失值
obj4.isnull()
#notnull()方法可以查看非缺失值
obj4.notnull()

#自动对齐索引
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['a','b','d'])
s1+s2
#series对象和索引的name属性可以设置名称
s1.name='snoopy'
s2.name='s2'
s1.index.name='usj'
s2.index.name='usj'
s1
#按位置赋值
s1[0]=10
s1
#按索引赋值
s1['a']=100
s1

#dataframe
#dataframe对象是pandas中二维数据结构，类似于Excel表格。

#创建dataframe对象
import pandas as pd
data={'name':['Alice','Bob','Charlie'],'age':[25,30,20]}
df=pd.DataFrame(data)
df
#索引序列为[0, 1, 2]
#列名序列为['name', 'age']
#数据为[['Alice', 25], ['Bob', 30], ['Charlie', 20]]

#head()方法可以查看前几行数据
df.head()
#head(n)方法可以查看前n行数据
df.head(3)
#tail()方法可以查看后几行数据
df.tail()
#tail(n)方法可以查看后n行数据
df.tail(2)
#指定列顺序
df[['age','name']]
#如果传的列不存在于字典中,会出现缺失值NAN
frame=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},columns=['name','age','gender'])
frame
#检索dataframe对象
frame['name']
frame.loc[1]
frame.loc[1,'age']
frame.loc[1,'name']
#赋值
frame['gender']='female'
frame['data']=np.arange(3)
frame
#将series对象合并到dataframe对象
s=pd.Series([10,20],index=[0,1])
frame['赋值列']=s
frame
#将dataframe对象合并到dataframe对象
df=pd.concat([df,s],axis=1)
df
#创建布尔值列
df['bool']=df['age']>25
df
frame['bool']=frame.gender=='female'
frame
#布尔值列可以进行逻辑运算
frame[frame['bool']]
#del方法可以删除列
del frame['data']
#drop_duplicates方法可以删除重复行
df.drop_duplicates()
#dropna方法可以删除缺失值
df.dropna()
#drop方法可以删除行
df.drop(1,inplace=True)
df
#reset_index()方法可以重置索引
df.reset_index(inplace=True)
df
#rename方法可以重命名索引
df.rename(columns={'index':'编号'},inplace=True)
df
#set_index方法可以设置索引
df.set_index('编号',inplace=True)
df
#groupby方法可以对dataframe对象进行分组
df.groupby('name')['age'].mean()
#unstack()方法可以将dataframe对象展开
df.unstack()
#stack()方法可以将dataframe对象堆叠
df.stack()
#pivot()方法可以将dataframe对象转置
df.pivot(index='name',columns='编号',values='age')
#merge方法可以合并dataframe对象
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
df3=pd.merge(df1,df2,on='name')
df3
#concat方法可以合并dataframe对象
df4=pd.concat([df1,df2],axis=1)
df4
#apply方法可以对dataframe对象进行自定义函数操作
df.apply(lambda x:x.max()-x.min())
#applymap方法可以对dataframe对象中的每个元素进行自定义函数操作
df.applymap(lambda x:x*2)
#to_csv方法可以将dataframe对象保存为csv文件
df.to_csv('test.csv')
#to_excel方法可以将dataframe对象保存为excel文件
df.to_excel('test.xlsx')
#read_csv方法可以读取csv文件
df=pd.read_csv('test.csv')
df
#read_excel方法可以读取excel文件
df=pd.read_excel('test.xlsx')
df
#dataframe转置
df.T
#包含Series的字典转为dataframe对象
d={'name':pd.Series(['Alice','Bob','Charlie']),'age':pd.Series([25,30,20])}
d
df=pd.DataFrame(d)
df
#dataframe对象转为字典
d=df.to_dict()
d
#dataframe对象转为numpy数组
arr=df.values
arr

#指定列名
df['age']
#指定行条件
df[df['age']>25]
#指定列条件
df[df['name'].isin(['Alice','Bob'])]
#指定行和列条件
df[(df['age']>25) & (df['name'].isin(['Alice','Bob']))]
#指定行和列条件，并排序
df[(df['age']>25) & (df['name'].isin(['Alice','Bob']))].sort_values(by='age')
#指定行和列条件，并排序，指定升序或降序
df[(df['age']>25) & (df['name'].isin(['Alice','Bob']))].sort_values(by='age',ascending=False)
#指定行和列条件，并排序，指定列名
df[(df['age']>25) & (df['name'].isin(['Alice','Bob']))].sort_values(by='age',ascending=False,inplace=True)
#describe()方法可以查看数据概览
df.describe()
#shape属性可以查看dataframe对象的形状
df.shape
#输出为(3, 2)

#reindx()方法可以重新排列索引
df.reindex([1,2,0])
#reindex_like()方法可以重新排列索引，使其与另一个dataframe对象相同
df.reindex_like(df2)
#dropna()方法可以删除缺失值
df.dropna()
#fillna()方法可以填充缺失值
df.fillna(value=0)
#reset_index()方法可以重置索引
df.reset_index(inplace=True)
df
#重命名索引
df.rename(columns={'name':'noname'},inplace=True)
df

#ffill()缺失值向前填充
obj3=pd.Series([1,np.nan,3,np.nan,5],index=list('abcde'))
obj3
obj3.fillna(method='ffill')
#bfill()缺失值向后填充
obj3.fillna(method='bfill')
#interpolate()缺失值按线性插值
obj3.interpolate()

#drop()删除指定条目
new_obj=obj3.drop(['b','d'])
new_obj
#isin()判断是否在指定列表中
new_obj.isin(['a','c'])
#nunique()统计唯一值个数
new_obj.nunique()
#value_counts()统计各值出现次数
new_obj.value_counts()
#apply()自定义函数操作
new_obj.apply(lambda x:x*2)
#applymap()自定义函数操作，对每个元素操作
new_obj.applymap(lambda x:x*2)
#to_dict()转为字典
new_obj.to_dict()
#to_list()转为列表
new_obj.to_list()
#to_numpy()转为numpy数组
new_obj.to_numpy()
#to_string()转为字符串
new_obj.to_string()
#to_csv()保存为csv文件
new_obj.to_csv('test.csv')
#to_excel()保存为excel文件
new_obj.to_excel('test.xlsx')
#read_csv()读取csv文件
new_obj=pd.read_csv('test.csv',index_col=0)
new_obj
#read_excel()读取excel文件
new_obj=pd.read_excel('test.xlsx',index_col=0)
new_obj
#轴向上删除条目
data={'name':['Alice','Bob','Charlie'],'age':[25,30,20]}
df=pd.DataFrame(data)
df
df.drop('a',axis=0)#删除行
df.drop('age',axis=1)#删除列
#根据行标签删除
df.drop(['a','c'],axis=0)
#根据列标签删除
df.drop(['age'],axis=1)
#找到满足条件的行的索引 删除这些行
rows_to_drop = df[df['age'] > 25].index
df = df.drop(rows_to_drop, axis=0)
df
#布尔值数组切片选择数据
df['age'] > 25
df[df['age'] > 25]
df[df['age'] > 25]=0
df

#loc选择数据
#loc 是基于标签的索引方式。
#loc[[row_indexer],[col_indexer]]
data=pd.DataFrame(np.arange(16).reshape(4,4),
                  index=['a','b','c','d'],
                  columns=['w','x','y','z'])
data
data.loc[['a'],['w']]
data.loc[['a','c'],['w','y']]
data.loc['a':'c',['w','y']]
data.loc['a':'c',['w','y']]=0
data
#iloc选择数据
#iloc 是基于位置的索引方式。
#iloc[[row_indexer],[col_indexer]]
data.iloc[[0],[0]]
data.iloc[[0,2],[0,2]]
data.iloc[0:2,[0,2]]
data.iloc[0:2,[0,2]]=0
data.iloc[:,:3][data.y>5]
data

#数据对齐
#add和fill_value用于填充缺失值
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['a','b','d'])
s1+s2
s1.add(s2,fill_value=0)
#join用于合并两个dataframe对象
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
df1.join(df2,on='name')
#merge用于合并两个dataframe对象
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
pd.merge(df1,df2,on='name')
#concat用于合并两个dataframe对象
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
pd.concat([df1,df2],axis=1)
#merge_asof用于合并两个dataframe对象，并根据时间对齐
df1=pd.DataFrame({'time':[1,2,3,4,5],'value1':[1,2,3,4,5]})
df2=pd.DataFrame({'time':[2,3,4,5,6],'value2':[2,3,4,5,6]})
pd.merge_asof(df1,df2,on='time')
#merge_ordered用于合并两个dataframe对象，并根据索引对齐
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
pd.merge_ordered(df1,df2,on='name')

#灵活算数方法
#add用于两个Series对象相加
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['a','b','d'])
s1.add(s2,fill_value=0)
#sub用于两个Series对象相减
s1.sub(s2,fill_value=0)
#mul用于两个Series对象相乘
s1.mul(s2,fill_value=1)
#div用于两个Series对象相除
s1.div(s2,fill_value=1)
#pow用于Series对象求幂
s1.pow(2)
#mean用于Series对象求平均值
s1.mean()
#median用于Series对象求中位数
s1.median()
#std用于Series对象求标准差
s1.std()
#var用于Series对象求方差
s1.var()
#quantile用于Series对象求分位数
s1.quantile(0.5)
#cumsum用于Series对象求累计和
s1.cumsum()
#cumprod用于Series对象求累计积
s1.cumprod()
#diff用于Series对象求差分
s1.diff()
#pct_change用于Series对象求百分比变化
s1.pct_change()
#rank用于Series对象求排序
s1.rank()
#fillna用于Series对象填充缺失值
s1.fillna(value=0)
#dropna用于Series对象删除缺失值
s1.dropna()
#clip用于Series对象裁剪
s1.clip(lower=1,upper=3)
#round用于Series对象四舍五入
s1.round(2)
#apply用于Series对象自定义函数操作
s1.apply(lambda x:x*2)

#dataframe对象算数方法
#add用于两个dataframe对象相加
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'name':['Alice','Bob','Charlie'],'gender':['female','male','male']})
df1.add(df2,fill_value=0)
#sub用于两个dataframe对象相减
df1.sub(df2,fill_value=0)
#mul用于两个dataframe对象相乘
df1.mul(df2,fill_value=1)
#div用于两个dataframe对象相除
df1.div(df2,fill_value=1)
#pow用于dataframe对象求幂
df1.pow(2)
#mean用于dataframe对象求平均值
df1.mean()
#median用于dataframe对象求中位数
df1.median()
#std用于dataframe对象求标准差
df1.std()
#var用于dataframe对象求方差
df1.var()
#quantile用于dataframe对象求分位数
df1.quantile(0.5)
#cumsum用于dataframe对象求累计和
df1.cumsum()
#cumprod用于dataframe对象求累计积
df1.cumprod()
#diff用于dataframe对象求差分
df1.diff()
#pct_change用于dataframe对象求百分比变化
df1.pct_change()
#rank用于dataframe对象求排序
df1.rank()
#fillna用于dataframe对象填充缺失值
df1.fillna(value=0)
#dropna用于dataframe对象删除缺失值
df1.dropna()
#clip用于dataframe对象裁剪
df1.clip(lower=1,upper=3)
#round用于dataframe对象四舍五入
df1.round(2)
#apply用于dataframe对象自定义函数操作
df1.apply(lambda x:x*2)
#applymap用于dataframe对象自定义函数操作，对每个元素操作
df1.applymap(lambda x:x*2)
#corr用于dataframe对象求相关系数
df1.corr()
#cov用于dataframe对象求协方差
df1.cov()
#corrwith用于dataframe对象求两个列之间的相关系数
df1.corrwith(df2['gender'])
#rank用于dataframe对象求排序
df1.rank()
#rank用于dataframe对象求排序
df1.rank()
#rank用于dataframe对象求排序
df1.rank()
#rank用于dataframe对象求排序
df1.rank()

#dataframe和series的合并
#concat用于合并dataframe和series
s1=pd.Series([1,2,3],index=['a','b','c'])
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
pd.concat([s1,df1],axis=1)
#merge用于合并dataframe和series
s1=pd.Series([1,2,3],index=['a','b','c'])
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
pd.merge(df1,s1,left_index=True,right_index=True)
#join用于合并dataframe和series
s1=pd.Series([1,2,3],index=['a','b','c'])
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df1.join(s1,on='name')
#dataframe和series减法
#sub用于dataframe和series相减
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
s1=pd.Series([1,2,3],index=['a','b','c'])
df1.sub(s1,fill_value=0)
#dataframe和series乘法
#mul用于dataframe和series相乘
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
s1=pd.Series([1,2,3],index=['a','b','c'])
df1.mul(s1,fill_value=1)
#dataframe和series除法
#div用于dataframe和series相除
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
s1=pd.Series([1,2,3],index=['a','b','c'])
df1.div(s1,fill_value=1)
#dataframe和series的合并
#concat用于合并dataframe和series
s1=pd.Series([1,2,3],index=['a','b','c'])
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
pd.concat([s1,df1],axis=1)
#merge用于合并dataframe和series
s1=pd.Series([1,2,3],index=['a','b','c'])
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]})

#广播机制
#广播机制的实现原理是：numpy会自动将数组的形状进行扩展，使得数组的形状相同，然后再进行算术运算。
#实例
a=np.array([1,2,3])
b=np.array([4,5,6])
a+b
#2. 数组的形状不同，但可以进行广播的情况。
#实例
a=np.array([[1,2,3],[4,5,6]])
b=np.array([7,8,9])
a+b

#排序和排名
#sort_index()用于按行或索引排序 默认升序
df=pd.DataFrame({'a':['Alice','Bob','Charlie'],'b':[25,30,20]},index=[3,2,1])
df.sort_index()
df.sort_index(axis=1)
#降序排序
df.sort_index(axis=0,ascending=False)

#sort_values()用于按series的值排序 默认升序
df=pd.DataFrame({'NO':['a','b','c'],'age':[25,30,20]})
df.sort_values(by='age')
df.sort_values(by='NO')
#对多列排序
df.sort_values(by=['NO','age'])
#降序排序
df.sort_values(by='age',ascending=False)
#rank()用于排名 对于每一列，rank() 方法会计算每个元素的排名。 
df=pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9,10],'b':[10,9,8,7,6,5,4,3,2,1]})
df.rank()
#降序排序
df.rank(ascending=False)
df.rank(axis=1)
df.rank(method='average')
df.rank(method='min')
df.rank(method='max')
df.rank(method='first')
df.rank(method='dense')

#描述性统计
#describe()用于对数据进行汇总统计
df=pd.DataFrame({'a':[1,2,3,4,5,6,7,8,9,10],'b':[10,9,8,7,6,5,4,3,2,1]})
df.describe()
#只显示数值型数据
df.describe(include='all')
#只显示数值型数据，指定百分比
df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9])
#只显示数值型数据，指定百分比，指定列
df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9],include='all',exclude=['b'])
#只显示数值型数据，指定百分比，指定列，指定汇总统计量
df.describe(percentiles=[0.1,0.25,0.5,0.75,0.9],include='all',exclude=['b'],
             stats=['mean','std','min','max'])

df.sum()#列上加和
df.sum(axis=1)#行上加和
df.mean()#列上平均值
df.median()#列上中位数
df.std()#列上标准差
df.var()#列上方差
df.min()#列上最小值
df.max()#列上最大值
df.count()#列上非空值个数
df.quantile(0.5)#列上中位数
df.cumsum()#列上累计和
df.cumprod()#列上累计积
df.diff()#列上差分
df.pct_change()#列上百分比变化
df.fillna(value=0)#列上填充缺失值
df.dropna()#列上删除缺失值
df.clip(lower=1,upper=3)#列上裁剪
df.round(2)#列上四舍五入
df.corr()#列上相关系数
df.cov()#列上协方差

#dataframe的相关性分析
#corr()用于计算两列之间的相关系数
a=np.array([1,2,3,4,5])
b=np.array([5,6,7,8,9])
np.corrcoef(a,b)[0,1]
#cov()用于计算两列之间的协方差
np.cov(a,b)[0,1]

#文本格式数据的读写
#read_csv()用于读取csv文件
df=pd.read_csv('test.csv')
#read_table()用于读取txt文件
df=pd.read_table('test.txt')
#to_csv()用于将数据写入csv文件
pd.to_csv('test1.csv')
#to_excel()用于将数据写入excel文件
pd.to_excel('test1.xlsx')
#to_json()用于将数据写入json文件
pd.to_json('test1.json')
#to_html()用于将数据写入html文件
pd.to_html('test1.html')
#to_latex()用于将数据写入latex文件
pd.to_latex('test1.tex')
#to_string()用于将数据写入字符串
pd.to_string()
pd.read_hdf()
pd.read_stata()
pd.read_sas()
pd.read_pickle()
pd.read_sql()
pd.read_gbq()


#数据清洗
#isnull()用于检测缺失值
df.isnull()
#notnull()用于检测非缺失值
df.notnull()
#dropna()用于删除缺失值
df.dropna()
#fillna()用于填充缺失值
df.fillna(value=0)
#replace()用于替换值
df.replace(to_replace=0,value=1)
#astype()用于转换数据类型   
df.astype(int)

#过滤缺失值
df.dropna()
df.dropna(how='all')#删除索引值均为NA的行
df.dropna(how='any')#删除有缺失值的行
df.dropna(subset=['a'])#删除a列中缺失值的行
df.dropna(thresh=2)#删除至少有2个非缺失值的行
df.dropna(axis=1)#删除有缺失值的列
df.dropna(thresh=2)#删除非缺失值的数量小于2的行。

#补全缺失值
df.fillna(value=0)
df.fillna(method='ffill',limit=2)#前向填充,最多填充2次。
df.fillna(1:0.5,2:0)#不同列的不同值填充
df.fillna(method='bfill')#后向填充
df.fillna(method='pad')#填充前后值
df.fillna(method='backfill')#后向填充
df.fillna(method='nearest')#最接近的前一个值填充
df.fillna(method='mean')#列上平均值填充
df.fillna(method='median')#列上中位数填充
df.iloc[0:2,0:2]=np.nan
data=pd.Series([1,2,np.nan,4,np.nan,6])
data.fillna(data.mean())#用列上平均值或中位数median填充缺失值

#删除重复值
df.duplicates()#返回一个布尔值Series
df.drop_duplicates()
df.drop_duplicates(subset=['a'])#删除a列中重复值
df.drop_duplicates(keep='last')#保留最后一个重复值
df.drop_duplicates(keep='first')#保留第一个重复值
#删除指定列
df.drop(['a'],axis=1)
#删除指定行
df.drop([0,1])
#删除指定条件
df[df['a']>1]

#使用映射进行数据转换
#map()用于映射数据
#假设收集到一组肉类数据，项目为品名和盎司数，数据如下：
data={'品名':['培根','牛腩','羊腿'],'盎司数':[100,200,150]}
df=pd.DataFrame(data)
df
#构造映射字典
mapping={'培根':'pig','牛腩':'beef','羊腿':'mutton'}
#使用map()函数进行数据转换
df['品名'].map(mapping)
#利用映射生成新的列名为动物
df['动物']=df['品名'].map(mapping)
df

#替代值
#replace()用于替代指定值
df.replace(100,300)
df.replace([150,200],400)
df.replace([150,200],[300,400])
#通过字典进行替代
mapping={100:300,150:400,200:500}
df.replace(mapping)

#重命名轴索引
df.rename(index={0:'first',1:'second',2:'third'},inplace=True)#inplace=True表示修改原数据
df
df.rename(index={0:'first',1:'second',2:'third'},columns={'品名':'name','盎司数':'weight'})

#离散化和分箱
#cut()用于离散化
data=np.array([1,2,3,4,5,6,7,8,9,10])
pd.cut(data,bins=3)
pd.cut(data,bins=[0,3,6,9,12])
pd.cut(data,bins=[0,3,6,9,12],labels=['0-3','3-6','6-9','9-12'])
#qcut()用于分箱
pd.qcut(data,q=3)
pd.qcut(data,q=[0,0.33,0.66,1])

ages=[20,22,25,27,30,35,40,45,50,55,60,65]
bins=[18,25,35,60,100]
cats=['Youth','Adult','Senior']
pd.cut(ages,bins,labels=cats)
pd.qcut(ages,4,labels=cats)

#分层索引
data=pd.Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]])
data
data.index
data['a']
data['a':'c']
data.loc['a']
data.loc[['a','c']]
data.loc['a':'c',1]
data.loc['a':'c',1:3]
data.unstack()#重新排列
data.unstack(level=0)
data.unstack(level=1)
data.unstack().stack()#stack()是unstack()的逆操作
#dataframe每个轴都能分层索引
data=pd.DataFrame(np.random.randn(10,4),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,1,2]],columns=[['Ohio','Ohio','Colorado','Colorado'],['Green','Red','Green','Red']])
data
data.index
data.columns
#分层的层级名称
data.index.names=['key1','key2']
data.columns.names=['state','color']
#通过层级名称访问数据
data.loc['a']
data.loc['a':'c']
data.loc['a':'c',('Ohio','Green')]
#通过层级名称访问数据
data.groupby(level='key1').mean()
data.groupby(level='key2')['Red'].mean()
#重排序和层级排序
data.swaplevel(0,1)
data.swaplevel('key1','key2')
data.swaplevel(0,1,axis=0)#列向上层级交换
data.swaplevel(0,1,axis=1)#行向上层级交换
data.sort_index(level=0)#按第一层（key1）排序
data.sort_index(level=1)#按第二层（key2）排序
data.sort_index(level=1,axis=1)#按行向，第一层（key1）排序
data.sort_index(level=1,axis=0)#按列向，第二层（key1）排序
data.swaplevel(0,1,axis=1).sort_index(level=1,axis=0)#先行向交换层级，再列向按第二层（key2）排序
#层级聚合sum
data.groupby(level='key1').sum()#默认按列向
data.groupby(level=1,axis=1).sum()#按行向第二层
#聚合mean
data.groupby(level='key1').mean()
#聚合max
data.groupby(level='key1').max()
#聚合min
data.groupby(level='key1').min()
#聚合std
data.groupby(level='key1').std()
#聚合var
data.groupby(level='key1').var()
#聚合count
data.groupby(level='key1').count()
#聚合first
data.groupby(level='key1').first()
#聚合last
data.groupby(level='key1').last()
#聚合prod
data.groupby(level='key1').prod()
#聚合size
data.groupby(level='key1').size()
#聚合median
data.groupby(level='key1').median()
#聚合quantile
data.groupby(level='key1').quantile(0.5)

#使用列作为索引
#假设有如下数据：
data={'name':['Alice','Bob','Charlie'],'age':[25,30,20]}
df=pd.DataFrame(data,index=['a','b','c'])
df
#将name列作为索引
df.set_index('name',inplace=True)
df
#reset_index()用于重置索引
df.reset_index()
df
#将age列作为列索引
#inplace=True 表示修改原数据
#append=True 用于指定在设置新索引时是否保留原来的索引。
#drop=True 用于指定是否删除原来的索引。
df.set_index('age',append=False,inplace=True,drop=False)
df

#数据库风格的dataframe连接
#假设有两个表：
#表1：
#id | name | age
#1  | Alice| 25
#2  | Bob  | 30
#3  | Charlie| 20
#表2：
#id | score
#1  | 80
#2  | 90
#3  | 70
#使用pd.merge()函数进行连接：
df1=pd.DataFrame({'id':[1,2,3],'name':['Alice','Bob','Charlie'],'age':[25,30,20]})
df2=pd.DataFrame({'id':[1,2,3],'score':[80,90,70]})
pd.merge(df1,df2,on='id')
#使用left_on和right_on参数指定连接列：
#left_on='id'指定 df1中用于合并的列名。
pd.merge(df1,df2,left_on='id',right_on='id')
#使用how参数指定连接方式：
pd.merge(df1,df2,on='id',how='left')#保留左边表的全部数据
pd.merge(df1,df2,on='id',how='right')#保留右边表的全部数据
pd.merge(df1,df2,on='id',how='inner')#保留交集数据
pd.merge(df1,df2,on='id',how='outer')#保留全部数据并对齐
#使用suffixes参数指定连接后重复列名的后缀：
pd.merge(df1,df2,on='id',suffixes=('_left','_right'))
#使用indicator参数添加一个列，值为'left_only'、'right_only'或'both'表示每一行的数据来源：
pd.merge(df1,df2,on='id',how='outer',indicator=True)
#使用left_index和right_index参数指定索引连接：
df1=pd.DataFrame({'id':[1,2,3],'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'id':[1,2,3],'score':[80,90,70]},index=['a','b','c'])
pd.merge(df1,df2,left_index=True,right_index=True)
#使用left_on和right_index参数指定连接列和索引：
pd.merge(df1,df2,left_on='id',right_index=True)
#使用left_index和right_on参数指定索引和连接列：
pd.merge(df1,df2,left_index=True,right_on='id')
#使用suffixes参数指定索引的列名后缀：
pd.merge(df1,df2,left_index=True,right_index=True,suffixes=('_left','_right'))

#根据索引合并
#假设有两个表：
#表1：
#id | name | age
#1  | Alice| 25
#2  | Bob  | 30
#3  | Charlie| 20
#表2：
#id | score
#1  | 80
#2  | 90
#3  | 70
#使用pd.merge()函数进行连接：
df1=pd.DataFrame({'id':[1,2,3],'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'id':[1,2,3],'score':[80,90,70]})
pd.merge(df1,df2,left_on='id',right_index=True,how='outer')

#join()函数
#join()函数用于合并两个Series或DataFrame对象，根据索引进行连接。
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['c','d','e'])
s1.join(s2)
#join()函数也可以用于合并多个Series或DataFrame对象，根据索引进行连接。
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'score':[80,90,70]},index=['c','d','e'])
df1.join(df2)
#join()函数也可以用于合并多个Series或DataFrame对象，根据索引进行连接。
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'score':[80,90,70]},index=['c','d','e'])
df3=pd.DataFrame({'height':[170,180,160]},index=['a','b','c'])
df1.join([df2,df3])

#轴向连接
#np.concatenate()函数也可以用于连接多个数组，根据轴进行连接。
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[7,8,9],[10,11,12]])
np.concatenate([a1,a2],axis=1)
#concat()函数用于连接两个或多个Series或DataFrame对象，根据轴进行连接。
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['c','d','e'])
pd.concat([s1,s2])
#concat()函数也可以用于连接多个Series或DataFrame对象，根据轴进行连接。
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'score':[80,90,70]},index=['c','d','e'])
df3=pd.DataFrame({'height':[170,180,160]},index=['a','b','c'])
pd.concat([df1,df2,df3],axis=1)
pd.concat([df1,df2,df3],axis=1,ignore_index=True)#忽略原索引
pd.concat([df1,df2,df3],axis=1,keys=['df1','df2','df3'],names=['upper','lower'])#为每个对象指定一个key
pd.concat([df1,df2,df3],axis=1,join='outer')    
pd.concat([df1,df2,df3],axis=1,join='inner')    
#append()函数用于在一个Series或DataFrame对象后面添加另一个Series或DataFrame对象。
s1=pd.Series([1,2,3],index=['a','b','c'])
s2=pd.Series([4,5,6],index=['c','d','e'])
s1.append(s2)
#append()函数也可以用于在一个DataFrame对象后面添加另一个DataFrame对象。
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'score':[80,90,70]},index=['c','d','e'])
df1.append(df2)
#np.concatenate()函数可以用于连接两个或多个数组，根据轴进行连接。
a1=np.array([1,2,3])
a2=np.array([4,5,6])
np.concatenate([a1,a2])

#联合(索引)重叠数据
a1=pd.Series([np.nan,4,5,1,2,np.nan],index=['a','b','c','d','e','f'])
a2=pd.Series([8,np.nan,np.nan,np.nan,3,7],index=['f','e','d','c','b','a'])
a1
a2
np.where(pd.isnull(a1),a2,a1)#如果 a1 中的某个元素是 NaN，则选择 a2 中对应的元素；否则，选择 a1 中对应的元素。
a1.combine_first(a2)
#combine_first()函数用于合并两个Series或DataFrame对象，并用另一个Series或DataFrame对象中的值填充缺失值。
df1=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20]},index=['a','b','c'])
df2=pd.DataFrame({'score':[80,90,70]},index=['c','d','e'])
df1.combine_first(df2)#df2中的缺失值用 df1 中的值填充。

#重塑和透视
#stack()函数用于将DataFrame的列转换为行，并生成一个新的层级索引。
df=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20],'score':[80,90,70]})
df
df.stack()#先按行索引再按列索引
df.stack().unstack()
#unstack()函数用于将DataFrame的行转换为列，并生成一个新的层级索引。
df.unstack()#先按列索引再按行索引

#将长透视为宽
#pivot()函数用于将长格式数据转换为宽格式数据。
data=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20],'score':[80,90,70]})
data
data.pivot(index='name',columns='age',values='score')#将name列作为索引，age列作为列索引，score列作为值。
#pivot_table()函数用于将长格式数据转换为宽格式数据，并进行聚合。
data=pd.DataFrame({'name':['Alice','Bob','Charlie','Alice','Bob','Charlie'],'age':[25,30,20,25,30,20],'score':[80,90,70,85,95,65]})
data
data.pivot_table(index='name',columns='age',values='score',aggfunc=np.mean)#将name列作为索引，age列作为列索引，score列作为值，使用np.mean()函数进行聚合。
#unstack()函数可以将pivot_table()函数的结果转换为长格式数据。
data.pivot_table(index='name',columns='age',values='score',aggfunc=np.mean).unstack()
#reset_index()函数可以将pivot_table()函数的结果转换为长格式数据。
data.pivot_table(index='name',columns='age',values='score',aggfunc=np.mean).reset_index()

#将宽透视为长
#melt()函数用于将宽格式数据转换为长格式数据。
data=pd.DataFrame({'name':['Alice','Bob','Charlie'],'age':[25,30,20],'score':[80,90,70]})
data
data.melt(id_vars='name',value_vars=['age','score'])#将name列作为索引，age列和score列作为值。
#unstack()函数可以将melt()函数的结果转换为宽格式数据。
data.melt(id_vars='name',value_vars=['age','score']).unstack()
#pivot()函数可以将melt()函数的结果转换为长格式数据。
data.melt(id_vars='name',value_vars=['age','score']).pivot(index='name',columns='variable',values='value')
#reset_index()函数可以将melt()函数的数据向右移动一列
data.melt(id_vars='name',value_vars=['age','score']).pivot(index='name',columns='variable',values='value').reset_index()

###绘图和可视化matplotlib###
#matplotlib是Python中用于绘图的库。
import matplotlib.pyplot as plt
import numpy as np
data=np.arange(10)
data
plt.plot(data)
plt.show()

fig=plt.figure()#创建图表
ax=fig.add_subplot(2,2,1)#添加子图
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax.plot(data)#data绘制在ax子图中
#k--表示黑色虚线 r-表示红色实线
ax2.plot(data,'k--')
ax3.plot(data,'r-')
plt.show()

# 创建图形和子图
fig, (ax, ax2, ax3) = plt.subplots(3, 1)
# 在指定的子图上绘图
ax3.plot(np.random.randn(50).cumsum(), 'k--')  # 绘制随机数累计和的折线图
 # 绘制直方图 表示 100 个随机数的分布，分成 20 个区间，颜色为黑色，透明度为 0.3。
ax.hist(np.random.randn(100), bins=20, color='k', alpha=0.3)  
#绘制一个散点图，表示 30 个数据点的分布，每个点的 y 值在 x 值的基础上加上一个随机偏移3 * np.random.randn(30)。
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))  # 绘制散点图
# 显示图形
plt.show()

#subplots()选项
fig, axes = plt.subplots(2, 3, figsize=(12, 8))#创建2行3列的图形，figsize设置图形大小
#在指定的子图上绘图
axes[0, 0].plot(np.random.randn(50).cumsum(), 'k--')  # 绘制随机数累计和的折线图
axes[1, 2].hist(np.random.randn(100), bins=20, color='k', alpha=0.3)  
axes[0, 1].scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))  # 绘制散点图
# 显示图形
plt.show()

#plt.subplots() 的参数
#nrows, ncols, sharex, sharey, subplot_kw, gridspec_kw, **fig_kw用法
fig, axes = plt.subplots(2, 3, figsize=(12, 8), sharex=True, sharey=True)
#nrows=2 和 ncols=3 表示创建一个包含 2 行 3 列子图的图形。
#sharex=True 和 sharey=True 表示子图共享 x 轴和 y 轴。
#figsize=(12, 8) 设置图形大小为 12 宽 8 高。
#subplot_kw={'xticks': [], 'yticks': []} 表示子图不显示坐标轴刻度。
#gridspec_kw={'wspace': 0.4, 'hspace': 0.3} 表示设置子图之间的间距。
#fig_kw={'facecolor': 'white'} 表示设置背景颜色为白色。

#设置子图标题
axes[0, 0].set_title('子图1')
#设置子图标签
axes[0, 0].set_xlabel('横坐标标签1')
axes[0, 1].set_ylabel('纵坐标标签3')
#设置子图范围
axes[0, 0].set_xlim(0,10)
axes[0, 1].set_ylim(0,10)
#设置子图刻度
axes[0, 0].set_xticks([0,2,4,6,8,10])
axes[1, 2].set_yticks([0,2,4,6,8,10])
#设置子图网格线
axes[1, 2].grid(True)
#设置子图背景颜色
axes[1, 2].set_facecolor('white')
#设置子图边框颜色
axes[0, 0].spines['bottom'].set_color('black')
axes[1, 2].spines['top'].set_color('black')
axes[0, 1].spines['right'].set_color('black')
axes[0, 0].spines['left'].set_color('black')

#设置seaborn-whitegrid样式
plt.style.use('seaborn-whitegrid')#设置白色背景和网格线
plt.plot(data)
plt.show()
#设置ggplot样式
plt.style.use('ggplot')#设置ggplot样式
plt.plot(data)
plt.show()
#设置图表颜色
plt.plot(data,color='r')
#设置线宽
plt.plot(data,lw=2)
#设置线型
plt.plot(data,ls='--')
#设置标记
plt.plot(data,marker='o')
#设置标记大小
plt.plot(data,ms=10)
#设置标记颜色
plt.plot(data,mfc='r')
#设置标记边框颜色
plt.plot(data,mec='b')
#设置标记边框宽度
plt.plot(data,mew=2)
#设置坐标轴标签
plt.xlabel('横坐标标签')
plt.ylabel('纵坐标标签')
#设置图例
plt.legend(['数据1','数据2'])
#设置坐标轴范围
plt.xlim(0,10)
plt.ylim(0,10)
#设置坐标轴刻度
plt.xticks([0,2,4,6,8,10])
plt.yticks([0,2,4,6,8,10])
ax.set_xticks([0,2,4,6,8,10])
ax.set_yticks([0,2,4,6,8,10])
#设置坐标轴网格线
#设置图表标题
plt.title('图表标题')
#设置图表注释
plt.text(2,8,'注释内容')
#设置网格线
plt.grid(True)
#设置背景颜色
plt.rcParams['axes.facecolor']='white'
#设置边框颜色
plt.rcParams['axes.edgecolor']='black'
#设置坐标轴颜色
plt.rcParams['axes.labelcolor']='black'
#设置字体大小
plt.rcParams['font.size']=14
#设置字体颜色
plt.rcParams['text.color']='black'
#设置图形大小
plt.rcParams['figure.figsize']=(10,8)

#绘制带标记的折线图
from numpy.random import randn
plt.plot(randn(30).cumsum(),'ko--')
plt.show()

plt.plot(randn(30).cumsum(),color='k',linestyle='dashed',marker='o')
plt.show()

#添加图例
plt.plot(randn(30).cumsum(),'ko--',label='one')
plt.plot(randn(30).cumsum(),'k^--',label='2')
plt.legend(loc='best')#设置图例位置
plt.show()

#折线图
import numpy as np
import matplotlib.pyplot as plt
s=pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
s.plot()
plt.show()

df=pd.DataFrame(np.random.randn(10,4).cumsum(0),
                columns=['A','B','C','D'],
                index=np.arange(0,100,10))
df.plot()
plt.show()

#Series.plot()方法参数
#kind:图表类型，默认折线图，可选值：'line'、'bar'、'barh'、'hist'、'box'、'kde'、'density'、'area'、'pie'、'scatter'
#ax:matplotlib.axes.Axes对象，用于指定绘图区域
#subplots:布尔值，是否创建子图
#sharex:布尔值，是否共享x轴
#sharey:布尔值，是否共享y轴
#layout:整数或(整数,整数)，子图布局
#figsize:元组，图形大小
#use_index:布尔值，是否使用索引值
#title:字符串，图表标题
#grid:布尔值，是否显示网格线
#legend:布尔值或字符串，是否显示图例，'best'表示自动选择位置
#style:字符串或列表，线条风格
#logx:布尔值，是否对x轴使用对数刻度
#logy:布尔值，是否对y轴使用对数刻度
#loglog:布尔值，是否对x轴和y轴同时使用对数刻度
#xticks:列表或元组，x轴刻度
#yticks:列表或元组，y轴刻度
#xlim:元组或列表，x轴范围
#ylim:元组或列表，y轴范围
#rot:整型，x轴刻度旋转角度
#fontsize:整型，字体大小
#colormap:字符串，颜色映射
#table:布尔值，是否显示数据框
#yerr:列表或元组，表示误差范围
#xerr:列表或元组，表示误差范围
#label:字符串或列表，数据标签
#secondary_y:布尔值或列表，是否将数据绘制在右侧y轴
#sort_columns:布尔值，是否对数据框的列排序
#mark_right:布尔值，是否将数据框的右侧数据绘制在右侧y轴


#DataFrame.plot()方法参数
#kind:图表类型，默认折线图，可选值：'line'、'bar'、'barh'、'hist'、'box'、'kde'、'density'、'area'、'pie'、'scatter'
#ax:matplotlib.axes.Axes对象，用于指定绘图区域
#subplots:布尔值，是否创建子图
#sharex:布尔值，是否共享x轴
#sharey:布尔值，是否共享y轴
#layout:整数或(整数,整数)，子图布局
#figsize:元组，图形大小
#use_index:布尔值，是否使用索引值
#title:字符串，图表标题
#grid:布尔值，是否显示网格线
#legend:布尔值或字符串，是否显示图例，'best'表示自动选择位置
#style:字符串或列表，线条风格
#logx:布尔值，是否对x轴使用对数刻度
#logy:布尔值，是否对y轴使用对数刻度
#loglog:布尔值，是否对x轴和y轴同时使用对数刻度
#xticks:列表或元组，x轴刻度
#yticks:列表或元组，y轴刻度
#xlim:元组或列表，x轴范围
#ylim:元组或列表，y轴范围
#rot:整型，x轴刻度旋转角度
#fontsize:整型，字体大小
#colormap:字符串，颜色映射
#table:布尔值，是否显示数据框
#yerr:列表或元组，表示误差范围
#xerr:列表或元组，表示误差范围
#label:字符串或列表，数据标签
#secondary_y:布尔值或列表，是否将数据绘制在右侧y轴
#sort_columns:布尔值，是否对数据框的列排序
#mark_right:布尔值，是否将数据框的右侧数据绘制在右侧y轴

#垂直柱状图
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,11)
y=np.random.randint(1,100,10)
plt.bar(x,y)
plt.show()
#水平柱状图
plt.barh(x,y)
plt.show()

#绘制多种柱状图
#fig 对象： fig 是整个图形的容器。axes 是一个包含子图的数组。你可以通过这个对象来设置图形的各种属性，比如大小、标题等
fig, axes = plt.subplots(2, 1)#表示创建了一个新的图形，并返回一个 2 行 1 列的子图的数组
data=pd.Series(np.random.rand(16),index=list('abcdefghijklmnop'))
data.plot.bar(ax=axes[0],color='k',alpha=0.7)#ax 参数用于指定绘图的子图（Axes 对象）。
data.plot.barh(ax=axes[1],color='b',alpha=0.7)#alpha 参数用于设置柱状图的透明度。
plt.show()

#dataframe中,柱状图将每一行的数据绘制成一组柱状图
df=pd.DataFrame(np.random.rand(10,4),
                index=list('abcdefghij'),
                columns=list('ABCD'))
df
df.plot.bar()
plt.show()
#dataframe堆积柱状图
df.plot.bar(stacked=True)
plt.show()

#使用seaborn计算百分比并绘制柱状图
import seaborn as sns
tips=sns.load_dataset('tips')
tips.head()
tips['tip_pct']=(tips['tip']/tips['total_bill'])*100
tips.head()
sns.barplot(x='day',y='tip_pct',data=tips,palette='coolwarm')#绘制水平柱状图，可以使用 orient='h'
plt.show()
#hue参数用于通过其他特征分组绘制柱状图
sns.barplot(x='day',y='tip_pct',data=tips,palette='coolwarm',hue='sex')#绘制分组柱状图
plt.show()

#直方图
import numpy as np
import matplotlib.pyplot as plt
tips['tip_pct'].plot.hist(bins=50,alpha=0.5,color='red',edgecolor='black')
plt.show()
#密度图
tips['tip_pct'].plot.density()
plt.show()

#散点图或点图 regplot()
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
tips=sns.load_dataset('tips')
sns.regplot(x='total_bill',y='tip',data=tips)
plt.show()
#使用散点图绘制线性回归线
sns.lmplot(x='total_bill',y='tip',data=tips)
plt.show()
#pairplot()函数绘制数据框的相关性图
import seaborn as sns
sns.pairplot(tips)
plt.show()










#绘制散点图
plt.scatter(x,y)
#绘制折线图
plt.plot(x,y)
#绘制直方图
plt.hist(x)
#绘制条形图
plt.bar(x,y)
#绘制饼图
plt.pie(x)
#设置图表标题
plt.title('图表标题')
#设置图表标签
plt.xlabel('横坐标标签')
plt.ylabel('纵坐标标签')
#设置图例
plt.legend(['数据1','数据2'])
#设置坐标轴范围
plt.xlim(0,10)
plt.ylim(0,10)
#设置坐标轴刻度
plt.xticks([0,2,4,6,8,10])
plt.yticks([0,2,4,6,8,10])
