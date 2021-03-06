# 软件学院《程序设计实践》2020小学期

[助教姓名与github昵称对应表](./助教昵称对应表.md)，包含了昵称对照、辨别助教的方法。

## 通知（持续更新）
如果选题改变，请联系你所在小组的助教

交互式网站类作品，在本地能够运行就行了，不需要部署到云端

交互式网站类作品，前后端分离 vs 前后端不分离，前后端分离（当然前端要使用框架例如vue）会获得分数的优势。（但是请没有经验的同学谨慎权衡技术风险）

对于 飞机大战、坦克大战、贪吃蛇、俄罗斯方块、2048 等游戏，因为网上找得到源码，所以一定要增加新的功能和玩法！！！

在任何的开发阶段，同学们都可以录制一个视频上传bilibili，然后到github来提issue，让助教和老师帮你参考一下是否符合要求、功能复杂度够不够。

不是说你按照自己登记的选题开发，就安全了。最终的分数还是取决于你的作品水平。

使用的技术或者是做出来的作品和填写的问卷有差别是允许的。

## 开发指引

### 小游戏开发

注：不推荐使用控制台去写过于丰富的图形界面的呈现，会不方便。同时，这类问题也难以解决： #24

[pygame指引](./starter-pygame.md)

关于pymunk：貌似有不少同学都在利用pygame做游戏的时候希望使用pymunk建立物理模型，如果有较好的解决「pymunk和pygame结合」或者是「鼠标键盘控制pymunk」两个技术问题的欢迎通过issue与大家分享

[unity&unreal指引 （待补充）](./starter-unity&unreal.md)

TODO...等待有经验的助教补充


### 网站开发
- 无基础的同学，建议使用前后端不分离的模式。
- 有基础的同学，可以考虑前后端分离的模式，前端考虑vue。

初学者框架推荐：
- python django [django指引（待补充）](./starter-django.md)
- python flask

初学者不推荐：
- java spring
- c# Asp.NetCore

理由：过于工程化，不适合初学者


### 小程序开发
小程序开发入门教程：

[小程序开发](https://bhpan.buaa.edu.cn:443/link/B72DDE846AD0914DA7073B8B0B549AEB)

来自软件学院科技实践部的王学长，欢迎各位19级萌新加入科技实践部！


### 桌面程序开发

c# winform：winform是最简单、最傻瓜式的。只需要拖控件、写代码，就可以完成想要的功能。 [Winform指引](./starter-winform.md)

c/c++使用windows api开发：效率极端低下，不推荐。助教也对这种开发模式不熟，难以回答 #23 #25 #29 这类的问题

qt：有基础的可以尝试。 [QT指引 (待补充)](./starter-QT.md)

java swing：swing的开发没有winform傻瓜式，建议有基础的同学尝试。

c# wpf：建议有winform基础的同学尝试。wpf是MVVM的始祖。
