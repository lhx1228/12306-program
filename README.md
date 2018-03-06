# python实现12306相关功能

标签：python

# 做一个更适合自己的12306

---

## 测试环境

python 3.6

## 代码功能

① 查询所有有剩余车票的列车以及可以选择的座位类型

② 输入时间范围，筛选出可以乘坐的列车

## 前期准备

我们进入**12306的车票预定页面**[点击这里](https://kyfw.12306.cn/otn/leftTicket/init),按下F12(我这里使用的是Chrome浏览器),输入出发地，目的地等信息后，会在开发者工具中看到一个这样的信息:

![](http://119.29.89.242/image/12306-1.PNG)

之后我们点击**queryZ?...**文件，查看**Headers**信息，复制**Request URL**里面的链接，在浏览器中打开，出现下图的画面:

![](http://119.29.89.242/image/12306-2.PNG)

## 分析过程

根据上图，我们发现有一个字段为**data**，而**data**中又有**map、result等**。不难发现，**map指的是我们输入的出发地和目的地；** **result是符合条件的全部列车班次。**

我们以其中一个班次为例：**VdJ3y1kMfVPLUzMR7lZ43Pwe%2FD6mV2irnkO%2BO8QcEPd4ErXyDUUYG0V49nmwGdVhLlBRZ%2B6ofYIo%0A7JL9OVXnvvXSeFut9EIdvTgpphWYDGswQh6MwfxVgOiDygJd1f4iREQq4zYj8Ztwnhk5xHGbB6Km%0Annk93ZQYKhhYcVXLSVAkqoZ25IaY4qdKevsBNsJVrOn1nR9WVyN3Uv2CFPk5uGPKApEh8544J7SF%0Ay1kct4P9pUvhTprLrLHjhWX1B1A%2BTfsMkg%3D%3D|预订|240000K18333|K183|BJP|NFF|BJP|AYF|13:06|21:15|08:09|Y|2EHmn1ZE9c%2BPwxtZJ10%2FO0QlrjwwNJybcXPjn%2BayDKlBYKYKeZts0%2B6ZU%2FY%3D|20180203|3|PA|01|07|0|0||||7|||有||6|无|||||10401030|1413|0**

分析这个字段，发现**预订|240000K18333|K183|BJP|NFF|BJP|AYF|13:06|21:15|08:09|Y|2EHmn1ZE9c%2BPwxtZJ10%2FO0QlrjwwNJybcXPjn%2BayDKlBYKYKeZts0%2B6ZU%2FY%3D|20180203|3|PA|01|07|0|0||||7|||有||6|无|||||10401030|1413|0**为有效信息。

其中，**240000K18333应该为列车的编号；K183为列车名称；BJP|NFF|BJP|AYF为map字段；13:06|21:15|08:09分别为出发时间，到达目的地时间，列车到达终点的时间；Y表示还有剩余的票，如果为N则表示票已售完；20180203明显为我们查询的日期；已'|'为分隔符，列车名称(K183)后的第20，21，22，23，24，25，26，27，28，29，30字段分别表示软卧，软座，商务特等座，高级软卧，无座，硬卧，硬座，二等座，一等座，商务特等座，动卧；**

## 代码实现

分析完各个字段的意义，我们考虑如何实现上述功能。

我采用的是**requests库配合正则表达式来实现的。**

现在我们分析上面提到的**Headers**信息中**Request URL**里面的链接：**https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-03&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=AYF&purpose_codes=ADULT**

容易发现**leftTicketDTO.train_date**字段为我们选择的日期，**leftTicketDTO.from_station**字段为我们的出发地，**leftTicketDTO.to_station**字段为目的地，所以我们可以用一个字典存入地点的中文名称和缩写，然后使用"url = 'http://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(time,from_where,to_where)" 来表示url，之后使用requests模块来实现一系列的操作。

具体实现过程请参考[12306.py](https://github.com/lhx1228/12306-program/blob/master/12306.py)代码。


而[sendmail-12306.py](https://github.com/lhx1228/12306-program/blob/master/sendmail_12306.py)为发送邮件的代码，可以用来自动检测，如果有余票，会自动给邮箱发邮件。


## 代码截图

![](http://119.29.89.242/image/12306-3.PNG)

![](http://119.29.89.242/image/12306-4.PNG)

## 代码地址

[12306-program](https://github.com/lhx1228/12306-program)