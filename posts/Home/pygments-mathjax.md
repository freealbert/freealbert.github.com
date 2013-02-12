Title: 解决Pygments与MathJax的冲突
Author: freealbert
Date: 2012-8-17
Tags: pygments, mathjax, css


MathJax是个人认为一个非常赞的开源项目，它是一个用来在浏览器上显示LaTeX数学公式的JavaScript引擎，本站的所有公式都是由它生成的。

Pygments是一个用来做语法高亮的利器，由pXq一直关注的Pocoo团队出品，Pocoo出品，必属精品。

但当两者共同工作时却出现了一点小意外，我发现数学公式中的字母颜色变淡了，情况如下：

![](http://i.imgur.com/xI6ox.png)

但我使用highlight.js来做高亮时，却又是好的。

![](http://i.imgur.com/KdSfO.png)

这说明是Pygments和MathJax起了冲突。听从pXq的建议，我将Pygments的主题从default换成了vim。Pygments产生主题的语句如下：

```.bash
$ pygmentize -S vim -f html > pygments_vim.css
```

主题名称可以从[这里](http://pygments.org/demo/53718/)找到，在*Use this style:* 的右边。

换了vim主题后，情况就变成这样了。

![](http://i.imgur.com/0aNwi.png)

从水木上得知，Pygments是只改变CSS的，那有这种状况应该是Pygments的某个CSS特性将MathJax原先的给替换掉了，导致公式里的字母也跟着代码一样变得花花绿绿。

现在的问题就是要使两者的CSS作用域分开，最后还是pXq想出了方法。刚学了一点CSS知识，我也现学现卖一下。

看一下Pygments产生的高亮CSS文件的随便一句代码：
```.css
.hll { background-color: #ffffcc }
```

这句话表明，在整个网页中，只要属于hll类的元素都将具有background-color特性是#ffffcc这个效果。

但事实上，我们并不希望这样。我们希望整个页面包括数学公式中的字母默认就是黑色的，而只有代码段里的字母才会高亮。套用面向对象的说法，代码段里的效果是整体字母效果的一个子类。

看一下高亮代码段的HTML代码：

```.html
<div class="codehilite"><pre>    <span class="kn">import</span> <span class="nn">PIL.Image</span> <span class="kn">as</span> <span class="nn">Image</span>
</pre></div>
```

可以看到他们都是属于codehilite类的，那么我们只要让Pygments产生的那个CSS文件只对codehilite类生效就可以了。具体方式是在每行的最开头加上 .codehilite  ，这样指定只有属于codehilite的代码才会高亮。形式如下：

```.python
.codehilite .hll { background-color: #ffffcc }
.codehilite .c { color: #60a0b0; font-style: italic } /* Comment */
.codehilite .err { border: 1px solid #FF0000 } /* Error */
.codehilite .k { color: #007020; font-weight: bold } /* Keyword */
.codehilite .o { color: #666666 } /* Operator */
...
```

由此问题便解决了。

** 增加.codehilite只针对markdown文件，如果是rst文件，请将codehilite替换成highlight**
