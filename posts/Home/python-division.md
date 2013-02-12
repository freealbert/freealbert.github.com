Title: 恼人的Python除法
Author: freealbert
Date: 2012-3-21
Tags: python


没搞清楚Python的除法已经变成最多的语义错误来源咯，所以今天好好看了下Learning Python。

在Python里一共有三种除法，分别是：

* 传统除法：对于操作数均为整数时结果会省去小数部分，对于操作数中有浮点数时，就会保留小数部分，也就是说，传统除法的结果是依赖于操作数类型的。Python2.x用 / 表示

* 真除法：无论操作数是任何类型，结果均为保留小数的浮点数。Python3.x中用 / 表示。

* Floor除法：不考虑操作数类型，结果总会省略掉小数部分。Python2.x和Python3.x中均用 // 表示。

<table width="600" border="1" align="center">
<tr>
<td></td>
<td>Python2.x</td>
<td>Python3.x</td>
</tr>
<tr>
<td>传统除法</td>	<td>X/Y</td><td>无</td>
</tr>
<tr>
<td>真除法</td><td>无</td><td>X/Y</td>
</tr>
<tr>
<td>Floor除法</td><td>X//Y</td><td>X//Y</td>
</tr>
</table>
有一点需要提醒，虽然Floor除法总是省略小数，但并不是说其结果总是整形数。结果还是根据操作数的类型来的，比如：
```.python
>>>1//3
>>>0
>>>1.0//3
>>>0.0
```
 
