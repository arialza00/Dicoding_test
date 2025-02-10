import sys
import os
import nbformat
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the Dicoding folder to the system path
dicoding_dir = os.path.abspath('Dicoding')
sys.path.insert(0, dicoding_dir)

import notebook
# Import the module from the dashboard folder
notebook = notebook

import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import streamlit as st
import pydeck as pdk
import pandas as pd
from diskcache import Cache
from babel.numbers import format_currency

# Initialize DiskCache
cache = Cache(directory='cache')

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
col5, col6, col7 = st.columns(3)
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

with col1:
    # Cache the data loading and preprocessing step
    # @st.cache_data(show_spinner=False)
    def load_data():
        df = notebook.orders_region_df2.loc[:, ('customer_lat', 'customer_lng', 'price')]  # Load only necessary columns

        # Optimize data types
        df['customer_lat'] = df['customer_lat'].astype('float32')
        df['customer_lng'] = df['customer_lng'].astype('float32')
        df['price'] = df['price'].astype('float32')
        
        return df
    st.subheader("# Order Distribution by Region")
    orders_region_df2 = load_data()

    # Sample the data to reduce the number of rows (e.g., take 0.5% of the data)
    orders_region_df_sample = orders_region_df2.sample(frac=0.005, random_state=42)

    # Check if the required columns exist in the DataFrame
    if not all(col in orders_region_df2.columns for col in ['customer_lat', 'customer_lng', 'price']):
        st.error("The DataFrame 'orders_region_df2' is missing required columns ('customer_lat', 'customer_lng', or 'price').")
    else:
        # Create the map bar chart with the sampled data
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=-13.338848,
                longitude=-47.442158,
                zoom=3,
                pitch=50,
            ),
            layers=[
                pdk.Layer(
                    'ColumnLayer',
                    data=orders_region_df_sample,
                    get_position=['customer_lng', 'customer_lat'],
                    get_elevation='price',
                    get_fill_color='[price * 10, 140, 190, 255]',  # Change color based on price
                    radius=20000,
                    elevation_scale=100,
                    elevation_range=[0, 10000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        ))
with col2:

    st.subheader("Highest Revenue by Product Category")
    data_df=notebook.product_seller_grouped_df
    fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(20, 30))

    sns.barplot(x="product_category_name_english", y="price", data=data_df.sort_values(by="price", ascending=False).head(10), palette=colors, ax=axs)
    
    axs.set_ylabel("price", fontsize=30)
    axs.yaxis.set_label_position("right")
    axs.yaxis.tick_right()
    axs.set_title("Best Performing Product", loc="center", fontsize=50)
    axs.tick_params(axis='y', labelsize=35)
    axs.tick_params(axis='x', labelsize=30, rotation=90)

    st.pyplot(fig)

with col3:
    st.subheader("Monthly Revenue")
    data = notebook.monthly_price_sum

    # Plotting the line chart
    st.line_chart(data.set_index('order_month')['total_price'])

with col4:
    data = notebook.category_monthly_price_sum
    category_monthly_price_sum = pd.DataFrame(data)

    # Set the title of the Streamlit app
    st.subheader('Monthly Total Price Line Chart by Product Category')

    # Convert 'order_month' to string format "yyyy-mm"
    category_monthly_price_sum['order_month'] = category_monthly_price_sum['order_month'].dt.strftime('%Y-%m')

    # Add a select box for product category
    product_category = st.selectbox('Select Product Category', category_monthly_price_sum['product_category_name_english'].unique())

    # Filter the DataFrame based on the selected product category
    filtered_data = category_monthly_price_sum[category_monthly_price_sum['product_category_name_english'] == product_category]

    # Create a line chart
    st.line_chart(filtered_data.set_index('order_month')[['total_price']])                                  
    
with col5:
    rfm_df = notebook.rfm_df
    avg_recency = round(rfm_df.recency.mean(), 1)
    st.metric("Average Recency (days)", value=avg_recency)
 
with col6:
    avg_frequency = round(rfm_df.frequency.mean(), 2)
    st.metric("Average Frequency", value=avg_frequency)
 
with col7:
    avg_frequency = format_currency(rfm_df.monetary.mean(), "$", locale='en_US') 
    st.metric("Average Monetary", value=avg_frequency)
 
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(35, 15))
colors = ["#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9", "#90CAF9"]
 
sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("customer_id", fontsize=30)
ax[0].set_title("By Recency (days)", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=30)
ax[0].tick_params(axis='x', labelsize=35, rotation=90)
 
sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("customer_id", fontsize=30)
ax[1].set_title("By Frequency", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=30)
ax[1].tick_params(axis='x', labelsize=35, rotation=90)
 
sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel("customer_id", fontsize=30)
ax[2].set_title("By Monetary", loc="center", fontsize=50)
ax[2].tick_params(axis='y', labelsize=30)
ax[2].tick_params(axis='x', labelsize=35, rotation=90)
 
st.pyplot(fig)