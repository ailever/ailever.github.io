---
title: ML, k-means clustering
date: 2020-05-30
description: ML, k-means clustering
categories:
  - education
image: https://github.com/ailever/ailever.github.io/raw/master/images/unsplash/gray_Machine_Learning.png
author_staff_member: anonym
---

## Issue
![image](https://user-images.githubusercontent.com/52376448/83324487-7d5dfc80-a2a0-11ea-817d-ab00d81a14e2.png)

<br><br><br>

## Implementation
`PYTHON CODE`
```python
import matplotlib.pyplot as plt
from mlxtend.data import three_blobs_data

X, y = three_blobs_data()
plt.scatter(X[:, 0], X[:, 1], c='black')
from mlxtend.cluster import Kmeans

km = Kmeans(k=3,
            max_iter=50,
            random_seed=1,
            print_progress=3)

km.fit(X)

print('Iterations until convergence:', km.iterations_)
print('Final centroids:\n', km.centroids_)
y_clust = km.predict(X)

plt.scatter(X[y_clust == 0, 0],
            X[y_clust == 0, 1],
            s=50,
            c='lightgreen',
            marker='s',
            label='cluster 1')

plt.scatter(X[y_clust == 1,0],
            X[y_clust == 1,1],
            s=50,
            c='orange',
            marker='o',
            label='cluster 2')

plt.scatter(X[y_clust == 2,0],
            X[y_clust == 2,1],
            s=50,
            c='lightblue',
            marker='v',
            label='cluster 3')


plt.scatter(km.centroids_[:,0],
            km.centroids_[:,1],
            s=250,
            marker='*',
            c='red',
            label='centroids')

plt.legend(loc='lower left',
           scatterpoints=1)
plt.grid()
plt.show()
```

![image](https://user-images.githubusercontent.com/56889151/83323053-315a8a00-a297-11ea-9b86-1495d9374762.png)
