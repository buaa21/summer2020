# pygame指引

TODO:

【写在前面】关于pygame，pymunk以及包括其他语言在内的组件，解决问题的最好方法其实是去翻官方文档，一般都包含了所有方法的详细说明以及实例
pymunk:http://www.pymunk.org/en/latest/pymunk.html#pymunk-package
pygame:https://www.pygame.org/docs/
pyglet:https://pyglet.readthedocs.io/en/latest/

首先安装python，安装好后终端输入 python 会显示当前python版本。

pip --version  查看安装的pip版本。

如果没有安装pip，下载并安装https://pypi.org/project/pip/#downloads

然后根据python版本安装对应的pygame

安装部分的官方指导（非常详细）：https://www.pygame.org/wiki/GettingStarted#Pygame%20Installation

这部分不一定靠谱：（安装可以直接去下载安装包 http://www.pygame.org/download.shtml ，或者根据自身情况终端安装：
python -m pip install --user pygame）

pygame官方文档（包含安装方法以及常用函数，函数包括绘制，色彩，时间控制，键盘、鼠标监听等）
https://www.pygame.org/docs/

一个游戏循环（也就是程序的主循环）分为三步：处理事件，更新游戏状态，屏幕绘制

一个Hollo world程序示例

          # -*- coding: UTF-8 -*-

          import pygame, sys 
          # 声明 导入pygame和sys模块，这样我们的程序才可以使用里面的方法

          from pygame.locals import *
          # 也是声明导入，只是形式不同，导入所有 pygame.locals里的变量（比如下面大写的QUIT变量）


          pygame.init()# 初始化pygame

          DISPLAYSURF = pygame.display.set_mode((400, 300))# 设置窗口的大小单位为像素

          pygame.display.set_caption('Hello World!')# 设置窗口的标题

          while True: # 程序主循环

              for event in pygame.event.get():# 获取事件

                  if event.type == QUIT:# 判断事件是否为退出事件

                      pygame.quit()# 退出pygame

                      sys.exit()# 退出系统

              pygame.display.update()# 绘制屏幕内容


最后，如果想尝试又不知道如何开始可以多跟助教沟通。
