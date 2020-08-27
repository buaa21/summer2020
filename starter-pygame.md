# pygame指引

TODO: 

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
