#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-16 12:27:37
# @Author  : mohailang (1198534595@qq.com)


# 基于 python2.7
# 可以通过 help()函数在解释器中获得帮助
# dir()可以得到对象的所有方法和属性
# python 一切皆是对象
import math
from time import ctime, sleep, time
from random import randint
from operator import add, mul
from functools import partial
# import Tkinter


"这是一个在线文档注释"
print("Hello World")
print "Welcome to python2.7"
print "Here are some notes"
print "This is fun"
print 'Yay! Fighting!'
print "I said'Learn somethings everyday'"
print 'I said "Get progress everyday."'
# 在解释器中会以字符串的方式显示‘mohailang’
a = 'mohailang'
print "show string：", a
# 文本输入,而且 raw_input会把所有输入都当做是字符串
num = raw_input("Enter a number:")
print 'your number: %s ' % num
# 所有必须把字符串转化为 int 型才可以进行科学运算
print 'doubling your number: %d ' % (int(num) * 2)
# math.floor得到最接近原数但小于原数的浮点型整数
math.floor(3.6)   # 返回3.0
# input() = eval(raw_input())
# input()要求输入的是一个表达式（如果输入字符串则需要用引号括起来）
# 元组语法上不需要一定带上圆括号
# extend()要求参数必须是可迭代对象，并把里面的元素逐个扩展到原对象中
# append()可传入任何参数，并且是把传入的参数作为一个元素附加到原对象中
a = [1, 2, 3]
b = [1, 2, 3]
a.extend([4, 5])    # a = [1, 2, 3, 4, 5]
print "extend():", a
b.append([4, 5])    # b = [1, 2, 3, [4, 5]]
print "append():", b
# 可变对象执行方法操作是没有返回值的，会在原地直接执行操作，也就是说会改变原对象的值，reversed()和 sorted()除外，
# 即使有返回值也一样会改变原对象
# 不可变对象执行方法操作是有返回值的，不会改变原对象的值
# for循环有next()调用和对StopIteration的处理
# for-else:else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样,而如果在for循环中含有break时则直接终止循环，并不会执行else子句
# iter()创建一个迭代器
for i, j in zip(a, b):
    if a is not b:
        print "No"
        break
else:
    print "Yes"
# hash()判断键是否有效
# 字典keys() values()得到字典的键、值，items()得到所有元组，fromkeys()得到默认字典，dict()创建字典
mydict = {'a': 1, 'b': 2}
b = ('c', 'd')
cdict = {}
d = cdict.fromkeys(b, "fromkeys")
yourdict = dict((('3', 1), ('4', 2)))
print "yourdict after dict():", yourdict
print "keys():", mydict.keys()
print "values():", mydict.values()
print "items():", mydict.items()
print "fromkeys:", d
# 遍历字典也不需要再用 keys()方法获取键值，直接用字典来作为迭代器就可以了
for x in mydict:
    print "字典作为迭代器：", x, mydict[x]
d = {key: value for (key, value) in mydict}
print "字典推导式：", d
# in或not in操作符“检查一个字典中是否有某个键”
# 用字典参数简化print语句
print "简化print：", 'a = %(a)s, b = %(b)s' % mydict
# del mydict['a']  # 删除键为'a'的条目
# mydict.clear()   # 删除 mydict 中所有的条目
# del mydict       # 删除整个字典
# mydict.pop('a')  # 删除并返回'a'的条目
# sorted()对字典直接得到有序的迭代子(key)
# 而 sort()则必选先获取 keys 再对key排序
print "sort():", mydict.keys().sort()
print "sorted():", sorted(mydict)
# update()将一个字典的内容添加到另一个字典中
print "update():", mydict.update({'c': 3})
print "mydict after update():", mydict
# get()若不存在则返回默认值，比[]灵活
print "get():", mydict.get('check', 'GetNothing')
# setdefault()检查键，如果不存在，给键赋值并添加到字典中
print "setdefault():", mydict.setdefault('check', 'added')
print "mydict after setdefault():", mydict
# 值相等的数字表示相同的键,1和1.0

# 集合的工厂方法 set()和 frozenset(),是无序的
myset = set('mohailang')    # 可变集合
print "可变集合 set:", myset
myfrozenset = frozenset('mohailang')  # 不可变集合
print "不可变集合 frozenset:", myfrozenset
# in/not in 检查元素是否属于集合
'm' in myset
# 更新可变集合成员,不能用+操作符
myset.update(set('love'))
print "myset after update():", myset
# 删除可变集合成员
# remove()只能一次删除一个元素
myset.remove('l')    # 等同于 -= set('l')
print "myset after remove():", myset
# 联合|
print "myset after |:", (myset | set('love'))
# 交集&
print "myset after &:", (myset & set('lang'))
# 差补/相对补集-,等价于 difference()
print "myset after -:", (myset - set('mo'))
print "myset after difference():", myset.difference(set('mo'))
# 对称差分^(异或),等价于symmetric_difference()
print "myset after ^:", (myset ^ set('hailang'))
print "myset after symmetric_difference():", myset.symmetric_difference(frozenset('hailang'))
# 结果集合的类型取决于左操作数的类型
# 可变集合操作符：
# (|=)等价于update()
# (&=)等价于intersection_update()
# (-=)等价于difference_update()
# (^=)等价于symmetric_difference_update()
# end
# 在循环中，break语句也会跳过 else语句
# 列表解析：[x**2 for x in range(10)]
# 生成器解析：(x**2 for x in range(10))
# 一个星（*）：表示接收的参数作为元组来处理
# 两个星（**）：表示接收的参数作为字典来处理


# 装饰器就是为已有的函数添加新的功能的修饰，省略了大量的重用代码:
def tsfuns(func):
    def wrappedFunc(*arg, **kw):
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func(*arg, **kw)  # 返回一个函数
    return wrappedFunc    # 返回一个装饰器


@tsfuns     # foo = tsfunc(foo)
def foo(var):
    print var


foo('我是装饰器')
sleep(4)
for i in range(2):
    sleep(1)
    foo('每隔一秒运行一次')

# 记住，函数也是一个对象，可以作为参数传入函数内
# 所有的必要参数都必须在默认参数之前
# 可变长参数元祖必须在位置和默认参数之后


def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachStrArg in theRest:
        print 'another arg:', eachStrArg


tupleVarArgs('abc', 123, 'mohailang', 520)

# 关键字变量参数应该为函数定义的最后一个参数


def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachStrArg in theRest.keys():
        print 'another arg %s: %s' % (eachStrArg, str(theRest[eachStrArg]))


dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))
# lambda 声明匿名函数
lambda x, y: x + y


# 这样理解 filter(): 返回的是一个 filter 对象，而不是一个序列
def myfilter(bool_func, seq):
    filtered_seq = []
    for eachItem in seq:
        if bool_func(eachItem):
            filtered_seq.append(eachItem)
    return filtered_seq


# 例子：
print "filter():", [n for n in [randint(1, 99) for i in range(9)] if n % 2]


# 这样理解map()
def mymap(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq


# 例子：
print "map():", ((lambda x: x + 2), [0, 1, 2, 3, 4, 5])
# map()和 filter()都可以被列表表达式取代
# 带有多个序列的 map():
print "map(seqs):", map(None, [1, 3, 5], [2, 4, 6])     # None可以是其他函数，而这样的 map()类似了zip()

# 这样理解 reduce():
# reduce(func, [1, 2, 3]) == func(func(1, 2), 3)


def myreduce(bin_fuc, seq, init=None):
    lseq = list(seq)  # convert to list
    if init is None:    # initialize?
        res = lseq.pop(0)   # no
    else:
        res = init      # yes
    for item in lseq:   # reduce sequence
        res = bin_fuc(res, item)  # apply function
    return res  # return result


# 使用functional模块中的partial()函数来创建PFA(偏函数)：
add1 = partial(add, 1)  # add1(x) == add(a,x)
mul100 = partial(mul, 100)  # mul100(x) == mul(100,x)
print "partial()创建PEA:add1()", add1(10)
print "partial()创建PEA:mul100()", mul100(10)

# 在mac下，Button的很多设置都无效,推荐使用ttk
# root = Tkinter.Tk()
# MyButton = partial(Tkinter.Button, root, fg='white', bg='blue')
# b1 = MyButton(text='Button1')
# b2 = MyButton(text='Button2')
# qb = MyButton(text='Quit', bg='red', command=root.quit)
# b1.pack()
# b2.pack()
# qb.pack(fill=Tkinter.X, expand=True)
# root.title('PFAS!')
# root.mainloop()

# 闭包概念：
# closure概念：在一个内部函数中，对外部作用域的变量进行引用，那么内部函数就被认为是closure（闭包）
# 自由变量：定义在外部函数内，被内部函数引用或者使用的变量为自由变量
# 先搜索局部变量再搜索全局变量，一层一层地向外搜索
# 可通过 func.func_closure 判断是否有闭包
output = '<int %r id=%#0x val=%d>'
w = x = y = z = 1


def f1():
    x = y = z = 2

    def f2():
        y = z = 3

        def f3():
            z = 4
            print output % ('w', id(w), w)
            print output % ('x', id(x), x)
            print output % ('y', id(y), y)
            print output % ('z', id(z), z)
        clo = f3.func_closure
        if clo:
            print "f3 closure vars:", [str(c) for c in clo]
        else:
            print 'no f3 closure vars'
        f3()

    clo = f2.func_closure
    if clo:
        print 'f2 closure vars:', [str(c) for c in clo]
    f2()


clo = f1.func_closure
if clo:
    print 'f1 closure vars:', [str(c) for c in clo]
else:
    print "no f1 closure vars"
f1()


# 装饰器、闭包：
def logged(when):
    def log(f, *args, **kargs):
        print '''Called:
function: %s
args: %r
kargs: %r''' % (f, args, kargs)

    def pre_logged(f):
        def wrapper(*args, **kargs):
            log(f, *args, **kargs)
            return f(*args, **kargs)
        return wrapper

    def post_logged(f):
        def wrapper(*args, **kargs):
            now = time()
            try:
                return f(*args, **kargs)
            finally:
                log(f, *args, **kargs)
                print "time delta: %s" % (time() - now)
        return wrapper
    try:
        return {"pre": pre_logged, "post": post_logged}[when]
    except KeyError as e:
        raise ValueError(e), 'must be "pre" or "post"'


@logged("post")
def hello(name):
    print "hello,", name


hello("mohailang")


# 生成器:
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# 通常和for循环配合使用(for循环有next()调用和对StopIteration的处理)
def odd():
    print 'yield 1'
    yield 1
    print 'yield 2'
    yield 2
    print 'yield 3'
    yield 3


for x in odd():
    print x


# 经典类(旧式类）：
class MyNewObjectType:
    'define MyNewObjectType classic class'
    pass
    # class_suite


# 新式类：必须继承一个父类
class ClassName(object):
    'define MyNewObjectType classic class'
    pass
    # class_suite


# 创建一个实例的过程称作实例化:没有使用 new
myFirstObject = MyNewObjectType()
myFirstObject.x = 1  # 实例属性，是动态的，不需要预先声明


# 在类里面所有声明方法都需要 self 参数：self 代表实例本身，而不是类本身
class MyMethod(object):  # 定义类

    def foo(self):  # 定义方法
        pass


# 一个特殊的方法 __init()__: 在创建对象的时候自动调用
class MyClass():
    'name and phone'

    def __init__(self, yourname, yourphone):  # 定义'构造器'
        self.name = yourname
        self.phone = yourphone
        print 'Created instance for: ', self.name
        print 'name: ', self.name
        print 'phone: ', self.phone

    def updatePhone(self, newphone):  # 定义方法
        self.phone = newphone
        print 'Updated phone for: ', self.name
        print 'new phone: ', self.phone


# 实例化调用，会自动调用__init()__：
worlder = MyClass('mohailang', '13112355359')
# 调用方法：
worlder.updatePhone('1198534595')


# 如果需要，每个子类最好定义它自己的构造器，不然，基类的构造器会被调用。
# 然而，如果子类重写基类的构造器，基类的构造器就不会被自动调用了——这样，基类的构造器就必须显式写出才会被执行，
# 像下面那样，用 MyClass.__init__()设置名字和电话号码。
class MyKidClass(MyClass):
    """docstring for MyKidClass"""

    def __init__(self, yourname, yourphone, yourid, youremail):
        # 注意，这里要显式传递self实例对象给基类构造器，因为不是在该实例中而是在一个子类实例中调用那个方法
        # 因为不是通过实例来调用它，所以c这种未绑定的方法调用需要传递一个适当的实例（self）给方法.
        MyClass.__init__(self, yourname, yourphone)
        self.id = yourid
        self.email = youremail
        print 'id: ', self.id
        print 'email: ', self.email

    def updateEmail(self, newemail):
        self.email = newemail
        print 'Updated email for: ', self.name
        print 'new email: ', self.email


hailang = MyKidClass('hailang', '13112355359', '2015052278', '1198534595@qq.com')
hailang.updateEmail('920399456@qq.com')

# 没有创建实例就不能调用类里面的方法
# dir()内建函数可以知道一个类有哪些属性：
print "通过dir()查看类的属性：", dir(MyKidClass)
# 或者是通过访问类或者类实例的字典属性：与vars(）内建函数等价
print '通过字典属性查看类的属性：', MyClass.__dict__
# __name__属性可以获得类型对象的相应字符串名,而不是类对象本身：
print '类的字符串名字：', MyClass.__name__
# __module__属性可以定位类的模块位置：
print '类所在的模块位置：', MyClass.__module__
# __class__属性可以定位实例所在的类位置：
print '实例化该实例的类的名字：', hailang.__class__
# __new__()方法才是类的真正的构造器，在创建实例前调用--创建返回实例，如果继承一个不可变对象(比如int)并想自定义实例化过程，那么就需要重写__new__()方法
# 实例可以有且仅有独立于其他实例火类的数据属性：
hailang.x = 'hailang的独有数据属性'
print 'hailang的独有数据属性: ', hailang.x
# 内建类型不存在__dict__属性
# 实例不能更新不可变类属性，只能访问，如果尝试更新类属性，就相当于给该实例创建了其独有的属性并覆盖了对该类属性的引用，所以只有类才能更新类属性
# 如果类属性可变，那么就可以这样更新，不过不建议这么做


# 静态方法不能访问类变量和实例变量，它跟类本身已经没什么关系了，它与类唯一的关联就是需要通过类名来调用这个方法
class MyPerson(object):

    @staticmethod
    def static_function():
        pass


# 类方法只能访问类变量，不能访问实例变量，通常用cls作为参数，代表类本身
class MyPeople():

    @classmethod
    def class_function(cls):
        pass


# 类的组合就是一个类中使用到了另一个类，从而把几个类拼在一起，就是在一个类中创建另一个类的实例：
class Date:

    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def birth_info(self):
        print("The birth is %s-%s-%s" % (self.year, self.mon, self.day))


class People:

    def __init__(self, name, age, year, mon, day):
        self.name = name
        self.age = age
        self.birth = Date(year, mon, day)  # 类的组合

    def walk(self):
        print("%s is walking" % self.name)


class Teacher(People):

    def __init__(self, name, age, year, mon, day, course):
        People.__init__(self, name, age, year, mon, day)
        self.course = course

    def teach(self):
        print("%s is teaching" % self.name)


class Student(People):

    def __init__(self, name, age, year, mon, day, group):
        People.__init__(self, name, age, year, mon, day)
        self.group = group

    def study(self):
        print("%s is studying" % self.name)


t1 = Teacher("mohailang", 28, 1989, 9, 28, "python")
s1 = Student("hailang", 22, 1996, 9, 28, "group2")
t1.birth.birth_info()
s1.birth.birth_info()


# 类的__bases__属性可以知道其父类
# 特殊属性__doc__不会被继承
# 通过继承覆盖父类方法，只需要重定义相同的方法名字即可，如果还想还想调用被覆盖的基类方法，那么就需要显式调用被覆盖的方法(参考前面子类的__init__())
# 但更好的方法是使用 super() 内建函数：
class P(object):

    def foo(self):
        print 'I am P-foo()'


class S(P):
    """docstring for C"""

    def foo(self):
        super(S, self).foo()
        print 'I am C-foo()'


s = S()
s.foo()

# 可以通过 mro()内建函数来获得某个类的MRO列表，它代表了类继承的顺序


class A(object):
    pass


class B(A):
    pass


class C(B):
    pass


print C.mro()


# 从标准类型派生：
# 1.不可变类型：
class RoundFloat(float):

    def __new__(cls, val):
        return float.__new__(cls, round(val, 2))


class RoundFloat1(float):

    def __new__(cls, val):
        return super(RoundFloat1, cls).__new__(cls, round(val, 2))


# 2.可变类型：
class SortedKeysDict(dict):

    def keys(self):
        return sorted(super(SortedKeysDict, self).keys())


# 类、实例和其他对象的内建函数：
# 1. issubclass(sub,sup)判断一个类是另一个类的子类或子孙类,第二个参数可以是父类组成的元组
# 2. isinstance(obj1,obj2)判定一个对象是否是另一个给定类的实例,第二个参数应当是类，也可以是类型对象，如isinstance(4,int)
# 3. hasattr()、getattr()、setattr()、delattr()
# super(type[, obj]): super()“返回此type的父类”。如果你希望父类被绑定，你可以传入obj参数（obj必须是type类型的）。否则父类不会被绑定


# 在类中定制自定义特殊方法：
class Time60(object):
    'Time60 - track hours and minutes'

    def __init__(self, hour, mins):
        self.hour = hour
        self.mins = mins

    def __str__(self):
        return '%d:%d' % (self.hour, self.mins)

    def __add__(self, other):
        return self.__class__(self.hour + other.hour, self.mins + other.mins)
    __repr__ = __str__

    def __iadd(self, other):
        self.hour += other.hour
        self.mins += other.mins
        return self     # 增量赋值必须返回self


mon = Time60(10, 30)
tue = Time60(11, 15)
myadd = Time60(1, 2)
print mon, tue
print mon + tue + myadd


# 如果在定义类的时候实现了__call__方法，类的实例就可以成为可调用的对象
class MyClass(object):

    def __call__(self, *args):
        print 'I am callable! Called with args:', args


me = MyClass()
me('mohailang')

# callable()判断一个对象是否可调用
# compile() 函数将一个字符串编译为字节代码，可以指定为 exec, eval, single
# exec()执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码
# eval() 函数用来执行一个字符串表达式，并返回表达式的值。
str = compile("print 'Hello, World'", '', 'exec')
exec('3+2')

####################################################
# 爬虫练习
####################################################
# 爬虫是请求网站并提取数据的自动化程序
# 爬虫基本流程：
# 1.发起请求：通过 HTTP 库向目标站点发起请求，即发送一个Request,请求可以包含额外的 headers 等信息，等待服务器响应
# 2.获取响应内容：如果服务器正常响应，会得到一个 Response,Response 的内容便是所要获取的页面内容，类型可能有 HTML,Json,二进制数据(如图片视频)等类型
# 3.解析内容：得到的内容可能是 HTML，可以用正则表达式、网页解析库进行解析。可能是 Json，可以直接换为 Json 对象解析。可能是二进制数据，可以做保存或者进一步的处理
# 4.保存数据：保存形式多样，可以存为文本，也可以保存至数据库，或者保存特定格式的文件
#
# Request和 Response:
# (1)浏览器就发送信息给该网址所在的服务器，这个过程叫做 HTTP Request
# (2)服务器收到浏览器发送的信息后，能够根据浏览器发送的内容做相应的处理，然后把消息回传给浏览器，这个过程叫做 HTTP Response
# (3)浏览器收到服务器的 Response 信息后，会对消息进行相应处理，然后展示
#
# Resquest 包含什么：
# 1.请求方式：主要有 get、post两种类型，另外还有 HEAD、PUT、DELETE、OPTIONS 等
# 2.请求 URL：URL 全称统一资源定位符，如一个网页文档、一张图片、一个视频等都可以用 URL 来唯一确定
# 3.请求头：包含请求时的头部信息，如 User-Agent、Host、Cookie 等信息
# 4.请求体：请求时格外携带的数据如表单提交时的表单数据
#
# Response 包含什么：
# 1.响应状态：有多种响应状态，如200代表成功，301跳转，404找不到页面，502服务器错误
# 2.响应头：如内容类型。内容长度、服务器信息、设置 Cookie 等等
# 3.响应体：最主要的部分，包含了请求资源的内容，如网页 HTML、图片、二进制数据等
#
# 解析方式：直接处理、Json解析、正则表达式、BeautifulSoup解析库、PyQuery解析库、XPath解析库
#
# 怎么解决JavaScript 渲染的问题：
# 分析Ajax 请求、Selenium/WebDriver、Splash、PyV8、Ghost.py
#
# 怎样保存数据：
# 1.文本：纯文本、Json、XML 等
# 2.非关系型数据库：如 MongoDB、Redis等Key-Values 形式存储
# 3.关系型数据库：如 MySQL、Oracle、SQL Server 等具有结构化表结构形式存储
# 4.二进制文件：如图片、视频、音频等等直接保存成特定格式即可
#
# 什么是 Urllib:
# Python 内置的 HTTP 请求库
# urllib. Request 请求模块
# urllib. Error 异常处理模块
# urllib. Parse url 解析模块
# urlib. Robotparser robots. Txt 解析模块


####################################################
# 高级主题
####################################################
