# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:41:38 2019

@author: kelly
"""

import numpy as np
import pandas as pd 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt 
import seaborn as sns

my_data = pd.read_csv('earthquake.csv')
my_data = my_data.drop(["id", "date",'time','mw','ms','mb','country','city','area','direction','dist','xm','md'], axis=1)

scaler=StandardScaler()
my_data[['lat', 'long', 'depth']]=scaler.fit_transform(my_data[['lat', 'long', 'depth']])
my_data['richter'] = np.where(my_data['richter']>1,1,0)
sns.pairplot(my_data, vars=['lat', 'long', 'depth'],hue='richter')
plt.show()

#PCA
pca = PCA(n_components=3)
my_principalComponents = pca.fit_transform(my_data[['lat', 'long', 'depth']])
my_principalDf = pd.DataFrame(data = my_principalComponents
             , columns = ['principal_component_1', 'principal_component_2', 'principal_component_3'])
my_finalDf = pd.concat([my_principalDf, my_data[['richter']]], axis = 1)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal_Component_1', fontsize = 15)
ax.set_ylabel('Principal_Component_2', fontsize = 15)
ax.set_title('2_component_PCA', fontsize = 20)
targets = [0,1]
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = my_finalDf['richter'] == target
    ax.scatter(my_finalDf.loc[indicesToKeep, 'principal_component_1']
               , my_finalDf.loc[indicesToKeep, 'principal_component_2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

my_explained_variance=pca.explained_variance_ratio_
with plt.style.context('seaborn-white'):
    plt.figure(figsize=(6, 4))
    plt.bar(range(3), my_explained_variance, alpha=0.5, align='center',
            label='individual_explained_variance')
    plt.ylabel('Explained_variance_ratio')
    plt.xlabel('Principal_components')
    plt.legend(loc='best')
    plt.tight_layout()

#plot principal components
pca = PCA(n_components=2)
my_principalComponents = pca.fit_transform(my_data[['lat', 'long', 'depth']])
my_principalDf = pd.DataFrame(data = my_principalComponents
             , columns = ['principal_component_1', 'principal_component_2'])
finalDf = pd.concat([my_principalDf, my_data[['richter']]], axis = 1)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1) 
ax.set_xlabel('Principal_Component_1', fontsize = 15)
ax.set_ylabel('Principal_Component_2', fontsize = 15)
ax.set_title('2_component_PCA', fontsize = 20)
targets = [0,1]
colors = ['r', 'g']
for target, color in zip(targets,colors):
    indicesToKeep = my_finalDf['richter'] == target
    ax.scatter(my_finalDf.loc[indicesToKeep, 'principal_component_1']
               , my_finalDf.loc[indicesToKeep, 'principal_component_2']
               , c = color
               , s = 50)
ax.legend(targets)
ax.grid()

print(my_explained_variance)
print(pca.components_)

#3D plot
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(my_data[['lat', 'long', 'depth']])
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=my_data['richter'],
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])
plt.show()