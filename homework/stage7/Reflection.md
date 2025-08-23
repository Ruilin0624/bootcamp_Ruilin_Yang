I used the IQR method with a IQR multiplier of 1.5 and the Z-score method with a threshold of 3.0. 
--> The IQR method is widely used in statistics because it is simple and robust against extreme values.
--> The Z-score method works well when data is roughly normal.

Assumptions Behind My Choices:
IQR assumes that the majority of data lies within the interquartile range and that values far outside this range are unusual.
Z-score assumes the data is approximately normal, so values far from the mean (in standard deviations) are unlikely.

Observed Impacts on Results:
Removing outliers reduced the mean and standard deviation, making the dataset less skewed.
median stays relative stable, outliers mainly affected mean and variance
Winsorization smoothed extreme values without deleting data

Risks If Assumptions Are Wrong:
1. Data is heavy-tailed, removing outliers might erase important information.
2. Wrong threshold could either remove too much data or fail to catch influential points
3. Not all extreme values are errors; some may be critical signals (especially when applied to context of gold, only rare and significant event will impact its price and is a crucial notification to be noticed)  