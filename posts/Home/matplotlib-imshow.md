Title: 解决matplotlib的imshow显示失真
Author: freealbert
Date: 2012-4-18
Tags: python,matplotlib

我用python写了数字图像处理的上机实验，做到最后一小题处理cell的时候，发现用imshow显示读入的图片发现明显跟直接打开图片看不同。回去看之前的题目，都跟原图有出入。
原图如下

![](http://i.imgur.com/Bs0YH.jpg)

打开后的失真图像如下

![](http://i.imgur.com/Znksp.jpg)

这是我的代码片段：
```.python
im_0 = np.asarray(Image.open('cell.jpg').convert('L'))
fig = pl.figure(figsize=(8,4))
ax_0 = fig.add_subplot(121)
ax_0.imshow(im_0,cmap=cm.gray)
```

由于imshow默认是显示伪彩色，所以colormap用了gray。仔细看对比两张图片可以发现，失真的图片很像是对原图做了灰度拉伸操作，故而变得比原图像清晰了。苦于找不到原因，我在水木的Python版上发了帖子求教，经过xgr和DaNei两位热心兄台的提点，我最终找到了原因和解决的途径。

原来，matplotlib的imshow函数显示灰度图像时，会对图像矩阵进行归一化，就是把矩阵中最小的灰度值(vmin)作为0，最大的灰度值(vmax)作为1，然后重新给colormap赋值 。用getextrema函数可以查看图像灰度值的最大值和最小值，cell的最大灰度值为138，最小灰度值为90。也就是说90～138会被线性拉伸成0~255。如果显示图片时，可以设置norm的值显式地令vmax=255，vmin=0，则可以显示这个问题，相应的，0～1的浮点数矩阵，vmax=1，vmin=0。

```.python
ax4.imshow(C[:,:,1],cmap=cm.gray,norm=pl.Normalize(vmin=0,vmax=255))
```

下图是设置后的图片，跟原图一模一样。

![](http://i.imgur.com/4Ru2t.jpg)
