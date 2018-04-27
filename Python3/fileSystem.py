#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class item:

    def __init__(self):
        self.father = 1  # 记录父节点的下标
        self.name = ''  # 名称
        self.isfolder = True  # 判断是否是文件夹
        self.son = []  # 列表


docu = []
docu.append(item())  # 定义结构对象
cur_folder = 0
num = 0


def IsSameName(name):
    for i in docu[cur_folder].son:
        if docu[i].name == name:
            return False
    return True


def output():
    print()
    print("        目录信息")
    print("****************************")
    if docu[cur_folder].father != cur_folder:
        print("上级目录名称：", docu[docu[cur_folder].father].name)
    print("当前目录名称: ", docu[cur_folder].name, "\n")
    print("目录下文件:", "\n")
    print("序号\t| 文件名\t| 属性")
    if len(docu[cur_folder].son) == 0:
        print("空")
    else:
        j = 0
        for i in docu[cur_folder].son:
            j += 1
            print(j, "\t| ", docu[i].name, "\t| ", end="")
            if docu[i].isfolder:
                print("文件夹")
            else:
                print("文件")
    print("****************************", "\n")


def init():
    docu[0].father = 0
    docu[0].name = "根目录"
    docu[0].isfolder = True


def new_file():
    print("请输入文件名：")
    new_name = input()
    global num
    num += 1
    docu.append(item())
    print()
    if IsSameName(new_name):
        print("文件创建成功！ 不存在同名文件文件夹!")
    else:
        print("存在同名文件文件夹!  文件创建失败!")
        return
    global cur_folder
    docu[num].father = cur_folder
    docu[cur_folder].son.append(num)
    docu[num].name = new_name
    docu[num].isfolder = False


def new_folder():
    print("请输入文件夹名：")
    new_name = input()
    global num
    num += 1
    docu.append(item())
    print()
    if IsSameName(new_name):
        print("文件夹创建成功！ 不存在同名文件文件夹!")
    else:
        print("存在同名文件文件夹!  文件夹创建失败!")
        return
    global cur_folder
    docu[num].father = cur_folder
    docu[cur_folder].son.append(num)
    docu[num].name = new_name
    docu[num].isfolder = True


def delete_docu():
    xu = int(input("请输入要删除的序号："))
    if xu < 1 or xu > len(docu[cur_folder].son):
        print("输入的序号不合法！")
        return
    docu[cur_folder].son.pop(xu - 1)


def rename():
    xu = int(input("请输入您要修改的序号："))
    if xu < 1 or xu > len(docu[cur_folder].son):
        print("输入的序号不合法！")
        return
    new_name = input("请输入新的文件文件夹名：")
    if IsSameName(new_name):
        print("修改成功！ 不存在同名文件文件夹!")
    else:
        print("存在同名文件文件夹!  修改失败!")
        return
    docu[docu[cur_folder].son[xu - 1]].name = new_name


def enter_son():
    global cur_folder
    xu = int(input("请输入要进入的子目录的序号："))
    if xu < 1 or xu > len(docu[cur_folder].son):
        print("输入的序号不合法！")
        return
    if not docu[docu[cur_folder].son[xu - 1]].isfolder:
        print("您选中的不是文件夹！")
        return

    cur_folder = docu[cur_folder].son[xu - 1]
    print("成功进入新的文件夹!")


def return_father():
    global cur_folder
    if docu[cur_folder].father == cur_folder:
        print("已经在根目录了")
    cur_folder = docu[cur_folder].father


def meun():
    print("      请选择您的操作")
    print("****************************")
    print("1、新建文件           2、新建文件夹", "\n")
    print("3、删除文件或文件夹   4、修改文件或文件夹名", "\n")
    print("5、进入下级目录       6、返回上级目录 ", "\n")
    print("7、退出文件系统", "\n")
    print("****************************")
    try:
        inp = int(input(""))
        if inp == 1:
            new_file()
        elif inp == 2:
            new_folder()
        elif inp == 3:
            delete_docu()
        elif inp == 4:
            rename()
        elif inp == 5:
            enter_son()
        elif inp == 6:
            return_father()
        elif inp == 7:
            return
        else:
            print("输入有误")
    except Exception as result:
        print("输入有误! 错误类型： %s" % result)
    output()
    meun()


init()
output()
meun()
print("退出了文件系统")
