#!/usr/bin/env python
# coding: utf-8

# # ZOMATO DATA ANALYSIS
# 
# I got the very interesting zomato data for the city Pune, we have lots of features telling lots of stories about the food habits in pune.
# I am curious to know the answers of some of the questions like...
# 
# 
# <b>
#     
# Ques-1 Which are the best rated restaurants in Pune?
# 
# Ques-2 Which is the best rated location for food in Pune?
# 
# Ques-3 What is most liked cuisine in Pune?
# 
# Ques-4 Which are the cheap but best restaurants in Pune?
# 
# Ques-5 Which restaurant serves the best "BIRYANI" in Pune?
# 
# Ques-6 Baner being my favourite place in Pune, Which are the best restaurants in Baner?
#     
# </b>
# 
# and so many other questions i have...
#     
# 
# 
# 
# Lets explore this data and try to find the answers of these questions...
# 

# In[4]:


#importing libraries
import numpy as np 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt




# In[5]:


#removing warnings
import warnings
warnings.filterwarnings('ignore')


# In[6]:


#loading the csv file
df= pd.read_csv("zomato_outlet_final (11).csv")
df.head(10)


# In[7]:


df.columns


# In[8]:


#removing the unncessary column "link"
df=df.drop(['link','Unnamed: 9'],axis=1)
df.head()

#deleting row axis=0
#deleting column axis=1


# In[9]:


#we have 5433 restaurats in our data, including small tapris, medium size restaurants,
#Bakeries, Dessert Parlours, Cake Shops, Bars, Big Restaurants, Casual Dinings etc.
df.shape


# In[10]:


df.info()


# We have some null values in some colums, we will handle them step by step

# In[11]:


# lets find the duplicates in the data

df.duplicated().sum()


# In[12]:


#we have 250 rows which are duplicates, lets remove the duplicate values

df=df.drop_duplicates()
df.shape

#after removing duplicate rows, we got 5183 restaurants in our dataset


# # Exploratory Data Analysis
# 
# Lets do the EDA on Zomato to understand the data in depth.
# 
# We gonna do Univariate Data Analysis and Bivariate Data Analysis
# 
# 

# # FEATURE-1(dine_rating)

# In[25]:


#lets plot the histogram
plt.hist(df['dine_rating'])
plt.xlabel("dine_rating")#
plt.ylabel("count of restaurants")



# In[26]:


plt.hist(df.delivery_rating)
plt.xlabel("delivery_rating")
plt.ylabel("count of restaurants")


# # OBSERVATIONS
# 
# 1.More than 500 restaurnants have 0 ratings
# 
# 2.Most of the restaurants got rating between 3.5 to 4 and thats a good news for zomato.
# 
# 3.There are no restaurants which got 1 as a rating in our data.

# In[27]:


#probability density function

sns.FacetGrid(df, size=5)    .map(sns.distplot, "dine_rating") 
plt.show()


# In[28]:


sns.FacetGrid(df, height=3)    .map(sns.distplot, "delivery_rating")
plt.show()


# In[29]:


#bar plot
dine=df['dine_rating'].value_counts()
plt.figure(figsize=(15,10))

plt.xlabel("dine_rating")
plt.ylabel("Count")
sns.barplot(x=dine.index,y=dine.values)


# In[30]:


dine2=df['delivery_rating'].value_counts()
plt.figure(figsize=(15,10))
print(dine2)

plt.xlabel("delivery_rating")
plt.ylabel("Count")
sns.barplot(x=dine.index,y=dine.values)


# # Observation
# 
# 1. Most of the restaurants have ordered 3.9 rating.
# 
# 
# 2. There are lots of restaurants which got 0 ratings.
# 
# 

# In[31]:


#box plot

sns.boxplot(df['dine_rating'])


# # Observation
# 
# 1. 25% of the dine ratings on zomato is less than 3.
# 
# 
# 2. 50% of the dine ratings on zomato is approximately less tha 3.8.
# 
# 
# 3. 75% of the dine rating on zomato is less than 4.
# 
# 
# 4. 50% of the restaurants have rating between 3 to 4 and thats a good news for a company like Zomato.

# # Feature-2(Rest_type- Restaurant_type)

# In[32]:


print(len(df['rest_type'].unique()))


# There are 67 types of restaurant types in pune

# In[33]:


#lets count the number of each Type
df['rest_type'].value_counts()


# # Which Types of restaurants are leaders in pune?

# In[34]:


rest_type_values=df['rest_type'].value_counts()[:10]
print(rest_type_values)


# In[35]:


plt.figure(figsize=(15,8))

sns.barplot(rest_type_values,rest_type_values.index)


# We can see, there are mostly quick bites restaurants, followed by casual dining and bakery

# In[36]:


#pie chart


labels=rest_type_values.index
size=rest_type_values.values 
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
       
plt.axis('equal')


# # Observation
# 
# 1. 39% of the restaurants in pune are Quick bites.
# 
# 
# 2. 24.2% of the restaurants in pune are Casual dining.
# 
# 
# 3. 8.7 % of the restaurants in pune are Bakeries.

# # Feature-3(Cuisines)

# In[37]:


# we can see that a restaurant can have multiple cuisine
df['cuisine']


# # Lets see what all cuisine Pune serves to us...

# In[38]:


#NUMBER OF CUISINE IN PUNE
cuisine=[]
for i in df['cuisine']:
    for j in i.split(","):
        if j not in cuisine:
            cuisine.append(j)
print(cuisine)
print(len(cuisine))

#there are 92 total cuisine in all the restaurant in pune


# We can see there are lots of cuisines in pune, some of them are are not cuisines like Coffee, Mithai etc but in data we have it like that
# 

# # Total number of restaurants serving biryani in Pune

# In[39]:


count=0
for i in df['cuisine']:
    for j in i.split(","):
        if j =="Biryani":
            count=count+1
print(count)

#There are 566 restaurant in pune which serves biryani


# # Total number of restaurants serving North Indian Food in Pune

# In[40]:


count=0
for i in df['cuisine']:
    for j in i.split(","):
        if j =="North Indian":
            count=count+1
print(count)

#There are 2057 restaurants out of 5183 restaurants(almost 40%) which serves North Indian Food


# In[41]:


list_res=[]
d={}
for i in df["cuisine"]:
    for j in i.split(","):
        list_res.append(j)

        
for i in list_res:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
        
for w in sorted(d, key=d.get, reverse=True):
    print(w, d[w])

        
        


# # Feature-4(loc-location where the restaurant is situated)

# In[42]:


total_locations=df['loc'].value_counts()
top_total_locations=df['loc'].value_counts()[:10]
print(top_total_locations)

places=top_total_locations.index

#these are the location with the maximum number of restaurants in pune


# In[43]:


sns.barplot(top_total_locations,places)


# # Observation
# 
# Kothrud has the maximum number of restaurants followed by wakad and viman nagar

# In[44]:


labels = top_total_locations.index
sizes =top_total_locations.values 

plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True)
plt.axis('equal')


# # Observation
# 
# 1. Kothrud covers 13.8% of top 10 locations in pune.
# 
# 
# 2. Viman Nagar and Baner covers almost 11.5% of the top 10 locations in pune

# # FEATURE-5(delivery_rating)

# In[45]:


deliver=df['delivery_rating'].value_counts()
deliver


# In[46]:


plt.figure(figsize=(15,8))


sns.barplot(deliver.index,deliver)


# # Observation
# 
# 1.Most of the restaurant gets 3.9 delievery rating
# 
# 2.There are very few restaurants who get less than 2.5 rating.
# 
# 

# In[47]:


#lets plot the histogram
plt.hist(df['delivery_rating'])
plt.xlabel("delivery_rating")
plt.ylabel("count of restaurants")


# In[48]:


#box plot

sns.boxplot(df['delivery_rating'])


# # Observation
# 
# 1. 25% of the delivery rating is less than 3.5
# 
# 
# 2. 50% of the delivery rating is less than 2.9
# 
# 
# 3. 75% of the delivery rating is less than 4.2
# 
# 
# 4. We can clearly observe that 50% of the delivery rating lies between 3.6 to 4.1 and thats a good news for Zomato.

# In[49]:


df.columns


# # Feature-5 Cost (RS)
# 
# We are assuming that this is the average cost of 2 people.
# 

# In[50]:


cost=df['Cost (RS)'].value_counts()
cost


# In[51]:


plt.figure(figsize=(15,8))


sns.barplot(cost.index,cost)


# # Observation
# 
# 1. There are 759 restaurants which that cost Rs300 for 2 people.
# 
# 
# 2. There are 624 restaurants which that cost Rs400 for 2 people.

# In[52]:


#lets plot the histogram
plt.hist(df['Cost (RS)'])



# In[53]:


sns.boxplot(df['Cost (RS)'])


# # Observation
# 
# 1. 25% of the restaurants cost less than 300 rupees for 2 people.
# 
# 
# 2. 50% of the restaurants cost less than 400 rupees for 2 people.
# 
# 
# 3. 75% of the restaurants cost less than 850 rupees for 2 people.
# 
# 
# 4. Obviously there are some outliers restaurants which cost more than 2000 , some even cost 5000.
# 

# In[54]:


#scatter plot
                     #x axis         #Y axis
sns.scatterplot(df["Cost (RS)"],df["delivery_rating"])


# # Observation
# 
# 1. There are obviously more ratings for the food which cost less than Rs500.
# 
# 
# 2. There are also restaurants which cost almost 2000 but has delivery_rating less than 3.

# In[55]:


sns.scatterplot(df["Cost (RS)"],df["dine_rating"])


# # Observation
# 
# 1. Obviosly there are more ratings for the food which cost less than 1000.
# 
# 
# 2. There are restaurants which does have rating irrespective of cost.
# 
# 
# 3. As cost increases, rating moves to 3 to 5, it means people are rating high to costly restaurnts.

# # Let's do some more Questions
# 
# Q1. Create a dataframe for all the restaurants
#     which belong to KOTHRUD?
#     
# Q2. Which are the highly rated restaurants in BANER?
# 
# Q3. Which are restaurtants which got 0 rating 
#     the city PUNE?
#     
# Q4. Return the location in pune with the best restaurants?
# 
# Q5. Plot the bar chart of top 10 locations rating wise in 
#     pune?
# 
# 

# # Dataframe for all the restaurants which belong to KOTHRUD?

# In[63]:


#q-1  Create a dataframe for all the restaurants which belong to KOTHRUD?
df_kothrud=df[(df['loc']=='Kothrud') | (df['loc']=='Baner')]
df_kothrud


# In[64]:


df_kothrud.shape


# In[65]:


df_fc=df[(df['loc']=='Fc Road') & (df['dine_rating']>4) ]
df_fc


# # HOW MANY RESTAURANTS IN KOTHRUD HAVE MORE THAN 4.2 RATING?
# 
# 

# In[42]:


df_kothrud[df_kothrud['delivery_rating']>4.2]


# # TOP RATED RESTAURANTS IN BANER

# In[43]:


df_baner=df[df['loc']=='Baner']
df_baner


# In[44]:


df_baner_top=df_baner[df_baner["dine_rating"]>4.2]
df_baner_top


# In[45]:


print((df_baner_top['rest_name'].unique()))
#there are duplicate restaurants"


# we can see that some restaurants names are almost same but they are repeating.
# 

# In[46]:


#lets clean the strings
baner_top_rest=[]
for i in df_baner_top['rest_name'].unique():
    i=i.strip()
    baner_top_rest.append(i)


# In[47]:


baner_top_rest
#still there are duplicates in this, lets remove the duplicate values


# In[48]:


#lets remove duplicates from the list
baner_rest_top=[]
for i in baner_top_rest:
    if i not in baner_rest_top:
        baner_rest_top.append(i)

print(baner_rest_top)
print(len(baner_rest_top))


# There are 17 restaurants in baner which got rating more than 4.2

# # Restaurants which got 0 rating on Zomato in Pune.

# In[49]:


df_zero_rating=df[df['dine_rating']==0]
df_zero_rating


# In[50]:


df_zero_rating.shape


# There are 566 restaurants which got 0 ratings on zomato, may be these are new restaurants or may be not very popular.

# # TOP 10 RESTAURANTS LOCATION IN PUNE

# In[3]:


df_locations=df[['dine_rating','loc']]
df_locations


# In[53]:


best_rest=df_locations[df_locations["dine_rating"]>4.2]
best_rest.head(20)


# In[2]:


best_rest.shape


# In[55]:


a=best_rest.groupby("loc")
print(a)


# In[56]:


location_wise_best_Restaurant=a.size()
print(location_wise_best_Restaurant)
print(type(location_wise_best_Restaurant))


# In[57]:


location_wise_best=location_wise_best_Restaurant.sort_values(ascending=False)
a=location_wise_best[:10]

location_wise_best


# In[58]:


#bar plot

sns.barplot(x=a,y=a.index)


# In[59]:


#total number of restaurant by location

Number_of_location=df[['loc','dine_rating']]
a=Number_of_location.groupby("loc")
rest_per_location=a.size()


# In[60]:


rest_per_location=rest_per_location.sort_values(ascending=False)
rest_per_location


# In[61]:


rest_per_location[:10]


# In[62]:


#now we want to find 
#(number of rest which got more than 4.2/ total number of rest) per location
#we are concatinating two series together
frames=[rest_per_location,location_wise_best]
data_n=pd.concat(
    frames,
    axis=1,
    join="inner",
    ignore_index=False,
    copy=True,
)


# In[63]:


data_n


# In[64]:


data_n[0]


# In[65]:


print(len(data_n[0].values))


# In[66]:


data_n['popularity_percentage']=list(map(lambda t: (t[1]/t[0])*100, zip(data_n[0], data_n[1])))


# In[67]:


data_n


# In[68]:


data_updated=data_n[data_n[0]>100]


# In[69]:


data_updated


# In[70]:


data_updated=data_updated.sort_values(by="popularity_percentage",ascending=False)


# In[71]:


data_updated


# In[72]:


sns.barplot(data_updated['popularity_percentage'],data_updated.index)


# These are the best locations in pune where find the high rated restaurants
# 
# Koregaun Park has the highest popuarity percentage out of all the locations in pune

# # THE END
# 

# In[ ]:




