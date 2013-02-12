Title: 高维真理
Author: freealbert
Date:  2012-7-30
Tags: electromagnetic

最近发现PDF对于[PyEE](https://github.com/freealbert/PyEE)并不是一种非常好的载体，我就寻思着将整个项目搬到web上去，希望借助于超链接和日新月异的技术能够让PyEE的表现力更强，也更为美观。接触Web开发，不可避免的便要学习HTML,CSS,Javasript这三座大山。
起初，我并不知道有CSS这种东西，直到现在我还每每将其读成CCS。但当我了解了CSS究竟是用来做什么的时候，一种熟悉感油然而生。先来看一下维基百科上说为何要采用CSS
> CSS最主要的目的是将文件的结构（用HTML或其他相关的语言写的）与文件的显示（CSS）分隔开来。这个分隔有许多好处：
>
> * 文件的可读性被加强
  * 文件的结构更加灵活
  * 作者和读者可以自己决定文件的显示
  * 文件的结构简化了。

笼统的概括一下CSS背后的目的，分工尽量精细，让每一样事物尽量专注自己的领域。这种想法，并不惟CSS独有，LaTeX也有自己事先定义好各种模板，目的也是为了让使用者更加专注与内容本身，而不是外观。再推远一点，面向对象编程出现的背后，同样是这种思想在推动。不止是编程领域，这种思想存在于这个世界的角角落落，因为把这种思想再精简一点，便是流水线。人类社会的发展一直便是分工尽量精细的过程，得益于工业化，全世界的流水线大大加速，小到一个CSS文件，大到一个人乃至一个国家实体，都是这亘古运转的流水线上的一环。

在这里，我不想讨论社会的流水线化是否会一直持续，精细分工究竟是好是坏。我更加关心的是，为何，这个世界上风马牛不相及的领域内会有相同的现象，抑或法则，抑或真理。
这个疑问，从我高一学习化学的时候便开始困扰我。

在有机化学中，当氢原子要脱落时，首先会从氢原子本来就少的碳原子上脱落；反之，当氢原子要增加时，首先增加的却是氢原子本来就多的碳原子上。这种现象与经济学上贫者愈贫，富者愈富，赢家通吃的经济学中收入分配不公的现象同样被称为马太效应。还有许许多多的其他领域同样存在着马太效应。

这么多不同领域却有着相同原理的现象背后，我并不认为这是一种巧合，也许，这个世界的确存在一个同一的真理。
再举一个我们熟悉的例子，大统一场理论（也称为万物之理），它是物理学家一直试图用同一组方程式描述全部粒子和力(强相互作用、弱相互作用、万有引力、电磁相互作用四种人类目前所知的所有的力)的物理性质的理论或模型。

我觉得，这个世界或许远不止弦论描述的是10维或是超弦理论描述的11维，很可能存在更高的维数，100维，抑或无穷维也有可能。在那里只存在着一条真理，但由于我们只能感知到空间的三维和时间的一维，于是我们对真理的认识也是非常片面的。每学科的研究都如盲人摸象一般，只能研究到高维真理的一小块碎片而已。这也可以解释为何在不同的学科之间存在相同的原理，因为他们本来就属于统一高维真理，只不过由于我们的视界只有四维，真理被碎片化了，但总有一点还是相同的。而不同的学科研究，便是沿着不同的山路攀爬同一座山峰。到了山顶，所有风景都是相似的。

我还可以提供一个有趣的例子，以供思考。

天线的辐射方向图其实是电流分布在天线上的傅立叶变换。下式是远区场的情形：
$$E_{\theta}=\int_{-l/2}^{+l/2}dE_{\theta}=j\eta\frac{ke^{-jkr}}{4\pi r}\sin{\theta}[\int_{-l/2}^{+l/2}I_{e}(x',y',z')e^{jkz'\cos{\theta}}dz']$$

公式右边的中括号内，便是不折不扣的傅立叶变换。这么样，为何无线小偶极子不会有旁瓣也就很容易解释了，因为冲击函数的傅立叶变换是1，每个方向都是均匀的，也就不会有旁瓣。

下图是一张矩形缝隙天线的辐射方向图，来自维基百科，从图中可以看出，正好是一个Sinc函数。众所周知，门函数的傅立叶变换便是Sinc函数。
![alt text](https://github.com/freealbert/freealbert_photo_1/blob/master/Tech/sinc.jpg?raw=true "sinc")

关于旁瓣和傅立叶变换的关系，更多的资料可以[点此](http://en.wikipedia.org/wiki/Side_lobe)。

最后，附上我天线大作业的[幻灯片](http://dymslide-freealbert.dotcloud.com/antenna-2012-6-28/antenna.html)，主要内容为无限小偶极子天线的辐射方向图以及旁瓣和傅立叶变换的关系，我将它改成了HTML5的形式，可以在线浏览。