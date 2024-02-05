# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:36:04 2024

@author: Mihlali
"""

import pandas as pd

file = pd.read_csv("movie_dataset.csv")

print(file.describe())

file = pd.read_csv('movie_dataset.csv')

missing_values = file.isnull().sum()

print(missing_values[missing_values > 0])

file.columns = file.columns.str.strip().str.replace(' ' , '_')

file['Revenue_(Millions)'].fillna(file['Revenue_(Millions)'].mean(), inplace=True)
file['Metascore'].fillna(file['Metascore'].mean(), inplace=True)

file.dropna(inplace=True)

file.reset_index(drop=True, inplace=True)

print(file.head())


import matplotlib.pyplot as plt

x = file['Title']
y = file['Rating']
plt.scatter(x, y)

plt.xlabel('Title')
plt.ylabel('Ratings')
plt.title('Highest in Rating')

#plt.show()

Revenue = file['Revenue_(Millions)']
r_sum = sum(Revenue)
r_size = len(Revenue)

r_avrg = r_sum/r_size

#print(r_avrg)

filtered_file = file[(file['Year'] >= 2015) & (file['Year'] <= 2017)]

average_revenue = filtered_file['Revenue_(Millions)'].mean()

print(f"Average revenue of movies from 2015 to 2017 is: {average_revenue:.2f}")

movies_2016_count = file[file['Year'] == 2016].shape[0]
print(f"movies released in 2016 are: {movies_2016_count}")


nolan_movies_count = file[file['Director'] == 'Christopher Nolan'].shape[0]
print(f"Movies directed by Christopher Nolan is: {nolan_movies_count}")


hrm_count = file[file['Rating'] >= 8.0].shape[0]
print(f"Movies with a rating of at least 8.0 is: {hrm_count}")


nmm_rating = file[file['Director'] == 'Christopher Nolan']['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is: {nmm_rating:.2f}")


avrg_rating_by_year = file.groupby('Year')['Rating'].mean()
highest_avrg_rating = avrg_rating_by_year.idxmax()
print(f"The yea with the highest avrg rating is: {highest_avrg_rating}")




movies_2006 = file[file['Year'] == 2006].shape[0]
movies_2016 = file[file['Year'] == 2016].shape[0]
movies_increase = 2016 - 2006
print(f"The number of movies percentage increase between 2006 and 2016 is: {movies_increase}")


movies_2006_file = file[file['Year'] == 2006]
movies_2016_file = file[file['Year'] == 2016]

movies_2006 = movies_2006_file.shape[0]
movies_2016 = movies_2016_file.shape[0]

percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")


all_actors = file['Actors'].str.split(', ').explode()
most_common_actor = all_actors.mode().iloc[0]
print(f"The most common actor in all the movies is: {most_common_actor}")


all_genres = file['Genre'].str.split(', ').explode()
unique_genres_count = all_genres.nunique()
print(f"Number of unique genres in the dataset is: {unique_genres_count}")


numerical_features = file.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numerical_features.corr()

print("Correlation Matrix:")
print(correlation_matrix)

