import pandas as pd
import seaborn as sns
df = pd.read_csv('titanic.csv')
print(df)
print(df.corr())
sns.heatmap(df.corr(), annot=True, linewidths=0.5)
#l = df.shape[0]
#print(df.shape[0]-df["Embarked"].dropna().shape[0])
#print(df["Cabin"].dropna().groupby(by = "Cabin"))
#print(df["Age"].fillna(df["Age"].median()).mean())
#print(df["Fare"].apply(lambda x: x).quantile(0.75))
#pr = df[df["Sex"].apply(lambda x: True if x == "male" else False)].copy()
#print("M ",pr["Sex"].shape[0]*100/l,"F",(l-pr["Sex"].shape[0])*100/l)
#print(df["Name"].apply(lambda x: len(x.split())).quantile(0.95))
#print(df["Cabin"].value_counts().shape[0])
#def Fun(install):
 #   install = install.split(',')
  #  list = install[1].split('.')
   # return list[0]
#print((df["Name"].apply(Fun).value_counts()))





df1 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],index_col=0,header=None)
df2 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],header=None)
work2 = df1.iloc[0:,45:]
work2.transpose().to_csv('r.csv')
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,23)])
Data = np.array(df2.iloc[1:,0:1])
r = []
for el in work2['категория']:
    r.append(el)
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)],index_col=0)
for i in range(work2.shape[1]-len(r)):
    r.append('None')
work2 = work2.transpose()
work2['Data'] = Data
print(work2)
fig = []
for i in range(work2.shape[1]-2):
    N = []
    for _ in range(work2.shape[0]):
        N.append(r[i])
    work2['Category'] = N
    fig.append(px.line(work2,x = "Data",y = r[i],markers=True,color='Category'))
data = fig[0].data
for i in range(1,len(fig)-1):
    data += fig[i].data
Fig = go.Figure(data)
Fig.show()

df1 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],index_col=0,header=None)
df2 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],header=None)
work2 = df1.iloc[0:,45:]
work2.transpose().to_csv('r.csv')
work2 = pd.read_csv('r.csv')
Data = np.array(df2.iloc[1:,0:1])
r = []
for el in work2['категория']:
    for _ in range(work2.shape[1]-2):
        r.append(el)
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)],index_col=0)
work2 = work2.transpose()
work2['Data'] = Data
work2 = pd.concat([work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2,work2])
work2['Category'] = r
print(work2)
fig = px.line(work2, x="Data",y = "автосервис", markers=True,color="Category")
fig.show()

#---------------
df1 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],index_col=0,header=None)
df2 = pd.read_excel('data1.xlsx',sheet_name='по месяцам',skiprows=[1],header=None)
Data = np.array(df2.iloc[1:,0:1])
work2 = df1.iloc[0:,44:]
work2.transpose().to_csv('r.csv')
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)])
r = []
print(df2)
Names = work2['категория']
for el in Names:
    for _ in range(work2.shape[1]-1):
        r.append(el)
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)],index_col=0)
work2 = work2.transpose()
full_data = []
for el in Names:
    full_data.append(work2[el])
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
#---------------------------------
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
work2 = pd.read_csv('r.csv',usecols=[i for i in range(1,48)],index_col=0,skiprows=(1))
work2 = work2.transpose()
full_data = []
for el in Names:
    full_data.append(work2[el])
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
fig.show()
