def recommend_products(df, category, max_price, min_rating):
    filtered = df[
        (df["primary_category"] == category) &
        (df["price_usd"] <= max_price) &
        (df["rating"] >= min_rating)
    ]
    return filtered.sort_values(by=["rating", "reviews"], ascending=[False, False]).head(10)
