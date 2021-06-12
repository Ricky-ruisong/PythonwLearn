"""最近项目用到python，稍微记录一下关于import的学习"""
""" 路径 """
from . import module_name。导入和自己同目录下的模块。
from .package_name import module_name。导入和自己同目录的包的模块。
from .. import module_name。导入上级目录的模块。
from ..package_name import module_name。导入位于上级目录下的包的模块。
每多一个点就多往上一层目录。

eg:
Tree(Dirctory)
| -t1.py
| |-t2.py
| |-t3.py
此时，如果t2.py中import了t3.py,且t1.py中importt2.py。那么t3中的import应该为：
from . import t3
绝对导入用于导入sys.path中的包和运行文件所在目录下的包。对于sys.path中的包，；导入自己写的文件，如果是非运行入口文件（上面的t1.py是运行入口文件，可以使用绝对导入,t3就是非运行入口文件），则需要相对导入。

""" 更名 """
有些module_name比较长，之后写它时较为麻烦，或者module_name会出现名字冲突，可以用as来给它改名, eg:import numpy as np  

""" 导入部分 """
假如 car.py 里定义了类 Car : from car import Car
假如  car.py 包含了三个类 Car ， Battery 和 ElectricCar 复制代码导入多个类，中间用逗号隔开：from car import Car,Battery,ElectricCar

""" 文件相关 """
读取整个文件
with open('test.txt') as file_obj:
    contents = file_obj.read()
    print(contents)
逐行读取
with open('test.txt') as file_obj:
    for line in file_obj:
        print(line.rstrip())

写入文件
with open('test.txt', 'w') as file_obj:
    file_obj.write("I love python")
可选模式：
r  ：只读。
w  : 只写。如果文件不存在则创建，如果文件存在则先清空，再写入。
a  ：附加模式，写入的内容追加到原始文件后面。如果文件不存在则创建。
r+ ：可读可写。

""" 异常 """
try:
    print(3/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
	print("no exception")

""" 用 json 存储数据 """
import json

userInfo = {'username': 'ricky', 'age': 8}

with open('test.txt', 'w') as obj:
    json.dump(userInfo, obj)

with open('test.txt') as obj:
    content = json.load(obj)
    print(content)

