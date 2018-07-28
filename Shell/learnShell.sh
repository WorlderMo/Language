# 执行脚本
# chmod +x ./learnShell.sh # 使脚本具有执行权限
# ./learnShell.sh #执行脚本, ./告诉系统就在当前目录找

# 指定系统用哪种 Shell来执行Shell脚本
#!/bin/bash

# shell 变量
# shell变量名和等号之间不能有空格
a="hello shell"
# 引用变量要加$
echo $a
# 推荐给所有变量都加上花括号，防止变量名和字符混合
echo "I say ${a} and hello world"
# 只读变量，其值不能被改变
# readonly a
# 删除变量
unset a


# shell 字符串
# 单引号里面的变量是无效的，也不能出现转义字符，但双引号里面可以使用
# 通过${#}获取字符串长度
string="mohailang"
len=${#string}
echo $string
