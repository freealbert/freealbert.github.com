Title: Emacs-Prelude简介
Author: freealbert
Date: 2012-9-6
Tags: emacs

* [为什么需要Prelude](#whyPrelude)
* [安装Prelude](#installPrelude)
* [再次审视Prelude](#reviewPrelude)
* [定制Prelude](#customPrelude)
* [关于作者](#aboutAuthor)
* [参考资料](#reference)

## <div id="whyPrelude">为什么需要Prelude</div>

前天重装了一下Ubuntu，忘记了备份辛辛苦苦才攒起来的 .emacs配置文件。由于我不会Emacs Lisp，再重新搜罗一下还是件挺费力的事，[qq987](http://shiquanwang.github.com/)给我推荐了Emacs-Prelude，我尝试了一下，目前感觉很不错，跟大家分享一下。

在使用Emacs的时候，我们都会有这样的感觉，Emacs真是一个太棒的编辑器，可以根据自己的需求个性化的定制。但这其中有一个问题，在享受个性化定制带来的便利之前，我们有一个不得不经过的序幕或者说前奏曲，写.emacs文件。这需要用到Emacs Lisp，应该说是相当高的门槛。当然你可以同我一样，不会Emacs Lisp，从那些牛人的配置里扒一点适合自己的，勉强凑合一个，可是这个也很花时间啊，而且出了一堆error还不知道怎么办。总之，要是想将Emacs调教的千依百顺，这光源式养成计划长路漫漫，且并不平坦。

> **"Get me out of the Prelude, I just want to use Emacs" **

Prelude的出现，很大程度上的解决了这个问题，它会自动将Emacs配置得比较舒适顺手，让你直接跳过那个并不愉悦的前奏曲，这也就是Prelude这个名字的由来。

## <div id="installPrelude">安装Prelude</div>

* ### Emacs 24
Prelude需要Emacs 24，且不向前兼容，目前从Ubuntu的源里安装的Emacs还是23，如果你跟我一样，请先卸载。后执行如下代码（当然可以自己动手编译，不过我等懒人还是喜欢简单直接的，不过这个源实在有点慢）

```.bash
    sudo add-apt-repository ppa:cassou/emacs
    sudo apt-get update
    sudo apt-get install emacs-snapshot
```

* ### git & curl
由于需要用到git 和 curl，需要先安装一下

```.bash
    sudo apt-get install git curl
```

* ### 安装
在安装之前，请先确保将原有的 .emacs文件和 .emacs.d文件夹删掉，我之前反复安装不成功，就是这个原因，多亏了Tux的提醒。安装的过程仍然一贯的简单
```.bash
    curl -L https://github.com/bbatsov/prelude/raw/master/utils/installer.sh | sh
```
更多的安装方法可以点[这里](http://batsov.com/prelude/) 和[这里](https://github.com/bbatsov/prelude)。
事实上，应该只要从其[github的项目主页](https://github.com/bbatsov/prelude)上将文件夹下下来，再重命名成 .emacs.d 放到Home下就可以了。

之后，启动Emacs，Prelude会自动安装不少东西，请稍微耐心等待一下。再次启动后，就会发现Emacs的背景色变成如下了，这是因为Prelude的配色方案默认启用了zenburn主题。

![](http://i.imgur.com/B2rRm.png)

## <div id="reviewPrelude">再次审视Prelude</div>
至此，Prelude的安装便算完成了。可是Prelude对于我一个一点也不会Emacs Lisp的菜鸟来说，还只是一只一无所知的黑箱子，我只知道Prelude预设了很多便利给我，但究竟是哪些呢，我又该怎么用呢？

我适当的摸索了一些，写在下面，如果你知道更多，也请告诉我～

### Prelude的便利

首先看上图，我们可以知道Prelude至少给了我们以下这些福利：

* 取消了启动画面
* 取消了菜单栏和工具栏
* 启用了一个不错的配色主题
  [zenburn](http://slinky.imukuppi.org/zenburn/)
* 显示行号和列号

接触更多，我们还会发现更多惊喜的，比如如下这个简短的hello.py

![](http://i.imgur.com/lDyRb.png)

* 启用了yasnippet
* 启用了whitespace mode
* 引号和括号自动补全
* 高亮当前所在的行
* minibuffer里的路径文件夹补全

其中，在每行的末尾都有一个美元符号$，以及缩进均有小点来标识，这就是whitespace mode，它实在是太赞了！

以前，在markdown模式下，yasnippet一直都不能用，我也搜寻了一些方法，但始终无效，现在这个问题不复存在，可以尽情的在编写markdown时使用yasnippet。

### 更多便利

Prelude预先定义了不少快捷键，我挑选了一些我常用的列举在下，更多的请阅读 [ prelude-global-keybindings.el ](https://github.com/bbatsov/prelude/blob/master/prelude/prelude-global-keybindings.el) 

<table border="1" width="600">
    <thead>
        <tr>
            <th>功能描述</th>
            <th>快捷键</th>
            <th>备注</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>redo</td>
            <td>C-/</td>
            <td>replacement of "C-x u"</td>
        </tr>
        <tr>
            <td>backward-kill-word</td>
            <td>C-M-h</td>
            <td>You know, like Readline.>
        </tr>
        <tr>
            <td>align-regexp</td>
            <td>C-x \\</td>
            <td>Align your code in a pretty way.</td>
        </tr>
        <tr>
            <td>text-scale-increase</td>
            <td>C-+</td>
            <td>Font size increase</td>
        </tr>
        <tr>
            <td>eshell</td>
            <td>C-x m</td>
            <td>Start eshell or switch to it if it's active.</td>
        </tr>
    </tbody>
</table>

容许我再对其中某两个快捷键罗嗦几句，因为我实在太喜欢了～

* align-regexp C-x \\

    套用[Lucifr](http://lucifr.com/)的大作
    [Sublime Text 2 入门及技巧](http://lucifr.com/139225/sublime-text-2-tricks-and-tips/)
    中的例子：

    对于某些喜欢整齐的程序员来说，看到下面这种情况可能是让其无法忍受的：
```.js
    var joe = 'joe';
    var johnny = 'johnny';
    var quaid = 'quaid';
```
    
一定要改成这样才会安心：
 
```.js
    var joe    = 'joe';
    var johnny = 'johnny';
    var quaid  = 'quaid';
```
    
这个功能可以通过输入C-x \\后再输入等号= （也就是你想要对其的符号）来对齐。

* redo C-/

以前我用CUA-mode，原因只有一个，那就是C-x u不方便，Prelude很贴心的设置
了C-/来替代。

### Prelude的不便
就像硬币总是有两面一样，Prelude预置的许多功能可以极大的方便我们，但事情总没有我们预想的那么十全十美，对我来说，Prelude至少有以下不足：

* 禁用了方向键以及Home,End,Delete键
* 缺少快速注释和反注释
* 缺少行号的显示

其中的第一点，称其不足，应该说委屈Prelude了，我想作者一定是故意为之，禁用了上下左右方向键以及Home，End，Delete，那么我们只能以C-p，C-n，C-b，C-f和C-a，C-e，C-d来代替，更加纯粹的Emacs，不是吗？俗话说，水至清则无鱼，作为笔记本用户，对此表示压力山大，左手经常要缩成鸡爪状，很不舒服。为什么要跟自己过不去呢？

PS: [pXq](http://pxqing.me/) 现在已经在研究如何制造脚踏板了～

关于如何消除这些不便，我们将在下一节讨论。

## <div id="customPrelude">定制Prelude</div>

Prelude不能让你100%的满意，没关系，我们可以自己动手，在~/.emacs.d文件夹下有一个 personal文件夹，
这里你只需新建一个后缀命是el的文件，即可开始定制，如我，是
myconfig.el.

* ### 重新启用方向键
```.cl
    ;; Re-enable the arrow keys
    (defun disable-guru-mode ()
    (guru-mode -1)
    )
    (add-hook 'prelude-prog-mode-hook 'disable-guru-mode t)
```
除了方向键，还有Home,End,Delete这些键也同时恢复了功能。

* ### 设置字体
```.cl
    ;;设置字体
    (set-frame-font "monaco-12")
```
显示代码我用的是monaco，感觉很不错，如果系统还没有安装，可以Google一下。
字体安装在Ubuntu下极其简单，只需要双击打开字体文件（一般是OTF或者TTF文
件）后，点击install即可。

其实Emacs会读取系统默认的字体，比如我在myunity里就将等宽字体
(Monospace)设置成了monaco，其余均是苹果冬青黑，所以这一行配置其实是句废话。

* ### 更换颜色主题

配色主题采用的是，(almost-monokai)[https://github.com/lut4rp/almost-monokai/]，顾名思义它是仿照TextMate下的monokai主题。由于它需要依赖[color theme](http://www.emacswiki.org/emacs/ColorTheme)，所以我们需要先安装它。

1.安装color theme
M-x package-install 回车后继续输入color-theme再回车即可。

2.从[almost-monokai的Github主页](https://github.com/lut4rp/almost-monokai/)上将其下载并解压后，把color-theme-almost-monokai.el文件放到~/.emacs.d/themes文件夹下，然后在配置文件（我是~/.emacs.d/personal/myconfig.el)内加入如下代码即可

```.cl
    ;; color theme
    (load-file "~/.emacs.d/themes/color-theme-almost-monokai.el")
    (color-theme-almost-monokai)
```

* ### 注释和反注释

```.cl
    ;; Comment and Uncomment
    (defun comment-or-uncomment-line-or-region ()
    "Comments or uncomments the current line or region."
    (interactive)
    (if (region-active-p)
    (comment-or-uncomment-region (region-beginning) (region-end))
    (comment-or-uncomment-region (line-beginning-position) (line-end-position))
    )
    )
    (global-set-key "\M-," 'comment-or-uncomment-line-or-region)
```
这里我们将M-,设置为注释和反注释的快捷键。当选中某块区域时，可以将该区
域注释或者反注释；而当不选中时，则对当前行进行操作。

* ### 取消 whitespace-mode
我很喜欢 whitespace-mode，但也看到不少人不喜欢它。不喜欢，那便可以取消
它，代码如下:

```.cl
    (add-hook 'prog-mode-hook 'prelude-turn-off-whitespace t)
```

## <div id="aboutAuthor">关于作者</div>

Prelude的作者名叫**Bozhidar Ivanov Batsov**，来自**保加利亚**的Veliko
Tarnovo，目前居住于其首都*Sofia*。

Batsov是一家主打商务社交的网站[tradeo.com](https://tradeo.com/)的
Technical Lead，负责开发基于Ruby on Rails的各种应用，曾经是Java工程师，
更早的时候则是C++工程师，而他的老本行则是基于Linux内核的嵌入式开发。
Batsov的经历，基本就是从低层逐渐往高层走的过程。

除了编程外，Bastov总是为Unix-like的操作系统着迷，最喜爱的编辑器是Emacs
（不然也不会制作Prelude啦），常用的shell是zsh，使用git来做版本控制。

最后上一张Bastov的靓照

![Bastov](http://batsov.com/images/articles/bozhidar.jpg)

## <div id="reference">参考资料</div>

1. [WikEmacs-Prelude](http://wikemacs.org/wiki/Prelude)
2. [Batsov's blog](http://batsov.com/)
3. [Prelude's github page](https://github.com/bbatsov/prelude)
4. [Prelude's Home](http://batsov.com/prelude/)
5. [Batsov's linkedin profile](http://www.linkedin.com/in/bozhidarbatsov)
6. [tradeo.com](https://tradeo.com/)
