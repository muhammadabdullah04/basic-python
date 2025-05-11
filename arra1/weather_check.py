import numpy as np
city_1 = np.array([30, 32, 35, 34, 31, 33, 36]) 
city_2 = np.array([25, 27, 29, 28, 26, 30, 32])  
city_3 = np.array([20, 22, 21, 23, 24, 26, 25])  

temperatures = np.array([city_1, city_2, city_3])

print("Temperature Data (Cities x Days):\n", temperatures)

average_temperatures = np.mean(temperatures, axis=1)
print("\nAverage Temperature for each city:", average_temperatures)

max_temperatures = np.max(temperatures, axis=1)
min_temperatures = np.min(temperatures, axis=1)
print("\nMaximum Temperatures for each city:", max_temperatures)
print("Minimum Temperatures for each city:", min_temperatures)

overall_average = np.mean(temperatures)
print("\nOverall Average Temperature for all cities:", overall_average)

max_temp_day = np.unravel_index(np.argmax(temperatures), temperatures.shape)
min_temp_day = np.unravel_index(np.argmin(temperatures), temperatures.shape)

print("\nDay with the highest temperature (City, Day):", max_temp_day)
print("Day with the lowest temperature (City, Day):", min_temp_day)

