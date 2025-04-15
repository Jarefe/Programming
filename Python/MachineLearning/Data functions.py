import numpy as np


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean_speed = np.mean(speed)

median_speed = np.median(speed)

standard_deviation_speed = np.std(speed)

variance_speed = np.var(speed)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

# what age are 75 % of people younger than
percentile_75_age = np.percentile(ages, 75)

# create big dataset of 250 values between 0 and 5
rand_250 = np.random.uniform(0.0,5.0,250)


import matplotlib.pyplot as plt

# histogram
plt.hist(rand_250, 5) # int = number of bars
plt.show

rand_100000 = np.random.normal(5.0, 1.0, 100000)

plt.figure()
plt.hist(rand_100000, 100)
plt.show()


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.figure()
plt.scatter(x,y)
plt.show()