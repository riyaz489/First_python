import pandas as pd

weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,31],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}

#pandas work on dataframe and dataframe looks like exel table
#converting dictionary to data frame
df = pd.DataFrame(weather_data)
df = pd.read_csv("SalesJan2009.csv")
print (df)

#tells dimesnion of table
rows,cols=df.shape
print (cols)

#take top 3 records
df.head(3)

#take last 3 records
df.tail(3)

#take data from row at index 1 to row at index 3 ( exclude row at index 4)
print(df[1:4])

#print columns
df.columns

#print only latitude col data
df['Latitude'] #or df.Latitude

#print only two cols data
df[['Product','Latitude']]

#print max value of price
df['Price'].max()

#print only dates where price are max
print(df['Transaction_date'][df['Price'] == df['Price'].max()])

#print whole row where price are max
print(df[df['Price'] == df['Price'].max()])

#provide mean, std ,min and other values of table
print(df.describe())

#to do indexing using product column
df.set_index('Product',inplace=True)
#inplace true means, it will reflect the changes in the actual table

#by indexing with product, now we can search data with products as index
df.loc['Product1']

#to reset the index
df.reset_index(inplace=True)



### movies assignment ##############
df = pd.read_csv('movies_metadata.csv')

# first solution
print('number of columns :\n ', df.columns, '\n')

# second solution
print('data frame information : \n', df.info(), '\n')

# third solution
print('third movie information :\n ', df.iloc[2], '\n')

# fourth solution
print('number of rows and columns:', df.shape, '\n')

# fifth solution
print('movie details: \n', df[df['title'] == 'Grumpier Old Men'], '\n')

# sixth solution
print('fifth movie \n:', df.iloc[4], '\n')

# seventh solution
# getting subset of columns
new_df = df[['id', 'original_language', 'release_date', 'revenue', 'runtime', 'vote_count']]
# getting subset of rows
print('smaller daa frame:\n', new_df.head(3))

# eight solution
print('top 10 rows:\n', df.head(10), '\n')

# ninth solution
print('sorted df:\n', df.sort_values('release_date'), '\n')

# tenth solution
print('\n', df[df['release_date'] > '1995-01-01'])

# eleventh solution
print('sorted df:\n', df.sort_values('runtime', ascending=False), '\n')

# twelfth solution
print('revenue more than 2 million and spent less than 1 million:\n', df[(df['revenue'] > 20000000) &
                                                                         (df['budget'] < 10000000)], '\n')

# thirteenth solution
run_time = df['runtime']
print('longest runtime: ', run_time.max(), '\n')
print('shortest runtime: ', run_time.min(), '\n')

# fourteenth solution
print(df['vote_count'].quantile(0.70), '\n')

# fifteenth solution
new_df = df[['title', 'runtime']]
print('movies whose runtime lie between 30 and 360', new_df[(new_df['runtime'] >= 30) & (new_df['runtime'] <= 360)])

# sixteenth solution
new_df = df[['title', 'vote_count']]
n = 100
print('list of title with specified votes', new_df[new_df['vote_count'] >= n])
