# download_ituring_free_books

## 工程缘起

在简书上看到相关的文章，觉得很有意思，于是就自己实现了一遍。有别于作者的是他只提供了《码农》的下载，而我一开始也打算以这样的思路来做。但是在图灵社区官网上看到有专门的免费的一栏（如下图所示），于是就开始了踩坑之路。

![爬取的起始页](https://github.com/wmltyq/download_ituring_free_books/blob/master/img/爬取的起始页.jpg)

## 工程难点

一开始以为挺简单的，通过 URL 构造就能把每个分页的地址构造出来，但是点击其他分页的时候发现浏览器地址栏根本没有变化。于是我用浏览器的开发人员工具的 Network 看了一下数据包，原来请求的数据地址跟我们平常访问的地址不太一样。因为有细微的区别，一开始没怎么注意到还为此纠结了好久……

地址的问题算是解决了，然后就开始一边写一边运行一边重构了。虽然期刊数量不是很多，但是好歹也有三十多，我不可能每页都去点开一下查看是否符合编码的规律，我只能先写个 Demo 运行看看有没有什么问题，遇到问题了再看一下具体是哪一页出了什么问题。发现并不是所有的《码农》都显式提供了下载链接，有的需要登录后点击”购买电子书“按钮才能获取下载链接（如下图所示）。所以忽然有点佩服那些做大数据的，怎么在海量的数据中剔除或者筛选出必要的数据。

![默认没有显式提供下载链接](https://github.com/wmltyq/download_ituring_free_books/blob/master/img/默认没有显式提供下载链接.jpg)

![登录购买后才能看到下载链接](https://github.com/wmltyq/download_ituring_free_books/blob/master/img/登录购买后才能看到下载链接.jpg)

这样折腾一番后，算是整体跑通了。于是我开始不满足只能下载《码农》了，我想下载尽可能多的免费电子刊。于是我又分析了一下所有免费电子刊的页面再对比写好的代码，发现只要修改一下起始 URL 几乎就可以完美运行了。跑着跑着好像还挺顺利的，但不一会儿给我来了一个“由于连接方在一段时间后没有正确答复或连接的主机没有反应,连接尝试失败”的提示。我就在想，码农何必为难码农啊。折腾了好久焦虑了好久，算是马马虎虎搞好了。

## 工程总结

除了《码农》以外的电子刊（工程完成时只有三本《码农》没有显式提供下载链接），其他免费的能下载下来的也不是很多，而且大多数默认只提供了 epub 的版本，如果想下载到 pdf 版本的只能手动登录后购买再下载了。但是好歹也比只能下载《码农》强一点吧，最终运行效果如下图所示：

![部分电子书没有显式提供下载链接](https://github.com/wmltyq/download_ituring_free_books/blob/master/img/部分电子书没有显式提供下载链接.jpg)