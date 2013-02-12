Title: 数字图像处理实验
Author: freealbert
Date: 2012-8-13
Tags: dip, pyee, python, matlab

<div id="part0"></div>
* [写在最前面的废话](#part1)
* [如何开始之Python篇](#part2)
    + [Python简介](#part2.1)
    + [模块介绍](#part2.2)
    + [了解更多](#part2.3)
    + [代码示例与骨架](#part2.4)
* [如何开始之Matlab篇](#part3)
* [EXP1 基本灰度变换](../ji-ben-hui-du-bian-huan.html) 
* [EXP2 直方图处理技术](../zhi-fang-tu-chu-li.html) 
* [EXP3 图像平滑技术](../ping-hua-ji-zhu.html) 
* [EXP4 图像锐化技术](../tu-xiang-rui-hua.html)       

      
## <div id="part1">写在最前面的废话</div>

> 既然课程名字叫作***数字图像处理***，而不是XXX程序语言设计，那么学生便有选择任何一种自己喜欢的语言完成实验的自由。

本文最早的写作时间起于我刚学Python的时候，对着实验指导书码着同样是刚开始学习的matlab语言代码的，想着如果这个实验也可以用Python完成就好了。恰逢《Python科学计算》刚刚出版，我买了一本学习了一下（我是亚马逊上第二个购买的～），试着用Python完成了实验，心里也萌生了我也可以写一下Python版的实验指导书的念头。

在这个想法的牵引下，我修改了一下原先老师下发的实验指导书，从最初的Word版，用刚学会的Latex排成了PDF，顺便增加了一些我自己理解的实验原理。然后又尝试了下Beamer还有HTML5制作幻灯片，得出结论虽然PDF不是最佳形式，但幻灯片更加不是。最后我想我找到了，网页由于其天生的超链接特性，可以方便的在不同资源之间自由跳转，以前那种一言难尽的感觉终于没了。还有[MathJax](http://www.mathjax.org/)这种优秀的开源项目，让呈现数学公式也变得容易。

过程中，我也收到了一些善意的建议，觉得这么做是徒劳的。我很清楚，不像同样开源的R之于统计领域，在通信这块，Matlab相比Python的优势实在巨大。开源不是万能的，科学计算方面，Python不论是文档还是社区都是远远不及，就性能而言，同样是其短板。其实更大的阻力来自于我自己的内心，我深知自己的水平，不管是这门课还是Python，连入门的门槛还没摸着，自娱自乐没事，误人子弟就罪孽深重了。也由此，这篇文章写写停停花了半年左右，现在我才发现，驱使我还在写的倒不是目的本身，而是这个过程。从一开始的LaTeX，到先前学着用Pelican，Github，带着我走进一个HTML+Javascript+CSS构成的Web世界，真的挺有趣的。

你现在正在访问的网站是由Python写成的，国内外很多著名网站比如[豆瓣](http://www.douban.com/)，[知乎](http://www.zhihu.com/)，[DropBox](http://dropbox.com/)都是由Python写的。
当然本文并不是要讨论其在Web端的应用以及如何建一个网站，而是在另一个领域——科学计算，更精确点也就是如何用Python完成我们的数字图像处理实验。考虑到大部分人可能对新语言不感冒，我也安排了Matlab的部分。

本文一共六个部分，除了你现在在阅读的废话环节，还有对于初学者如何用Python或Matlab来完成本实验，以及四个完整的实验，包括了实验原理，内容步骤等。其中我会用Python给出代码骨架。由于我行文实在罗嗦，因此我强烈建议你当感觉不耐烦时，按下[Home](#part0)键，返回页首，然后根据目录直奔目标。

## <div id="part2">如何开始之Python篇</div>

### <div id="part2.1">Python简介</div>

Python不同于我们之前学过的C/C++，她是一种解释性语言，这一点，本文的另一种备选语言Matlab也是相同的。没有编译这个环节，在程序写好后，便可以运行，当程序运行到有错误的时候便会停下来。一般来说，解释性语言的速度慢于编译型语言，但在现在我们的电脑上，这一点可以完全忽略了。

Matlab除了Matlab语言本身还有许许多多的工具箱（你很可能已经在数字信号处理的课堂上见识过信号处理工具箱），工具箱其实就是一堆函数。这些工具箱就是一个个扩展的模块，用来满足某些领域的需求。比如

+ 信号处理工具箱提供了丰富的信号处理方面的函数
+ 符号数学工具箱扩展了原先只能做数值运算的Matlab使其也能够做符号运算
+ 图像处理工具箱当然是用来做图像处理的，针对的就是本实验。
+ 更多的工具箱，传送门在[这里](http://www.mathworks.cn/products/)

同Matlba一样，Python也有许多的扩展类库，也可以称之为模块。我觉得，模块之于Python就像守护在雅典娜身边的圣斗士，团聚在其周围，扩充了其的应用领域和威力。下面这张图很好的表现了这一点：

![Athena](https://github.com/freealbert/PyEE/blob/master/Python/pyintro/python_1.png?raw=true)

### <div id="part2.2">模块介绍</div>
上图中的模块构成了一个较为完整的科学计算的生态系统，当然对于本实验我们用不了这么多，只要稍微了解下下面的青铜五小强即可。

* [Scipy](http://www.scipy.org/)
Scipy是一个用于数学，科学和工程领域仿真的类库，提供了大量现成的函数。本实验中我们会使用其中的signal模块,约定模块导入的形式如下：

```.python
	import scipy.signal as signal
```

* [Numpy](http://numpy.scipy.org/)
Numpy模块是Scipy的基础，提供了对矩阵和多维数组的支持以及许多数值计算的函数。约定其导入形式如下:
```.python
	import numpy as np
```

* [matplotlib](http://matplotlib.sourceforge.net/)
matplotlib是一个二维图像绘制为主的类库，我们会用到其中的pylab模块和cm模块。
	+ pylab模块集成了一些常用的绘图函数，应付我们这次实验绰绰有余。
	+ cm是colormap的缩写，指明的是表示颜色的数值和具体颜色之间以何种方式映射。拍照时的一些效果，如老照片（红铜色）就是由这个决定的。

	我们约定模块导入形式如下：

```.python
	import matplotlib.cm as cm
	import matplotlib.pylab as pl
```
有必要提醒一下，matplotlib的那些container的层次还是搞清一下最好，有点恼人的。

* [PIL](http://www.pythonware.com/products/pil/)
PIL是Python Image Library的缩写，顾名思义，是用来做图像处理的类库。
我们约定模块导入形式如下：
```.python
	import PIL.Image as Image
```

* [PyOpenCV](http://code.google.com/p/pyopencv/)
OpenCV是一个基于C/C++语言的开源图像处理函数库，而PyOpenCV是其Python语言的绑定，由此，我们便可以抛开一想就头大的C++,使用Python直接调用其中的函数了。OpenCV功能十分强大，完成本实验小菜一叠，<strike>虽然并不一定要用到它，写在这儿，权做推荐了解一下。</strike>
**怀着激动的心情还更新下～～～ PyOpenCV好久没有更新了，建议安装OpenCV最新的Python扩展库cv2，《Python科学计算》的[作者](http://hyry.dip.jp/)将书中所有的PyOpenCV都用cv2重写了，[这里](http://blog.chinaunix.net/uid-23100982-id-3082055.html)有说明和实例。**
 

### <div id="part2.3">了解更多</div>
由于篇幅有限，本文不可能对Python的语法来个详细的介绍，如果想用Python完成本实验，那么你只好去看别的教程了，幸好我们的要求并不高，一会会就可以将所能用到的语法一网打尽了，这么简单，你也可以边写程序边学习。

Python有着一个庞大的社区，网络上的好资源也是汗牛充栋。你大致了解下Python的简单语法，和一点点用Python做科学计算的知识就可以开始啦。下面是一些资源索引:
#### 推荐
+ [简明 Python 教程](http://woodpecker.org.cn/abyteofpython_cn/chinese/index.html) 推荐，可直接浏览，一天之内应该就可以写程序了。
+ [用Python做科学计算](http://hyry.dip.jp:8000/pydoc/index.html) 强烈推荐，这本书详细的介绍了我们会用到的类库（Numpy、Scipy、 matplotlib），目前也是唯一一本关于Python做科学计算的书。可以在图书馆借到，作者在网上放了大部分的内容，对我们实验而言已经足够了。
+ [HYRY Studio](http://hyry.dip.jp/) 《Python科学计算》作者的网站，汇集了博客、论坛等功能，里面的技术文章自然是很有价值，无需多言。让我印象更为深刻的是，里面记载的作者平时生活工作的点滴，让我感到就像身边稍微年长一点的前辈或是关系稍好的年轻老师，还是个好爸爸，觉得可亲，再看他的书，仿佛也更容易理解了。还有他女儿的日记呢，かわいい！
#### 可参考 
+ [NumPy for Matlab Users](http://www.scipy.org/NumPy_for_Matlab_Users/) Matlab与Numpy/Scipy有很多相似之处，也有很多不同。这篇文章比较了两者的差异，有兴趣者可以看看。
+ [matplotlib gallery](http://matplotlib.sourceforge.net/gallery.html) 有很多绘图的案例，也有相应的代码，我觉得是matplotlib绘图的最好教程了。
+ [Python Imaging Library Handbook](http://www.pythonware.com/library/pil/handbook/index.htm) PIL的官方手册，其中的Image模块我们会经常用到，虽然是英文，但也比较好懂，有兴趣可以看看。
+ [Numpy Reference Guide](http://docs.scipy.org/doc/numpy/reference/) Numpy的手册，非常详尽，不推荐阅读，因为太详尽会把你吓跑的。
+ [Scipy Reference Guide](http://docs.scipy.org/doc/scipy/reference/) Scipy手册，不推荐阅读，理由同上。

### <div id="part2.4">代码示例</div>
万事开头难，先选取实验一中的步骤2作为例子。
```.python
# -*- coding:utf-8 -*-

import Image
import numpy as np
import matplotlib.cm as cm
import matplotlib.pylab as pl

def trans_line(r):
    if r < 0.35:
        s = 0.3*r
    elif r <= 0.65:
        s = 0.105+2.6333*(r-0.35)
    else:
        s = 1 + 0.3*(r-1)
    return s

rice_0 = np.asarray(Image.open('rice.png').convert('L'))/float(255)
(M,N) = rice_0.shape
fig = pl.figure()
ori_pic = fig.add_subplot(2,2,1)
ori_pic.imshow(rice_0,cmap=cm.gray,norm=pl.Normalize(vmin=0,vmax=1))
ori_pic.set_title('input image')

rice_1 = rice_0.copy()
for m in range(M):
    for n in range(N):
        rice_1[m,n] = trans_line(rice_0[m,n])
result_pic = fig.add_subplot(222)
result_pic.imshow(rice_1,cmap=cm.gray,norm=pl.Normalize(vmin=0,vmax=1))
result_pic.set_title('output image')
r = np.arange(0,1+0.001,0.001)
s = np.array([trans_line(rr) for rr in r])
trans_line_curve_fig = fig.add_subplot(2,2,(3,4))
trans_line_curve_fig.plot(r,s)
trans_line_curve_fig.set_title('s-r')
trans_line_curve_fig.set_xlabel('r')
trans_line_curve_fig.set_ylabel('s')
fig.suptitle('exp_1_2')
fig.savefig('exp_1_2.jpg')
```

```.python
			# -*- coding:utf-8 -*-
```
Python中#开头的都是注释，通常注释都是不起作用的，但这句注释放在程序开头，是一句有意义的注释。它告诉Python解释器，里面的代码我是用utf-8编码。不然的话，Python解释器会默认程序使用的是ASCII码。ASCII码我们以前接触过，比如\n，\t，A是65，a的值是97等等，但有个缺点，不能表示中文（注释很容易出现中文），所以解释器遇到了它不认识的字符便会报错，添加这句注释，解释器就知道你用的是utf-8编码，便不会对中文报错了。
```.python
			import Image
			import numpy as np
			import matplotlib.cm as cm
			import matplotlib.pylab as pl
```
就像上文所说的那样，这段代码是告诉Python解释器我要引入相应的类库，并以相应的缩写表示，这是为了在之后用到时可以少打几个字，看起来也清爽一些，不然如果每处都要写matplotlib.pylab肯定很痛苦。
```.python
			def trans_line(r):
			    if r < 0.35:
			        s = 0.3*r
			    elif r <= 0.65:
			        s = 0.105+2.6333*(r-0.35)
			    else:			
			        s = 1 + 0.3*(r-1)
			    return s
```
这段代码我们是来定义如下这段函数的，对于每个像素的灰度值都进行变换。
\\[ 
	s = \\left\\{
		\\begin{array}{lr}
			0.3r， & r < 0.35 \\\\
			0.105 + 2.6333(r-0.35)， & 0.35\\leq r \\leq 0.65\\\\
			1 + 0.3(r-1)， & r > 0.65.
			\\end{array}
		\\right.
\\]

```.python
	rice_0 = np.asarray(Image.open('rice.png').convert('L'))/float(255)
```
这句话我们一下子做了很多事情。

+ 首先,我们用打开图片，Image.open('rice.png')是打开图片，其中图片应该是要同程序文件放在同一目录下，如果不是同一目录，那应该再加上系统路径。
+ convert('L')是用来确保读入的图像是灰度图像，因为有的图像是伪装成灰度图像的彩色图像。
+ 经过上述步骤后，我们读入的其实还是一个Image类的对象，这一点，你可以在解释器中输入如下代码验证一下。
而np.asarray(Image_Object)这一步就是为了将Image对象转化为我们能处理的ndarray对象，也就是一个二维数组。
```.python
	img = Image.open('rice.png').convert('L')
	help(img)
```
+ 最后一步，由于我们读入图片的灰度是表示成0-255的，而要求的公式却是0-1的，所以我们要将灰度归一化。之所以要费事费力的写个float(255)
的原因想必你已经清楚了，如果还未明了，那么可以看一下我的另一片[拙作](../nao-ren-de-pythonchu-fa.html)。
```.python
(M,N) = rice_0.shape
```
这句话我们得到了读入矩阵的形状，其中M是行数，N是列数。shape是ndarray对象均有的属性。
```.python
fig = pl.figure()
```
既然要画图，那当然要有一个画图的窗口啦。这句话就是产生一个画图的窗口，目前我们没有对fig的大小做任何设置，因而便自动采用默认值也就是figsize=(8, 6)，再后期，我们会遇到一个窗口里需要里放下很多张图片，那时小小的640*480窗口便不够用了（figsize中的每一个单位默认代表80个像素）。我们可以指明我们所要的窗口大小。
```.python
fig = pl.figure(figsize=(16,12)) # 1280*960
```
```.python
ori_pic = fig.add_subplot(2,2,1)
```
说曹操曹操就到，刚讲过可能一个窗口里需要放下好几副话，这不来了嘛。subplot很熟悉吧，matlab里用过，就是将窗口分为几行几列的子窗口。括号内的第一个参数是行数，第二个参数是列数，第三个参数指定需要将图画在那个子窗口上，这个序号就是从第一行第一列的那个子窗口开始从左往右数的序号。严格一点，这里的子窗口叫做Axes对象，这不ax1就是一个我们当前要画图的Axes对象。
```.python
ori_pic.imshow(rice_0,cmap=cm.gray,norm=pl.Normalize(vmin=0,vmax=1))
```
Oh,yeah!到了这句，我们的任务已经阶段性完成了一大块了，接下去的都是类似的工作，恕我不能一一详述了。在上一句中，我们将第一个子窗口命名为ax1，现在便是用imshow函数将图片显示在ax1上。你可能会问，那为什么不是ax1.imshow(rice_0)这么简单了当就可以了呢？后面的又是什么东西？再次稍微罗嗦一下。

+ cmap=cm.gray 指明我们的颜色映射采用灰度图像，否则的话，imshow会启用默认的伪彩色，你得到的就是一张花花绿绿的rice了，这当然不是你想要得。
+ norm=pl.Normalize(vmin=0,vmax=1) 指明灰度映射时，将0映射成0,255映射成1。为什么要这么指明呢？这就是matplotlib蛋疼的地方了，它会默认进行灰度拉伸，如果你的一张图像的灰度值范围是120-220，那么它就会把120映射成0,220映射成1,造成不必要的错误。关于这一点，更多的内容可以看我的[另一篇文章](../jie-jue-matplotlibde-imshowxian-shi-shi-zhen.html)和[水木上的帖子](http://www.newsmth.net/nForum/#!article/Python/89271)。
```.python
fig.savefig('exp_1_2.jpg')
```
没错，保存图像就是这样，Python单双引号是一样的，只要在引号内输入你要的文件名即可，格式便是你输入的格式。至此，恭喜你大功告成～

## <div id="part3">如何开始之Matlab篇</div>
如果从头至尾看到这，想必你也清楚我的水平了，货真价实MADAO一个。。。

Matlab应该是在之前的课程中接触过了，如果感觉有困难的话，我也不误人子弟了，图书馆里的Matlab书籍汗牛充栋，人手一本绰绰有余，而这些工具书大体都相似，故也没什么好坏之分。


**出于整个页面排版的考虑，我将实验内容做成了独立的页面。如果你性急End一下就到了这边，那还请你再按下[Home](#part0)键，返回页首再选取实验内容。**
