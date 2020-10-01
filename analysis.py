import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv')

subset=data[['Mortality rate, infant (per 1,000 live births)', 'GDP per capita (constant 2010 US$)', 'Country Name']]


plt.scatter(subset['GDP per capita (constant 2010 US$)'],subset['Mortality rate, infant (per 1,000 live births)'],color='red')
plt.xlabel("GDP")
plt.ylabel("Mortality Rate")
plt.show()
