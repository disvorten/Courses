import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mean
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_excel('data1.xlsx',sheet_name='по дням',header=None,skiprows=[0,1,3],index_col=0)
work = df.iloc[1:,0:21]
delta = np.array(work.max()) - np.array(work.min())
Names = df.iloc[0,0:21]
work1 = df.iloc[1:,22:44]
delta1 = np.array(work1.max()) - np.array(work1.min())
fig, ax = plt.subplots()
ax.set_title('1 задача',loc='center')
ax.set_xlabel('$delta$,мм',c = 'r',fontsize = 15)
ax.set_ylabel('$Names$,мм',c = 'r',fontsize = 15)
ax.grid(which='major',linewidth=1.1)
ax.grid(which='minor',linestyle='--',color='g',linewidth=0.5)
ax.plot(delta,Names,linewidth = 1)
#----------------------------------------------------------------
df1 = pd.read_excel('data1.xlsx',sheet_name='по неделям',skiprows=[0,1,3],index_col=0,header=None)
work2 = df1.iloc[0:,22:44]
work2.to_csv('res.csv')
work2 = pd.read_csv('res.csv',usecols=[i for i in range(1,23)],skiprows=[0])

#sns.heatmap(work2.corr(), annot=True, linewidths=0.5)
#--------------------------------------------------------------------
df_w = pd.read_excel('data1.xlsx',sheet_name='по неделям', skiprows=[0,1,3])
df_w_week = df_w.iloc[0:,45:]
week_19 = np.array(df_w_week.iloc[51,0:])
week_20 = np.array(df_w_week.iloc[108,0:])
week_21 = np.array(df_w_week.iloc[164,0:])
df_clear = df_w.drop([51,108,164]).iloc[0:,45:]
av_year19 = np.array(df_w_week.iloc[0:51,0:].mean())
av_year20 = np.array(df_w_week.iloc[51:108,0:].mean())
av_year21 = np.array(df_w_week.iloc[108:164,0:].mean())
#----------------------------------------
df1 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],header=None)
Data = np.array(df1.iloc[1:,0:1])
work2 = df1.iloc[0:,np.r_[0,45:67]]
work2.transpose().to_csv('r.csv')
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)],skiprows=(1))
r = []
Names = work2['категория']
for el in Names:
    for _ in range(work2.shape[1]-1):
        r.append(el)
work2 = work2.transpose().drop('категория')
full_data = []
for i in range(work2.shape[1]):
    full_data.append(work2[i])
full_data = np.array(full_data).reshape(46*22)
Dates = []
for _ in range(work2.shape[1]):
    for i in range(work2.shape[0]):
        Dates.append(Data[i])
full_data = np.array(full_data).reshape(work2.shape[1]*work2.shape[0])
Dates = np.array(Dates).reshape(work2.shape[1]*work2.shape[0])
final = pd.DataFrame()
final['Data'] = Dates
final['Category'] = r
final['value'] = full_data
fig = px.line(final, x="Data",y = "value", markers=True,color="Category")
#fig.show()
#-----------------------------------
df_m = pd.read_excel('data1.xlsx',sheet_name='по месяцам', skiprows=[1], index_col=0)
df_m_fit = df_m['автосервис']
av_spr19 = [df_m_fit['2019-10-01'],df_m_fit['2019-04-01']]
av_spr20 = [df_m_fit['2020-10-01'],df_m_fit['2020-04-01']]
av_spr21 = [df_m_fit['2021-10-01'],df_m_fit['2021-04-01']]
av_spr22 = [df_m_fit['2022-10-01'],df_m_fit['2022-04-01']]

d = df_m.drop(['2019-04-01','2019-10-01','2020-04-01','2020-10-01','2021-04-01','2021-10-01','2022-04-01','2022-10-01'])['автосервис']
av_ye19 = mean(d['2019-01-01 ':'2019-12-01'])
av_ye20 = mean(d['2020-01-01 ':'2020-12-01'])
av_ye21 = mean(d['2021-01-01 ':'2021-12-01'])
av_ye22 = mean(d['2022-01-01 ':])
Dates=['2019','2020','2021','2022']
oct=[av_spr19[0], av_spr20[0], av_spr21[0], av_spr22[0]]
apr = [av_spr19[1], av_spr20[1], av_spr21[1], av_spr22[1]]
year=[av_ye19, av_ye20, av_ye21, av_ye22]
width=0.3
x = np.arange(len(Dates))

fig, ax = plt.subplots(figsize=(10, 10))


ax.bar( x-width, oct, width, label='Октябрь' )
ax.bar( x, apr, width, label='Апрель' )
ax.bar( x+width, year,width,color="maroon", label='Остальные месяцы')

ax.set_xticks(x)
ax.set_xticklabels(Dates)
ax.legend()
plt.title("Траты категории автосервис")
#plt.show()
#----------------------------
df = pd.read_excel('data1.xlsx',sheet_name='по месяцам', skiprows=[1])
Dates = df['категория']
index = []
for i in range(len(Dates)):
    if(str(Dates[i])[5:7]=='04' or str(Dates[i])[5:7]=='10'):
        index.append(i)
proper_m = df.iloc[np.r_[index]]
auto = proper_m['автосервис']
m_2_m = []
for i in range(len(index)):
    m_2_m.append(auto[index[i]])
auto = df.drop(np.r_[index])['автосервис']
av_ye19 = mean(auto[0:11])
av_ye20 = mean(auto[12:23])
av_ye21 = mean(auto[24:35])
av_ye22 = mean(auto[36:])
Dates=['2019','2020','2021','2022']
year=[av_ye19, av_ye20, av_ye21, av_ye22]
oct=[m_2_m[0], m_2_m[2], m_2_m[4], m_2_m[6]]
apr = [m_2_m[1], m_2_m[3], m_2_m[5], m_2_m[7]]
width=0.3
x = np.arange(len(Dates))

fig, ax = plt.subplots(figsize=(10, 10))

ax.bar( x-width, oct, width, label='Октябрь' )
ax.bar( x, apr, width, label='Апрель' )
ax.bar( x+width, year,width,color="maroon", label='Остальные месяцы')

ax.set_xticks(x)
ax.set_xticklabels(Dates)
ax.legend()
plt.title("Траты категории автосервис")
plt.show()