#!/usr/bin/env python
import numpy as np
import pylab as P

mu, sigma = 200, 25
x = mu + sigma*P.randn(10000)


# create a new data-set
x = mu + sigma*P.randn(1000,3)

n, bins, patches = P.hist(x, 10, normed=1, histtype='bar',
                            color=['crimson', 'burlywood', 'chartreuse'],
                            label=['Crimson', 'Burlywood', 'Chartreuse'])
P.legend()

#
# ... or we can stack the data
#
P.figure()
n, bins, patches = P.hist(x, 10, normed=1, histtype='bar', stacked=True)
P.show()
