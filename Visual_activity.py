#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#read in data
df = pd.read_csv('gas prices.csv')

"""
#plot line graph
plt.figure(figsize=(8,5))
plt.plot(df.Year, df.Japan, 'r.-', label="Japan")
plt.plot(df.Year, df.UK, 'b.-',label ="UK")
plt.plot(df.Year, df.France, 'g.-',label ="France")
plt.xticks(df.Year[::3])
plt.title('Gas Prices', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.ylabel('USD/Gallon', fontdict={'fontweight':'bold', 'fontsize': 15})
plt.xlabel('Year', fontdict={'fontweight':'bold', 'fontsize': 15})
plt.legend()
plt.savefig('Gas Prices_Plot_graph.png', dpi=300)
plt.show()
"""

"""
#plot Histogram
bins = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8]
plt.hist(df.USA, bins=bins, color='#ffaf8c', edgecolor='black',label='USA')
plt.hist(df.Italy,bins=bins,color='#70B793',edgecolor='black', label='Italy')
plt.title('USA & Italy Gas Prices', fontdict={'fontweight':'bold', 'fontsize': 18})
plt.xlabel('Prices', fontdict={'fontweight':'bold', 'fontsize': 15})
plt.ylabel('Total', fontdict={'fontweight':'bold', 'fontsize': 13})
plt.legend()
plt.savefig('Gas Prices_Histogram.png', dpi=300)
plt.show()
"""

"""
#plot pie chart
plt.title('Pie Chart for Gas Prices')
labels = ['less than $2/gal', 'greater than $2/gal']
colors = ['#ffaf8c','#70B793']
usa = df.loc[(df.USA >= 0) & (df.USA < 2)].count()[0]
mex = df.loc[(df.Mexico >= 0) & (df.Mexico > 2)].count()[0]
plt.pie([usa,mex], labels=labels,colors=colors, autopct='%.2f%%', shadow=True, startangle=90,explode=(0,0.1))
plt.savefig('Gas Prices_PieChart_graph.png', dpi=300)
plt.show()
"""
"""
#plot scatter graph
plt.style.use('seaborn')
usa = df['USA']
france = df['France']
mex = df['Mexico']
can = df['Canada']
plt.scatter(usa,mex,c=can, edgecolor='black',linewidth=2,alpha=0.75,cmap='summer')
cbar = plt.colorbar()
cbar.set_label('Gas Prices')
plt.title('Gas Prices Scatter Plots',fontdict={'fontweight':'bold', 'fontsize': 13})
plt.tight_layout()
plt.savefig('Gas Prices_ScatterPlot_graph.png', dpi=300)
plt.show()
"""
"""
#plot 3-D or map
"""