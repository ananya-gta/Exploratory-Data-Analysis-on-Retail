# -*- coding: utf-8 -*-
"""Task #3- Exploratory Data Analysis- Retail by Ananya Gupta

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g70LA3zIW8-6jIgps7Yx7rFeliJuxPkq

# **Ananya Gupta**

### *Dataset: SampleSuperstore.csv* (https://bit.ly/3i4rbWl) 

## **EXPLORATORY DATA ANALYSIS - RETAIL**

Hey everyone! This is an EDA project analyzing SampleSuperStore data set and visualizing it. The objective of this project is to analyze and identify trends and patterns in the current retail sales and identify which sector of the market is under loss and which sector is making huge profits. Every sector offers discounts on sales, but, do they collect profits as needed on the discounts they offer? Which shipment class boosts the sales of which category?

This video will guide you through the process of retrieving answers to all these questions.

Let us get started!

### **Loading Packages**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""### **Reading the Dataset**

 **Print the first 5 rows**
"""

df=pd.read_csv("SampleSuperstore.csv")
df.head()

"""### **Full Summary of the Dataframe**"""

df.info()

"""### **Data Types of each column in the Dataset**"""

df.dtypes

"""### **Finding all the column names inside the Dataset**"""

df.columns

"""### **Shape of the Dataset**"""

df.shape

"""### **Count distinct observations over requested axis**"""

df.nunique()

"""### **Statistical details of the Dataset**"""

df.describe()

"""#**DATA PREPARATION & CLEANING**

### **Total number of null values in a Dataset**
"""

df.isnull().sum()

"""### **Removing Duplicates**

**Sometimes you get a messy dataset. You may have to deal with duplicates, which will skew your analysis. In python, pandas offer function drop_duplicates(), which drops the repeated or duplicate records.**
"""

df.duplicated().sum()

df.drop_duplicates()

"""### **Find the correlation and covariance of dataset**"""

df.corr()

df.cov()

"""### **Find the Series containing counts of unique values**"""

df.value_counts()

"""### **Removing Country and Postal Codes feature**"""

col=['Postal Code', 'Country']
df1=df.drop(columns=col,axis=1)
df1.head()

"""# **UNDERSTANDING THE DATASET**

### **What are the Region wise Sales value ?**
"""

df.groupby("Region").Sales.sum()

"""### **What are the Top 10 selling products ?**"""

df.groupby("Sub-Category").Sales.sum().sort_values(ascending=False).head()

"""### **What are the Top 5 Profitable Products ?**"""

df.groupby("Sub-Category").Profit.sum().sort_values(ascending=False).head(5)

"""### **What are the different ship mode ?**"""

diff_ship_mode=df['Ship Mode'].unique()
for x in diff_ship_mode:
    print(x)

"""### **What are the category wise profit?**"""

df.groupby("Category").Profit.sum()

"""### **What is the maximum sale ?**"""

df.Sales.max()

"""### **What is the minimum sale ?**"""

df.Sales.min()

"""## **PROPER VISUALISATION OF THE DATASET**
**Let’s analyze patterns in our cleaned data**



"""

segment= df.Segment.value_counts().reset_index()
segment.columns=("Segments", "Total")
segment

plt.figure(figsize=(19,6))
plt.title('SUB-CATEGORIES VS REGION')
sns.countplot(x=df['Sub-Category'], hue= df['Region'])
plt.xticks()
plt.show()

"""# **Sales vs Quantity**"""

plt.figure(figsize= (19,9))
plt.title('SALES VS QUANTITY')
sns.barplot(x=df['Quantity'], y= df["Sales"], data= df, hue='Ship Mode')
plt.show()

"""# **Sales vs Discount**
### **Let us see how Sales are affected if discounts are offered.**
"""

plt.figure(figsize= (9,5))
plt.title('SALES VS DISCOUNT')
sns.histplot(x=df['Discount'], y= df["Sales"], data= df, hue='Ship Mode')
plt.show()

"""### **It is evident from the above graph that discounts attract more sales.**

# **Sales vs States**
"""

highest_sales=df[df['Sales']>5000]
plt.figure(figsize=(10,9))
sns.barplot(x=highest_sales['Sales'], y=highest_sales['State'], data=df)
plt.show()

"""### **We clearly see that the highest sales have been made in Florida.**

# **Profits vs Discount**
### **Let’s see whether profits have been triggered if discounts have been redeemed.**
"""

plt.figure(figsize = (10,4))
plt.title('PROFIT VS DISCOUNT')
sns.lineplot('Discount', 'Profit', data = df, color = 'r', label= 'Discount')
plt.legend()
plt.show()

"""**Yes, we see clearly, the more discounts have been offered and redeemed, the lesser profits the segments have achieved. Products with no discounts show high range of profits but as the discount range increases, we only see more and more loss with hardly any profit.**
### **Let us see if this is the case with other segments**
"""

plt.figure(figsize= (18,7))
plt.title('PROFIT VS SUB-CATEGORY')
sns.barplot(x=df['Sub-Category'], y= df["Profit"], data= df, hue="Region")
plt.xticks(rotation=90)
plt.show()

"""### **We see that more losses have been incurred by the Binders industry mainly in the Central region and Machines industries in South and Central region and Tables industry in South, East and Central region.**

## **Now,**
"""

plt.figure(figsize= (10,5))
plt.title('SALES VS CATEGORY')
sns.barplot(x=df['Sales'], y= df["Category"], data= df, hue='Region')
plt.show()

"""### **More Sales have been incurred by the technology category, then Furniture and office supplies. Mostly sales have been made from the West and East regions**"""

plt.figure(figsize= (10,5))
plt.title('PROFIT VS CATEGORY')
sns.barplot(x=df['Profit'], y= df["Category"], data= df, hue='Region')
plt.show()

"""### **The furniture category incurrs more losses than losses in the technology and Office Supplies category. Since, Sales also vary from low to high in this category so is are profits.**"""

fig, ax = plt.subplots(figsize = (19 , 8))
ax.scatter(df["Sales"] , df["Profit"], c= 'g' )
ax.set_title('SALES vs PROFIT')
ax.set_xlabel('Sales')
ax.set_ylabel('Profit')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
plt.show()

"""### **We have now witnessed from the above graphs that the Sales to Profit ratio is same in every category, no matter how they are clubbed.**

# **CONCLUSION:**

### **Recommended Solutions/ Key Insights:**

***Same day shipment if receives more discounts can trigger sales/profits. Discounts should be based on the Sales and should not increase a particular range otherwise unnecessary disounts with low sales can witness huge losses Binders and Machines industry should be focused upon more so as to strengthen these weakened industry areas. Office Supplies and the Furniture industries do not seem to boom in the Central Region.***

# ***Thank You!***
"""
