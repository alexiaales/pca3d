# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 12:42:18 2020

@author: Alexia
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import matplotlib.pyplot as plt
import pylab as pzt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as plt

g1 = input("""
                  
  ====================================================================
  =   Please name the file you want to work on :                     =
  ==================================================================== 
  
 --> Type the name:""")

#df = pd.read_excel(io='protein_significance.xlsx')

def readfiles(g1):
    # check for the names
    m=g1
    if m[-3:]=='lsx':
        name = pd.read_excel(io=m)
        name=name.fillna(0)
        namenp=np.array(name)
    if m[-3:]=='txt':
    #open all files and make them in a form that is readable
        name=pd.read_csv(m,sep='\t')
        namenp=np.array(name)
        
    return(name,namenp)
########################################################################
print('.')
print('.')
print('The file you chose has the following columns:')
print('.')
print('.')
m=readfiles(g1)[0].columns.values
counter=0

for x in m :  
    print(counter,x)
    counter+=1  
#########################################################################
m=readfiles(g1)[0]

keepfrom = input(""" --> Type the columns you want to keep from:""")
keepuntil= input(""" --> Type the columns you want to keep until(+1):""")

fr=int(keepfrom)
un=int(keepuntil)

i=m.iloc[:,fr:un]

m=i.columns.values

print('you have kept the following columns:')
counter=0
for x in m :  
    print(counter,x)
    counter+=1  


    

dropfrom = input(""" --> Type the columns you want to drop from:""")
dropuntil= input(""" --> Type the columns you want to drop until(+1):""")

dfr=int(dropfrom)
dun=int(dropuntil)

ix=i.drop(i.columns[dfr:dun], axis=1)

m=ix.columns.values

print('you have kept the following columns:')



count=0
for x in m:
    count+=1
    print(count, x)
    


numberList = []

print("\n")
for i in m:
    print("what is the index of",i, ":")
    item = int(input())
    numberList.append(item)
print("User List is ", numberList)
##############################################################################
#                           MANUALLY                                         #
##############################################################################



ls=numberList
lst=pd.DataFrame(numberList) 
ini=ix.T

sns.set_style("white")
 
 

# Run The PCA
pca = PCA(n_components=3)
pca.fit(ini)

 
# Store results of PCA in a data frame
result=pd.DataFrame(pca.transform(ini), columns=['PCA%i' % i for i in range(3)], index=ini.index)

# Plot initialisation
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(result['PCA0'], result['PCA1'], result['PCA2'],alpha=0.8,c=ls, cmap="tab10", s=60)
 
# make simple, bare axis lines through space:
xAxisLine = ((min(result['PCA0']), max(result['PCA0'])), (0, 0), (0,0))
ax.plot(xAxisLine[0], xAxisLine[1], xAxisLine[2], 'r')
yAxisLine = ((0, 0), (min(result['PCA1']), max(result['PCA1'])), (0,0))
ax.plot(yAxisLine[0], yAxisLine[1], yAxisLine[2], 'r')
zAxisLine = ((0, 0), (0,0), (min(result['PCA2']), max(result['PCA2'])))
ax.plot(zAxisLine[0], zAxisLine[1], zAxisLine[2], 'r')
 
# label the axes
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")
ax.set_title("PCA on the data set")
plt.show()

