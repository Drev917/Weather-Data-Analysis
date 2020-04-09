# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:13:36 2020

@author: Drewb
"""

import numpy as np

weatherData = np.genfromtxt('weatherData.csv', delimiter=',') #imports weatherData as np array

print('Max daily sales: \n' + str('${:,.2f}'.format(weatherData.max(axis=0)[2]))) #max sales
print('Minimum daily sales: \n' + str('${:,.2f}'.format(weatherData.min(axis=0)[2]))) #min sales
print('Mean daily sales: \n' + str('${:,.2f}'.format(weatherData.mean(axis=0)[2]))) #mean sales

days_500k = np.sum(weatherData[:,2] > 500000) #sums sales days over $500k in revenue
temp_500k = np.multiply(weatherData[:,2] > 500000, weatherData[:,0]) #temperature above this value is recorded
avgTemp_500k = np.sum(temp_500k)/days_500k #avg temp for days with at least $500k in sales revenue

print('\nAverage temperature for days with more than $500,000 in sales:\n' + str('{:.2f}'.format(avgTemp_500k)))

avgTempAll = weatherData.mean(axis=0)[0]


if (avgTemp_500k > avgTempAll):
	print('\nThe average temperature on days where sales exceeded $500,000 is > than the average temperature for all days in the dataset\n')
else:
	print('\nThe average temperature on days where sales exceeded $500,000 is < than the average temperature for all days in the dataset\n')

import pandas as pd

df = pd.DataFrame(weatherData, columns = ['Temperature','Rain','Sales'])

rain_temp = df[df['Rain']==1]['Temperature'].mean() #mean temperatures on rainy days
rain_sales = df[df['Rain']==1]['Sales'].mean() #mean sales on rainy days
nonrain_temp = df[df['Rain']==0]['Temperature'].mean() #mean temperatures on non-rainy days
nonrain_sales = df[df['Rain']==0]['Sales'].mean() #mean sales on non-rainy days

print('Average temperature for rainy days:\n' + str('{:.2f}'.format(rain_temp)))
print('Average sales for rainy days: \n' + str('${:,.2f}'.format(rain_sales)))
print('Average temperature for non-rainy days:\n' + str('{:.2f}'.format(nonrain_temp)))
print('Average sales for non-rainy days: \n' + str('${:,.2f}\n'.format(nonrain_sales)))

import seaborn as sns

#sns.pairplot(df)

df = df.sort_values(by ='Sales')
print(df.tail())

import matplotlib.pyplot as plt

#linear relationship between temperature and sales
#non-rainy days plotted in yellow and rainy days plotted in black
plt.scatter(df['Temperature'],df['Sales'],c = df['Rain']) 
plt.ylabel('Sales')
plt.xlabel('Temperature')
plt.title('Relationship between temperature and sales')


from scipy import stats

slope, intercept, r_value, p_value, std_err = stats.linregress(df['Temperature'], df['Sales']) #obtain stats from regression line

#printing stats
print('\nSlope: ' + str(slope))
print('y-intercept: ' + str(intercept))
print('r value: ' + str(r_value))
print('p value: ' + str(p_value))
print('standard error : ' + str(std_err))
print('r-squared: %f' % r_value**2)

x = df['Temperature']
y = df['Sales']

#visualizing line of best fit relationship with scatter plot
plt.plot(x, y, 'o', label='original data')
plt.plot(x, intercept + slope * x, 'r', label='fitted line')
plt.legend()
plt.show()






