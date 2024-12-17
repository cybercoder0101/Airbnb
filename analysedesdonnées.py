#importation des bibliotheques necessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
import statsmodels.api as sm


#réglage afon d'afficher toutes les lignes
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#chemin du fichier
filepath = 'C:/Users/ibrah/Documents/My projects/Airbnb/pythonProject/AB_NYC_2019.csv'

#lecture du fichier
data = pd.read_csv(filepath)

d=data.columns[data.isna().any()].tolist()
print(d)

#visualisation des lignes avec des valeurs nulles
print(data.isnull().sum())
#suppression des lignes a valeurs vides
data = data.dropna()

#verification de la suppression des lignes
print(data.isnull().sum())

#visionnage de l'appartement le plus populaire
print(data.loc[data['number_of_reviews'].idxmax()])


#le moins populaire
print(data.loc[data['number_of_reviews'].idxmin()])


#l'appartement le moins cher
print(data.loc[data['price'].idxmin()])


#l'appartement le moins cher
print(data.loc[data['price'].idxmax()])


#visionnage des zones les plus populaires
neighborhood_counts = data.groupby("name")["number_of_reviews"].count().reset_index()
top_neighborhoods = neighborhood_counts.sort_values("number_of_reviews", ascending=False)
print(top_neighborhoods.head(5))

"""""""""
#les zones populaires
print(data.groupby("neighbourhood_group"))
print(data.groupby("neighbourhood_group")["name"].count())
"""""""""
test =data[["name","number_of_reviews"]]
#print(data.head(5))
print(test.head(5))

#les zones les plus populaires selon le quartier
plt.scatter(data['neighbourhood_group'], data['number_of_reviews'])
plt.xlabel('neighbourhood_group')
plt.ylabel('Number of Reviews')
plt.show()

#les prix selon les zones
plt.scatter(data['neighbourhood_group'], data['price'])
plt.xlabel('quartiers')
plt.ylabel('prix')
plt.show()

#les types de maisons les plus louées
plt.scatter(data['room_type'], data['calculated_host_listings_count'])
plt.xlabel('room type')
plt.ylabel('host listing')
plt.show()

#les maisons les plus louees selon le prix
plt.scatter(data['room_type'], data['price'])
plt.xlabel('room type')
plt.ylabel('price')
plt.show()

ax=sns.barplot(x='neighbourhood_group', y='price', hue='room_type', data=data, order=data.neighbourhood_group.value_counts().index)
plt.show()

#
print(data.loc[data['calculated_host_listings_count'].idxmax()])

#
d=data.columns[data.isna().any()].tolist()
print(data.columns.values)
print(d)

#
nbgroupe= data['neighbourhood_group'].value_counts()
# Création un graphique en barres pour les locations par arrondissement
fig, ax = plt.subplots()
ax.bar(nbgroupe.index, nbgroupe.values)
ax.set_xlabel('Quartiers')
ax.set_ylabel('Nombre de locations')
ax.set_title('Nombre de locations Airbnb par quartiers ')
plt.show()

#prix moyens des type de chambres par quartier
print(data.groupby(['neighbourhood_group','room_type'])['price'].mean().sort_values(ascending=False).reset_index())

top_reviewed_listings=data.nlargest(10,'number_of_reviews')
print(top_reviewed_listings.loc[:,].head(2))
plt.boxplot(data['number_of_reviews'],data['neighbourhood_group'])
plt.ylabel('nb_of_reviews')
plt.xlabel('name')
plt.show()
