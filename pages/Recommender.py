# pages/Recommender.py

import streamlit as st
import pandas as pd
from recommender import recommend_products  # ✅ logic from root file

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Recommender", page_icon="🧴")

# --- PAGE TITLE ---
st.title("🧴 DermaSelect – Product Recommender")
st.markdown("Find the best-rated beauty products that match your needs 💅")

# --- LOAD DATASET ---
df = pd.read_csv("product_info.csv")

# --- USER FILTER FORM ---
with st.form("filter_form"):
    category = st.selectbox("📦 Choose Product Category", df["primary_category"].dropna().unique())
    max_price = st.slider("💰 Max Price (USD)", 10, int(df["price_usd"].max()), 50)
    min_rating = st.slider("⭐ Minimum Rating", 1.0, 5.0, 4.0, step=0.1)
    submit = st.form_submit_button("✨ Show Recommendations")

# --- SHOW RESULTS ---
if submit:
    results = recommend_products(df, category, max_price, min_rating)
    
    if not results.empty:
        st.success("🎯 Top Products Based on Your Selection:")
        st.dataframe(results[[
            "product_name", "brand_name", "price_usd", "rating", "reviews"
        ]].reset_index(drop=True))
    else:
        st.warning("😕 No matching products found. Try different filters.")
