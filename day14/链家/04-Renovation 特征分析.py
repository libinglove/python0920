import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style({'font.sans-serif':['SimHei','Arial']})

# 导入链家二手房数据,
lianjia_df = pd.read_csv('lianjia.csv')
#查看前面2部分
# print(lianjia_df.head(n=2))

# 检查缺失值情况，发现了数据集一共有`23677`条数据，其中`Elevator`特征有明显的缺失值。",
# lianjia_df.info()

#结果给出了特征值是数值的一些统计值，包括平均数，标准差，中位数，最小值，最大值，25%分位数，75%分位数。这些统计结果简单直接，对于初始了解一个特征好坏非常有用，比如我们观察到 `Size` 特征 的最大值为1019平米，最小值为2平米，那么我们就要思考这个在实际中是不是存在的，如果不存在没有意义，那么这个数据就是一个异常值，会严重影响模型的性能。"
# print(lianjia_df.describe())
# 添加新特征房屋均价,
df = lianjia_df.copy()
df['PerPrice'] = lianjia_df['Price']/lianjia_df['Size']
# 重新摆放列位置\n",
columns = ['Region', 'District', 'Garden', 'Layout', 'Floor', 'Year', 'Size', 'Elevator', 'Direction', 'Renovation', 'PerPrice', 'Price']
df = pd.DataFrame(df, columns = columns)


df['Renovation'] = df.loc[(df['Renovation'] != '南北'), 'Renovation']
# 画幅设置\n",
f, [ax1,ax2,ax3] = plt.subplots(1, 3, figsize=(20, 5))
sns.countplot(df['Renovation'], ax=ax1)
sns.barplot(x='Renovation', y='Price', data=df, ax=ax2)
sns.boxplot(x='Renovation', y='Price', data=df, ax=ax3)
plt.show()