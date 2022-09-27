from statistics import median
import pandas as pd
pd.options.mode.chained_assignment = None 
import matplotlib.pyplot as plt
    
df = pd.read_csv('train.csv')

#print(df.info(verbose=True))

columnsAsNumericValues = df.select_dtypes(include=['number']).columns # this line of code is to print the columns that has numeric values

columsAsNonNumericValues = df.select_dtypes(exclude=['number']).columns # this line of code represents the columns that has not numeric values

# now that we know better our dataset, and the information inside it, its time to know 
# the columns that have missing values or null values, since it makes it difficult to
# make our analysis and see the data visualization wrong. 

#print(df[columsAsNonNumericValues].info()) # this line it shows the column and the missing values inside these columns
#if we print it, we can see that we dont have any missing values inside these columns

missing_values = df.isna().sum() #this line it show us the columns and there missing values
print(missing_values[:10])

#ISNA -> it detects the missing values

missing_by_row = df.isna().sum(axis='columns')
missing_by_row.hist(bins=50)
#plt.show()

# Altough we can drop the colums or the rows, to make the dataset
# much smaller and work better with the dataset, it's not (depending on your project's goals)
# the mos efficient way in our project to clear out data
# since that, we are going to fill the missing data
# with statics

df_copy = df.copy()
filliningNumericValues = df_copy[columnsAsNumericValues].median()
df_copy[columnsAsNumericValues] = df_copy[columnsAsNumericValues].fillna(filliningNumericValues)
#print(filliningNumericValues)

fillingNonNumericValues = df_copy[columsAsNonNumericValues].describe().loc['top']
df_copy[columsAsNonNumericValues] = df_copy[columsAsNonNumericValues].fillna(fillingNonNumericValues)
#print(fillingNonNumericValues)

describingLife_sqColumn = df_copy['life_sq'].describe()


grafica = df_copy['life_sq'].hist(bins=100)
#df_copy.boxplot(column=['life_sq'])
#plt.show()

df['ecology'].value_counts().plot(kind = 'bar')
#plt.show()

#Unnecessary data
newDataFrame = df_copy.drop(columns=['id']).drop_duplicates()

#INCONSISTENT data
upperCaseData = newDataFrame['sub_area'].str.upper()
inconsistentData = upperCaseData.value_counts(dropna=False)
#print(upperCaseData)

# Cleaning data types
newDataFrame['timestamp_dt'] = pd.to_datetime(newDataFrame['timestamp'], format='%d/%m/%Y')
newDataFrame['day'] = newDataFrame['timestamp_dt'].dt.day
newDataFrame['month'] = newDataFrame['timestamp_dt'].dt.month
newDataFrame['year'] = newDataFrame['timestamp_dt'].dt.year
newDataFrame['weekday'] = newDataFrame['timestamp_dt'].dt.weekday

#print(newDataFrame[['timestamp_dt', 'day', 'month', 'year', 'weekday']].head())

missing_values = newDataFrame.isna().sum() #this line it show us the columns and there missing values
print(missing_values[:10])

new = newDataFrame.isna().sum(axis='columns')
new.hist(bins=50)
plt.show()
#print(newDataFrame.info(verbose=True))