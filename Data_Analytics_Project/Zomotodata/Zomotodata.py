import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("zomoto.csv")
print(data.head())



            
# print(data.tail()) 

def handleRate(value):
    value = str(value).split('/')
    value = value[0]

    return  float(value)


data['rate'] = data['rate'].apply(handleRate)
print(data.head())


print(data.info)   
# print(data.describe())


print(data.isnull().sum())

sns.countplot(x=data['listed_in(type)' ], color='yellow')
plt.xlabel('Types of Resautrant')
plt.savefig('Resautrant_types.png')
# plt.show()

# sns.countplot(x = data['online_order'])
# plt.show()

# sns.countplot(x = data['book_table'])
# plt.show()


grouped_data = data.groupby('listed_in(type)')['votes'].sum()

# print(grouped_data)
result = pd.DataFrame({'votes': grouped_data})


plt.plot(result, c='green', marker='o')

plt.xlabel("Types of Restaurant")
plt.ylabel("Votes")

plt.savefig('Votes by Restaurant')

# plt.show()


max_votes = data['votes'].max()
restuarant_with_max_votes = data.loc[data['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restuarant_with_max_votes)

sns.countplot(x=data['online_order'])

plt.savefig('max-votes.png')

# plt.show()

plt.hist(data['rate'], bins=4)
plt.title('rating Distributation')

plt.show()

couple_data = data['approx_cost(for two people)']
sns.countplot(x=couple_data)
plt.savefig('APPROX_COST_FOR_TWO_PEOPLE.png')
# plt.show()

plt.figure(figsize=(6,6))
sns.boxplot(x = 'online_order', y = 'rate', data=data)
plt.savefig('online_order.png')
plt.show()

pivot_table = data.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()