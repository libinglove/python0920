import pandas as pd  #数据框操作
from pandas import options

import matplotlib.pyplot as plt #绘图
import matplotlib as mpl #配置字体


mpl.rcParams['font.sans-serif'] = ['SimHei'] #这个是绘图格式，不写这个的话横坐标无法变成我们要的内容
#配置绘图风格
plt.rcParams['axes.labelsize'] = 8.
plt.rcParams['xtick.labelsize'] = 12.
plt.rcParams['ytick.labelsize'] = 12.
plt.rcParams['legend.fontsize'] =10.
plt.rcParams['figure.figsize'] = [8.,8.]

data = pd.read_excel('lagou2.xlsx',encoding='gbk') #出现错误的话试试utf8，路径不能出现中

# 算出各个城市招聘的信息
city_info = data.groupby('工作地点')['工作地点'].count()
print(city_info)

# 算出总的招聘信息
city_total = city_info.sum()
print(city_total)

# 算出比例
bili = 100.00 * city_info / city_total
print(bili)

# 转换成二维
city = city_info.to_frame('招聘数量')

city.insert(0,'比例',bili)

options.display.float_format = "{:,.2f}%".format

labels = city.index.tolist()
plt.pie(city_info,autopct='%.2f%%',labels=labels)

plt.title("各个城市的招聘数量占比图")
#设置示例
plt.legend(labels)

plt.show()