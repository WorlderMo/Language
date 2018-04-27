a = 520
print "表面积 = ", a ,"\n"
print "表面积 = #{999}\n"
puts "表面积 = #{a}"#会自动输出换行符
=begin
这是注释
=end

print "注释结束\n"
p "\n"
p (9 == 9)
if a > 20 then
	print("bigger\n")
else
	print("smaller")
end
i = 2
while i < 3
	print("bigger\n")
	i = i+1
end
while i <= 10
	print i, "\n"
	i = i+1
end
2.times do
	print("打印两次\n")
end
names = ["莫m", "海h", "浪L"]
print(names[1], "\n")
names.each do |n|
	puts n
end
sym = :foo
print sym.to_s, "\n"
address = {:name => "莫海浪", pinyin:"mohailang"}
print address[:name], "\n"
address.each do |key, value|
	puts("#{key}:#{value}")
end
puts "匹配的位置为：#{/ruby/ =~ "rubyhello"}"
puts "不分大小写匹配的位置为：#{/ruby/i =~ "RUBYhello"}"#正则表达式右边的 / 后面加上 i 表示不区分大小写匹配。
names.each do |name|
	if /莫/ =~ name
		puts name
	end
end
def hello
	print "hello, 我在调用方法\n"
end
hello()
#多重赋值
a, b, c, d = 520, 1314
p [a, b, c]
a, b, c = 666, 888, 999, 000
p [a, b, c]
a, *b, c = 111, 222, 333, 444, 555
p [a, b, c]
#置换变量的值
a, b = "mo", "lang"
a, b = b, a
p [a, b]
#获取数组的元素
ary = [1314, 520]
a, b = ary
p a, b
ary = [222, 444]
a, = ary
p a   #尽量少用
#获取嵌套数组的元素
ary = [1, [2, 3], 4]
a, b, c = ary
p a, b, c
a, (b1, b2), c = ary# 对与数组结构相对应的变量赋值
p a, b1, b2, c
#条件判断
p "".empty?
p "I LOVE YOU".empty?
a = 10
b = 20
if a > b then
	puts "a > b"
elsif a < b then
	puts "a < b"
else
	puts "a = b"
end
unless a > b then
	puts "a <= b"
end
tags = [ "I", "LOVE", "YOU"]
tags.each do |tagname|
	case tagname
	when "SOFT", "I", "Ware", "BLOCKQUICT"
			puts "#{tagname}, has child."
	when "LOVE", "2015"
		puts "#{tagname} has no child."
	else
		puts "#{tagname} cannot be used."
	end
end
array = ["I", 520, nil]
array.each do |item|
	case item
	when String
		puts "item is a String."
	when Numeric
		puts "item is a Numeric."
	else
		puts "item is something"
	end
end
puts "if 与 unless 可以写在希望执行的代码的后面" if a < b
#对象的同一性
ary1 = []
ary2 = []
p ary1.object_id
p ary2.object_id
#循环
#times方法
3.times do
	puts "I LOVE 莫海浪"
end
3.times do |i|
	puts "第 #{i+1} 次 LOVE 浪哥"
end
#for循环
for i in 4..6 do
	puts "第 #{i} 次 LOVE 浪哥"
end
for tag in tags do
	puts tag
end
#while语句
i = 1
while i <= 3
	puts "浪哥好丑"
	i+=1
end
#until语句
i = 1
until i > 3 do
	puts "浪哥好帅啊"
	i+=1
end
#each方法
tags.each do |tag|
	puts tag
end
(1..3).each do |num|
	puts "死了都要LOVE"
end
#方法调用
p Time.now.to_s
Array.new   #创建新的数组
#方法的定义
def hello(name)
	puts "你说你是街角的野蔷薇"
	puts "而 #{name} 却傻傻只当你是朵玫瑰"
end
hello("mhl")
def hello(name="mhl")
	puts "就算你被全世界的坏人包围"
	puts "看 #{name} 化身超人 一一把他们击退"
end
hello()
hello("mohailang")
#定义带块的方法
def myloop
	yield #执行块，实际上是方法里面的内容
end
num = "吹啊吹啊我的骄傲放纵"
myloop do
	puts num   #yield的内容
end
#参数个数不确定的方法
def foo(*args)
	args
end
puts foo("吹啊吹啊", "不毁我纯净花园")
#至少需要指定一个参数的方法
def mhl(arg, *args)
	[arg, args]
end
puts mhl("怎么风越狠")
puts mhl("我心越荡", "看不见你的笑我怎么睡得着")
#关键字参数
def love(x:0, y:0, z:0)
	x  + " " + y + " " + z
end
puts love(z:"YOU", y:"LOVE", x:"I")
#使用“** 变量名”的形式来 接收未定义的参数
def love(x:0, y:0, z:0, **arg)
	[x, y, z, arg]
end
p love(z:"YOU", y:"LOVE", x:"I", w:",too")
#new 新的对象
ary = Array.new
ary = [520, 1314]
p ary
#用 class 测试对象的类
ary = [520]
str = "I Love YOU"
p ary.class
p str.class
#用instance_of？判断对象是否属于某个类
p ary.instance_of?(Array)
p str.instance_of?(String)
p ary.instance_of?(String)
p str.instance_of?(Array)
#根据类的继承关系反向追查对象是否属于某个类时，则可以使用is_a方法
p ary.is_a?(Array)
p str.is_a?(Object)
#创建类 and 存取器
class ILoveYou
	def initialize(myname = "lover")
		@love = myname		#参数 myname 传给实例变量@name
	end
#注：实例变量的名称要和存取器的名称一致，不会出现莫名的错误
	attr_accessor:love		#存取器
=begin	def love
			@love		#直接获取 @name
		end

		def love=(value)
			@love = value		#修改 @name
		end
=end
	def YouLoveMe
		puts "Hello, my dear #{@love}"
	end
end
MHL = ILoveYou.new#("ruby")
mohailang = ILoveYou.new("python")
MHL.YouLoveMe
mohailang.YouLoveMe
p MHL.love
mohailang.love = "Java"
p mohailang.love
#在 class << 类名 ~ end 这个特殊的类定义中，以定义实例方法的形式来定义类方法
class SheLoveMe
	def my_love(myname)
		p "#{myname} said Love me firstly"		#该类中可以没有方法
	end
end
mohailang = SheLoveMe.new	#普通类必须先 new 一个对象才能使用类里面的方法
mohailang.my_love("mohailang")
class << SheLoveMe		#使用该定义的时候，前面必须已经定义了一个相同的类，不然会出现该类还没初始化的错误
	def she_love(hername)
		p "#{hername} said She Love Me"
	end
end
SheLoveMe.she_love("nine hundred millons girls")	#在引用的对象是该类本身时，无需 new 对象就可以使用类方法
#在 class 上下文中使用 self 时，引用的对象是该类本身，因此，我们可以使用 class << self ~ end 这样的形式，在 class 上下文中定义类方法。
class ILoveShe
	class << self
		def love(lovername)
			p "#{lovername} said I Love You"
		end

	end
end
ILoveShe.love("mohailang")		#调用类本身
#还可以使用 def 类名 . 方法名 ~ end 这样的形式来定义类方法
def SheLoveMe.loves(name)
	p "#{name} said All of us love you so much"
end
SheLoveMe.loves("nine hundred millons girls")	#使用该定义的时候，前面必须已经定义了一个相同的类，不然会出现该类还没初始化的错误
#another style
class AllLoveMe
	def self.love(name)
		print name, " said I would marry mohailang\n"
	end
end
AllLoveMe.love("Nine hundred millons girls")	#该类方法不需预先定义一个普通类
# 常量(必须以大写字母开头)
class Constant
	Vindication = "Everybody Love mohailang"
end
p Constant::Vindication
#类变量 @@
class ClassName
	@@count = "I am a class constant"		#类变量
	def ClassName.count		#类方法
		@@count
	end
end
puts ClassName.count
#限制方法的使用
class ACC_Test
	def one
		p "I am a public methon"
	end
	public :one		#可以省略,把 one 方法设为 public
	def two
		p "I am a private methon"
	end
	private :two		#把 two 方法设定为 private
	def three
		p "I am a protected methon"
	end
end
oner = ACC_Test.new
oner.one
#oner.two	如果编译这行就会出现错误，因为私有类不能指定对象，但可以被定义它的类和子类访问
oner.three	#protected可以被定义它的类和子类访问
#统一定义多个方法的访问级别
class ACCTest
	public		#不指定参数时，以下方法都为 public
	def one
		p "I am a public methon"
	end
	private		#不指定参数时，以下方法都为 private
	def two
		p "I am a private methon"
	end
	protected		#不指定参数时，以下方法都为 protected
	def three
		p "I am a protected methon"
	end
end
#扩展类
class String
	def count_word
		ary = self.split(/\s+/) # 用空格分割接收者
		return ary.size # 返回分割后的数组的元素总数
	end
end
str = "nobody nobody but you"
p str.count_word
#继承
class RingArray < Array # 指定父类
	def [](i)		# 重定义运算符[]
		idx = i % size 	# 计算新索引值
		super(idx)		# 调用父类中同名的方法
	end
end
wday = RingArray["死", "了", "都", "要", "爱", "啊"]
print wday[0], wday[1], wday[2], wday[3], wday[4], wday[5], "\n"
#alias  设置别名
class C1
	def hello
		"I love you"
	end
end
class C2 < C1		#定义 C1 的子类 C2
	alias old_hello hello		#设置别名为 old_hello
	def hello		#重定义方法 hello
		"#{old_hello}, too"
	end
end
love = C2.new
p love.old_hello
p love.hello
#undef
#模块    通过 include 可以把模块内的方法名、常量名合并到当前的命名空间
p Math::PI
include Math
p PI
#创建模块
module HelloModule
	Version = "You are my world"
	def hellolove(name)
		p "I love you, #{name}"
	end
	module_function:hellolove		#指定 hello 为模块函数
end
p HelloModule::Version
HelloModule.hellolove("Big Data")
include HelloModule		#include模块的时候，前面不能有相同的方法名称，不然会混乱,表示以下的内容都包含着 HelloModule模块
p Version
hellolove("Alice")
#Mix-in，类包含模块后就可以直接使用模块里面的方法
module ModuleName
	def meth
		p "You also love me, right?"
	end
end
class ClassName
	include ModuleName		#包含 ModuleName 模块
end
Cname = ClassName.new
Cname.meth
# ancestors 方法和 superclass 方法调查类的继承关系
p ClassName.ancestors
p ClassName.superclass
#extend方法
module Edition
	def edition(name)
		"#{self}, #{name}"
	end
end
str = "I miss you"
str.extend(Edition)		#把模块 Mix-in进对象
puts str.edition("mohailang")
#类与 Mix-in and 使用extend 方法追加类方法 and include方法追加实例方法
module ClassMethons		#定义类方法的模块
	def cmethon
