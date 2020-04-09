# Weather Data Analysis and Visualization

I used NumPy and Pandas libraries to analyze and sort overall weather correlation to sales revenue.

The dataset had no headers, so I added headers `Temperature`, `Precipitation`, and `Sales`.

I also looked at relationships between the weather as a binary indicator (precipitation or dry) and sales vs weather given the attached csv file.

I used Seaborn to visualize the data commonality for easy dissemination.

![ScreenShot](https://github.com/Drev917/Weather_Data/blob/master/WeatherPlot.JPG)

I wanted to look more closely at the linear relationship between temperature and sales in the data set. I started by sorting values by `Sales` looking at the `Temperature` column. 

By importing Matplotlib, I was able to show the overall ascending relations ship between `Temperature` values and `Sales` values. To enhance the graph, I plotted the no-precipitation values yellow, and the precipitation weather values black.

![ScreenShot](https://github.com/Drev917/Weather_Data/blob/master/TempvSales.JPG)

I also wanted to look at the relationship from a linear regression model. First I imported the stats tools from SciPy, a scientific computing library for python. This shed light on overall statistical functions that are helpful to know. I was then able to plot a line of best fit over the existing DataFrame that I created to fully visualize the linear relationship between the two indexes.

![ScreenShot](https://github.com/Drev917/Weather_Data/blob/master/FittedLine.JPG)


#### Quick Observations:

- Standard distributions of sales and temperatures can be seen creating appealing data visualizations
- A clearly visible linear relationship between sales and temperatures can also be observed
- The cluster of sales vs no-precipitation days is positionally higher than the cluster of sales vs precipitation days which is logical
