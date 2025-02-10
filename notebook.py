# %% [markdown]
# # **Import Dataset**
# 

# %%
import setup


# %% [markdown]
# ## **Customer Dataset**
# 

# %%

# Specify the path to your CSV file
import pandas as pd

file_path = "data/customers_dataset.csv"

# Read the CSV file into a pandas DataFrame
customers_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['customer_id','customer_unique_id',
                                    'customer_zip_code_prefix',
                                    'customer_city',
                                    'customer_state'],
                            dtype={ 'customer_id' : 'str',
                                    'customer_unique_id' : 'str',
                                    'customer_zip_code_prefix' : 'int64',
                                    'customer_city' : 'str',
                                    'customer_state' : 'str'})

# print the DataFrame
customers_df.head()




# %% [markdown]
# ## **Geolocation Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/geolocation_dataset.csv"

# Read the CSV file into a pandas DataFrame
geolocation_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['geolocation_zip_code_prefix',
                                     'geolocation_lat',
                                     'geolocation_lng',
                                     'geolocation_city',
                                     'geolocation_state'],
                            dtype={ 'geolocation_zip_code_prefix' : 'int64',
                                    'geolocation_lat' : 'float64',
                                    'geolocation_lng' : 'float64',
                                    'geolocation_city' : 'str',
                                    'geolocation_state' : 'str'})

# print the DataFrame
geolocation_df.head()




# %% [markdown]
# ## **Order Items Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/order_items_dataset.csv"

# Read the CSV file into a pandas DataFrame
order_items_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['order_id',
                                     'order_item_id',
                                     'product_id',
                                     'seller_id',
                                     'shipping_limit_date',
                                     'price',
                                     'freight_value'],
                            dtype={  'order_id' : 'str',
                                     'order_item_id' : 'int64',
                                     'product_id' : 'str',
                                     'seller_id' : 'str',
                                     'shipping_limit_date' : 'str',
                                     'price' : 'float64',
                                     'freight_value' : 'float64'})

order_items_df['total_value'] = order_items_df['price'] + order_items_df['freight_value']
# print the DataFrame
order_items_df.head()



# %% [markdown]
# ## **Order Payments Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/order_payments_dataset.csv"

# Read the CSV file into a pandas DataFrame
order_payments_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['order_id',
                                     'payment_sequential',
                                     'payment_type',
                                     'payment_installments',
                                     'payment_value'],
                            dtype={ 'order_id' : 'str',
                                    'payment_sequential' : 'int',
                                    'payment_type' : 'category',
                                    'payment_installments' : 'int',
                                    'payment_value' : 'float64'})

# print the DataFrame
order_payments_df.head()



# %% [markdown]
# ## **Order Review Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/order_reviews_dataset.csv"

# Read the CSV file into a pandas DataFrame
order_reviews_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['review_id',
                                     'order_id',
                                     'review_score',
                                     'review_comment_title',
                                     'review_comment_message',
                                     'review_creation_date'],
                            dtype={  'review_id' : 'str',
                                     'order_id' : 'str',
                                     'review_score' : 'int64',
                                     'review_comment_title' : 'str',
                                     'review_comment_message' : 'str',
                                     'review_creation_date' : 'str'})

# print the DataFrame
order_reviews_df.head()



# %% [markdown]
# ## **Order Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/orders_dataset.csv"

# Read the CSV file into a pandas DataFrame
orders_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['order_id',
                                     'customer_id',
                                     'order_status',
                                     'order_purchase_timestamp',
                                     'order_approved_at',
                                     'order_delivered_carrier_date',
                                     'order_delivered_customer_date',
                                     'order_estimated_delivery_date'],
                            dtype={  'order_id' : 'str',
                                     'customer_id' : 'str',
                                     'order_status' : 'str',
                                     'order_purchase_timestamp' : 'str',
                                     'order_approved_at' : 'str',
                                     'order_delivered_carrier_date' : 'str',
                                     'order_delivered_customer_date' : 'str',
                                     'order_estimated_delivery_date' : 'str'})

# print the DataFrame
orders_df.head()


# %% [markdown]
# ## **Product Category Name Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/product_category_name_translation.csv"

# Read the CSV file into a pandas DataFrame
product_category_name_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['product_category_name' ,
                                     'product_category_name_english'],
                            dtype={  'product_category_name'  : 'str',
                                     'product_category_name_english'  : 'str'})

# print the DataFrame
product_category_name_df.head()



# %% [markdown]
# ## **Product Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/products_dataset.csv"

# Read the CSV file into a pandas DataFrame
products_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['product_id',
                                     'product_category_name',
                                     'product_name_lenght',
                                     'product_description_lenght',
                                     'product_photos_qty',
                                     'product_weight_g',
                                     'product_length_cm',
                                     'product_height_cm',
                                     'product_width_cm'],
                            dtype={  'product_id'  : 'str',
                                     'product_category_name'  : 'str',
                                     'product_name_lenght'  : 'int64',
                                     'product_description_lenght'  : 'int64',
                                     'product_photos_qty'  : 'int64',
                                     'product_weight_g'  : 'int64',
                                     'product_length_cm'  : 'int64',
                                     'product_height_cm'  : 'int64',
                                     'product_width_cm'  : 'int64'})

# print the DataFrame
# print(products_df.head())


# %% [markdown]
# ## **Seller Dataset**
# 

# %%

# Specify the path to your CSV file
file_path = "data/sellers_dataset.csv"

# Read the CSV file into a pandas DataFrame
sellers_df = pd.read_csv(file_path, delimiter=",", 
                            usecols=['seller_id',
                                     'seller_zip_code_prefix',
                                     'seller_city',
                                     'seller_state'],
                            dtype={  'seller_id'  : 'str',
                                     'seller_zip_code_prefix'  : 'int64',
                                     'seller_city'  : 'str',
                                     'seller_state'  : 'str'})

# print the DataFrame
sellers_df.head()

# %% [markdown]
# # **Deskripsi Dataset**
# 

# %% [markdown]
# ## **Info Dataset**
# 

# %%
customers_df.info(memory_usage='deep')

geolocation_df.info(memory_usage='deep')

order_items_df.info(memory_usage='deep')

order_payments_df.info(memory_usage='deep')

order_reviews_df.info(memory_usage='deep')

orders_df.info(memory_usage='deep')

product_category_name_df.info(memory_usage='deep')

products_df.info(memory_usage='deep')

sellers_df.info(memory_usage='deep')

# %% [markdown]
# ## **Kolom Dataset**
# 

# %%
print("customers_df columns:")
print(customers_df.columns)
print("\ngeolocation_df columns:")
print(geolocation_df.columns)
print("\norder_items_df columns:")
print(order_items_df.columns)
print("\norder_payments_df columns:")
print(order_payments_df.columns)
print("\norder_reviews_df columns:")
print(order_reviews_df.columns)
print("\norder_df columns:")
print(orders_df.columns)
print("\nproducts_df columns:")
print(products_df.columns)
print("\nsellers_df columns:")
print(sellers_df.columns)

# %% [markdown]
# ## **Info Dataset**
# 

# %%
orders_customers_df = pd.merge(order_items_df, products_df, on='product_id', how='left')
orders_customers_df2 = pd.merge(orders_customers_df, product_category_name_df, on='product_category_name', how='left')
orders_customers_df2 = orders_customers_df2[["order_id", "product_category_name_english", "seller_id", "price"]]
orders_customers_df2.groupby('product_category_name_english')['order_id'].count()


# %%
order_status_counts = orders_df.groupby('order_status')['order_id'].count()
print(order_status_counts)

# %% [markdown]
# # **Analisis Dataset**
# 

# %% [markdown]
# ## **Produk dari Vendor Mana yang Memberikan Revenue Tertinggi?**

# %%
# Merge orders and customers dataframes
orders_customers_df = pd.merge(order_items_df, products_df, on='product_id', how='left')
orders_customers_df2 = pd.merge(orders_customers_df, product_category_name_df, on='product_category_name', how='left')
orders_customers_df2 = orders_customers_df2[["order_id", "product_category_name_english", "seller_id", "price"]]
# print the merged DataFrame
#print(orders_customers_df2.head())

# prompt: pandas sum column and show as column

# Calculate the sum of the 'price' column and create a new column
orders_customers_df2['price_sum'] = orders_customers_df2.groupby('product_category_name_english')['price'].transform('sum')

# print the DataFrame with the new 'price_sum' column
orders_customers_df2[["product_category_name_english", "seller_id", "price_sum"]]

# prompt: pandas group by 2 column

# Group by two columns and calculate the sum of 'price'
grouped_df = orders_customers_df2.groupby(["product_category_name_english", "seller_id"])["price"].sum().reset_index()

# print the grouped DataFrame
# print(grouped_df.head())


product_seller_grouped_df = grouped_df.sort_values(by="price", ascending=False)
product_seller_grouped_df.head(10)

# %%
grouped_df

# %%


# prompt: pandas group by 2 column

# Group by two columns and calculate the sum of 'price'
grouped_df = orders_customers_df2.groupby(["product_category_name_english", "seller_id"])["price"].sum().reset_index()

# print the grouped DataFrame
# print(grouped_df.head())


product_seller_grouped_df = grouped_df.sort_values(by="price", ascending=False)
product_seller_grouped_df.head(10)

# %%
grouped_df = grouped_df.sort_values(by=['seller_id', 'price'], ascending=[True, False])
grouped_df

# %%
grouped_df = grouped_df.sort_values(by="price", ascending=False)

# Display the first row for each seller_id based on the sorted price
result_df = grouped_df.groupby('seller_id').first().reset_index()
# Display the result
print(result_df)

# %%
result_df = result_df.sort_values(by='price', ascending=False)
result_df.head(10)

# %%
result_df["price"] = result_df["price"] / 1000
result_df['price'] = result_df['price'].map("${:,.0f}K".format)

# %% [markdown]
# ## **Wilayah Mana yang Memiliki Nilai Order Tertinggi?**

# %%
customers_region_df = pd.merge(customers_df, geolocation_df, left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')
customers_region_df = customers_region_df[["customer_id", "geolocation_lat", "geolocation_lng", "customer_city", "customer_state"]]
customers_region_df = customers_region_df.rename(columns={
    'geolocation_lat': 'customer_lat',
    'geolocation_lng': 'customer_lng'
})
customers_region_df.drop_duplicates(subset='customer_id', keep='first', inplace=True)


# %%
# prompt: pandas join 2 table
# Merge orders and customers dataframes
orders_region_df = pd.merge(orders_df, customers_region_df, on='customer_id', how='inner')
orders_region_df2 = pd.merge(orders_region_df, order_items_df, on='order_id', how='inner')

# print the merged DataFrame
orders_region_df2 = orders_region_df2[["customer_city","customer_state","customer_lat", "customer_lng","price"]]

# Group by two columns and calculate the sum of 'price'
grouped_df = orders_region_df2.groupby(["customer_city","customer_state","customer_lat", "customer_lng"])["price"].sum().reset_index()

# print the grouped DataFrame
grouped_df.head()


# %% [markdown]
# ## **Nilai pesanan setiap bulan**

# %%
orders_recap_df = pd.merge(orders_df, order_payments_df, on='order_id', how='inner')
orders_recap_df.columns

# %%
orders_recap_df1 = pd.merge(orders_recap_df, order_items_df, on='order_id', how='left')
orders_recap_df1.columns

# %%
orders_recap_df2 = pd.merge(orders_recap_df1, orders_customers_df2[['order_id','product_category_name_english']], on='order_id', how='left')
orders_recap_df2.columns

# %%
orders_recap_df2[['order_id', 'customer_id', 'seller_id', 'product_category_name_english', 'order_item_id',
                  'payment_sequential', 'payment_type', 'payment_installments', 
                 'price', 'freight_value', 'payment_value', 'total_value', 'order_status', 
                 'order_purchase_timestamp','order_approved_at', 'order_delivered_carrier_date',
                 'order_delivered_customer_date', 'order_estimated_delivery_date']]

# %%
orders_recap_df2['product_category_name_english'] = orders_recap_df2['product_category_name_english'].replace('home_appliances_2', 'home_appliances')

# %%
orders_recap_df2['product_category_name_english'] = orders_recap_df2['product_category_name_english'].replace('home_comfort_2', 'home_comfort')

# %%
orders_recap_df2['product_category_name_english'].unique()

# %%
# Convert 'order_purchase_timestamp' to datetime
orders_recap_df2['order_purchase_timestamp'] = pd.to_datetime(orders_recap_df2['order_purchase_timestamp'])

# Extract the month and year from 'order_purchase_timestamp'
orders_recap_df2['order_month'] = orders_recap_df2['order_purchase_timestamp'].dt.to_period('M')

# Group by 'order_month' and calculate the sum of 'price'
monthly_price_sum = orders_recap_df2.groupby('order_month')['price'].sum().reset_index()

# Rename the columns for better understanding
monthly_price_sum.columns = ['order_month', 'total_price']

# Display the result
monthly_price_sum

# %% [markdown]
# ## **Nilai pesanan berdasarkan bulan dan produk**

# %%
# Group by 'product_category_name_english' and 'order_month' and calculate the sum of 'price'
category_monthly_price_sum = orders_recap_df2.groupby(['product_category_name_english', 'order_month'])['price'].sum().reset_index()

# Rename the columns for better understanding
category_monthly_price_sum.columns = ['product_category_name_english', 'order_month', 'total_price']

# Display the result
category_monthly_price_sum

# %% [markdown]
# ## **Jumlah pesanan setiap bulan**

# %%
# Group by 'order_month' and count the number of 'order_id'
monthly_order_count = orders_recap_df2.groupby('order_month')['order_id'].count().reset_index()

# Rename the columns for better understanding
monthly_order_count.columns = ['order_month', 'order_count']

# Display the result
monthly_order_count

# %% [markdown]
# ## **Nilai pesanan setiap bulan berdasarkan seller**

# %%
# Group by 'product_category_name_english' and 'order_month' and calculate the sum of 'price'
seller_monthly_price_sum = orders_recap_df2.groupby(['seller_id', 'order_month'])['price'].sum().reset_index()

# Rename the columns for better understanding
seller_monthly_price_sum.columns = ['seller_id', 'order_month', 'total_price']

# Display the result
seller_monthly_price_sum

# %% [markdown]
# ## **Penggabungan Dataset**

# %%
seller_region_df = pd.merge(sellers_df, geolocation_df, left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix', how='left')
seller_region_df = seller_region_df[["seller_id", "geolocation_lat", "geolocation_lng", "seller_city", "seller_state"]]
seller_region_df = seller_region_df.rename(columns={
    'geolocation_lat': 'seller_lat',
    'geolocation_lng': 'seller_lng'
})
seller_region_df.drop_duplicates(subset='seller_id', keep='first', inplace=True)

# %%
orders_recap_df2 = pd.merge(orders_recap_df2, customers_region_df, on='customer_id', how='inner')
orders_recap_df2

# %%
orders_recap_df2 = pd.merge(orders_recap_df2, seller_region_df, on='seller_id', how='inner')
orders_recap_df2.columns

# %%
orders_recap_df2[['order_id', 'customer_id', 'product_id', 'seller_id', 'customer_lat',
       'customer_lng', 'customer_city', 'customer_state', 
       'seller_lat', 'seller_lng', 'seller_city', 'seller_state',
       'product_category_name_english', 'payment_sequential', 'payment_type', 'payment_installments',
       'order_item_id', 'order_status', 'price', 'freight_value', 'total_value', 'payment_value', 'shipping_limit_date', 
       'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date']]


#  orders_recap_df2[['order_id', 'customer_id', 'product_id', 'seller_id', 'customer_lat',
#         'customer_lng', 'customer_city', 'customer_state', 
#         'seller_lat', 'seller_lng', 'seller_city', 'seller_state',
#         'product_category_name_english', 'payment_sequential', 'payment_type', 'payment_installments',
#        'order_item_id', 'order_status', 'price', 'freight_value', 'total_value', 'payment_value', 'shipping_limit_date', 
#        'order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date',
#         'order_delivered_customer_date', 'order_estimated_delivery_date']].to_csv('all_dataset.csv', index=False)

# %%
import datetime as dt

# Define the current date for recency calculation
current_date = dt.datetime(2018, 9, 1)

# Convert 'order_purchase_timestamp' to datetime if not already done
orders_recap_df2['order_purchase_timestamp'] = pd.to_datetime(orders_recap_df2['order_purchase_timestamp'])

# Calculate Recency, Frequency, and Monetary values for each customer
rfm_df = orders_recap_df2.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (current_date - x.max()).days,
    'order_id': 'count',
    'total_value': 'sum'
}).reset_index()

# Rename the columns for better understanding
rfm_df.columns = ['customer_id', 'recency', 'frequency', 'monetary']

# Display the result
rfm_df.head()


