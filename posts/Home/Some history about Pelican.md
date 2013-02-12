Title: Some history about Pelican
Author: freealbert
Date: 2012-7-23
Category: Tech
Tags: pelican, python, web

> 这篇文章翻译自Pelican的文档，主要讲述了Pelican的技术方案，[原文请点此](http://pelican.notmyidea.org/en/latest/report.html)。

***<pre>提示：这篇文章是由Pelican的作者Alexis Métaireau在2010年12月写的，有些信息也许已经过时了。</pre>***

Pelican 是一个简单的静态博客生成器。它分析由Markdown或是reStructuredText写就的标记语言文档，并产生一个包括了建博客所需的所有HTML文件的文件夹。考虑到Python语言较为简单且能满足我的所有需求，我选择了它来开发Pelican。我并不想为每一样事物都定义一个类(class)，但仍希望所有东西都能宽松的耦合。结果证明这正是我想要的。也要感谢一些用户们时不时的极有价值的反馈，我每次都只需很少的时间来修复一些bug。到目前为止，我已经彻底重构了 Pelican 的代码两次，每次都不到30分钟。

## Pelican的方案
早先，我是WordPress用户，WordPress是用PHP语言开发的博客平台，支持在PHP和MySQL的服务器上架设并管理自己的博客。大多数时候，我更喜欢用诸如Markdown、reStructuredText这样的标记语言来写文章，还有，我都是用vim来写的！（译者注:Alexis是vim党）我觉得让人们有选择他们自己喜欢的文本编辑器来写文章的自由是非常重要的！在我看来，一个博客管理器只要能把无论什么格式的输入文件转化成一个博客这件事做好就可以了。这就是Pelican的用途，可以让你选择你钟爱的任何编辑器，使用你想用的标记语言，来生成一个静态的HTML博客站点。
![alt text](https://github.com/freealbert/freealbert_photo_1/blob/master/Tech/overall.png?raw=true  "overall")

出于足够灵活的考虑，Pelican提供模板支持，只要你想要，便能轻松地写出你自己的模板。

## 设计过程
Pelican 来自我个人的需求，起初，它只是只有一个文件的程序，渐渐的，它已经茁壮成长成现在这样了。最初，我写下我希望能够实现的功能，然后写了一个reStructuredText文件来作为语法分析的测试用例，并开始反复试验和修改代码。当Pelican第一次可用时，它有200行代码，包含了差不多10个函数和一个类

开发过程中，总是会冒出各种各样不同的问题，而我也总是想实现更多的功能。支持setting file，是我想要添加的第一个功能。在这之前，Pelican其实也可以通过命令行传递一些选项来实现设置功能，但当选项一多，这样做就十分繁琐和无聊了。后来，以同样的方式，我添加了Atom feeds,多种主题，多种标记语言支持等等。某种意义上这表明，我把Pelican程序全写在一个文件里是有问题的，因此，我决定全部推倒，把程序分散到多个不同的文件里，从头再写一遍。

从逻辑的角度出发，我区分了一些类和内容

+ writer类，负责生成最终的所有文件，不管是.html文件还是RSS feeds或是其它东西。writer对象一产生，接着便是将它们传递给generator对象。

+ reader类，可以读入不同格式的文件（目前还仅支持Markdown和reStructuredText，但系统是可以扩展的),给定一个文件，返回诸如作者、标签、分类目录这样的元数据以及html格式的内容。

+ generator类生成不同的输出。举个例子，Pelican有一个文章生成器（ArticlesGenerator）还有一个页面生成器（PagesGenerator），他们一块来生成些别的东西。给定一个配置，他们便会按照你的配置去做。多数情况下，pelican根据用户输入的文件来产生输出。

我还处理了那些容器对象，不管是Aticles,Pages,Quotes还是你自己定制的，所有用来展现内容的对象都可以在contents.py里被定义。

## 更多细节
这是一张Pelican所有类的关系图.
![alt text](https://github.com/freealbert/freealbert_photo_1/blob/master/Tech/uml.jpg?raw=true "uml")


由于我用了鸭子类型，而不是接口，所以上图中的接口(interface)并不存在，之所以画出来，只是为了让整幅图像更加清晰而已。
Pelican内部是这么运行的：

* 首先，对用户输入的命令行进行语法分析，其中的某些内容被用来初始化不同的generator类的对象。
* 接着，产生一个context，它包含一些从命令行的来的设置，如果有setting file的话，还要包括setting file。
* 然后，每个generator对象的generate_context方法被调用，更新context。
* 最后，writer对象被创建，并被传递给每个generator对象的generator_output方法。

我觉得当不同的 generator 对象产生了各自的输出后，保持内容的不变非常重要，所以我用了两个调用函数。换句话说，只有第一个 generate_context 方法被允许修改context，而第二个 generator_output 方法绝不可以。对于 generate_context 方法和generator_output方法，合理的就是只做他们应该做的事。下面是调用ArticlesGenerator类的generate_context 方法时所发生的事情，或许能帮助理解：

+ 读入文件夹路径，找寻restructuredtext，每载入一个文件，先用reader对象读入，然后构造一个Article类的内容对象
+ 更新所有读入的文章的context

最后，generate_content方法用context 和writer来生成你所想要的最终的输出。

> <pre>本作品采用*自由转载-非商用-非衍生-保持署名 | [Creative Commons BY-NC-ND 3.0](http://creativecommons.org/licenses/by-nc-nd/3.0/deed.zh)*进行许可。</pre>

感谢我的好友*[pXq](http://panxiuqing.github.com/)*审阅了本文并提供了宝贵的建议。
