# -*- coding: utf-8 -*-
from sys import argv    #引入模块

script, input_file = argv   #定义 argv

def print_all(f):      #定义函数 「打印全部」
    print f.read()     #读文件

def rewind(f):        #定义函数
    f.seek(0)        # seek 用于读取文件指定位置数据

def print_a_line(line_count, f): #定义函数「打印行」
    print line_count, f.readline()

current_file = open(input_file)  #当前文件

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)    #print row 1

current_line = current_line + 1
print_a_line(current_line, current_file)    #print row 2

current_line = current_line + 1
print_a_line(current_line, current_file)    #print row 3

# 'a+=b'相当‘a=a+b’
