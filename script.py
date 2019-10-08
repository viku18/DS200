import matplotlib.pyplot as plt 
import pandas as pd

data = pd.read_excel('datafile.xls')
ds=data.loc[:, ['StateName','General','SC']]
df=ds['StateName'].unique().tolist()
x1=[]
y1=[]
#print(df)
for x in df:
	df1=ds.loc[ds['StateName']==x]
	x2=sum(df1['General'])
	x3=sum(df1['SC'])
	x1.append(x2)
	y1.append(x3)
#print(x1)
plt.figure()

plt.barh(df,x1,align='edge')
plt.xlabel('General')
plt.ylabel('State')
plt.title('General Population in states')

plt.figure()
plt.scatter(x1,y1)
plt.xlabel('General')
plt.ylabel('SC')
plt.title('Statewise comparison between General and SC population')

plt.figure()
ax = data.loc[:, ['General', 'SC', 'ST']].boxplot()
ax.set_title('Category wise Distribution of population across districts')
plt.show()