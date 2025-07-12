def get_bot_response(question):
    q = question.lower()

    # 🔴 Reject clearly unrelated topics
    unrelated = ["president", "politics", "cricket", "india", "weather", "modi", "bjp", "rahul"]
    if any(word in q for word in unrelated):
        return "💡 I'm a beauty advisor bot! Please ask something about skincare, makeup, or haircare 😊"

    # 🟢 Sunscreen Queries
    if "sunscreen" in q or "spf" in q:
        if "50" in q:
            return ("🧴 The most recommended SPF 50+ sunscreen is **La Roche-Posay Anthelios** – "
                    "it's lightweight, dermatologist-approved, and a favorite last year!")
        elif "30" in q:
            return ("🧴 **Neutrogena Ultra Sheer SPF 30** is a great everyday option with a matte finish.")
        elif any(spf in q for spf in ["40", "45", "55", "60"]):
            return ("🧴 Try **Bioderma Photoderm Max SPF 60** or **RE' EQUIL Ultra Matte SPF 50+** – popular among Indian users.")
        else:
            return "🧴 Please mention the SPF level you are looking for (30+, 50+, etc.)."

    # 🟢 Moisturizer Queries
    if "moisturizer" in q or "moisturiser" in q:
        if "dry" in q:
            return ("💧 **CeraVe Moisturizing Cream** is excellent for dry skin with ceramides + hyaluronic acid.")
        elif "gel" in q or "oily" in q:
            return ("🌿 **Neutrogena Hydro Boost Gel** is perfect for oily skin and under ₹500!")
        elif "fragrance free" in q:
            return ("🚫 Try **Cetaphil Moisturizing Lotion** – it's gentle and fragrance-free.")
        elif "best" in q:
            return "💖 Try **CeraVe**, **Cetaphil**, or **The Ordinary** based on your skin type!"
        else:
            return "💧 Please mention your skin type or need (gel, dry skin, etc.)."

    # 🟢 Face Wash / Cleanser
    if "face wash" in q or "cleanser" in q:
        if "acne" in q:
            return "🧼 Use **Salicylic Acid Face Wash** from **Plum**, **Minimalist**, or **Neutrogena** – great for acne-prone skin."
        elif "sensitive" in q:
            return "🌸 **Cetaphil Gentle Cleanser** is perfect for sensitive skin."
        else:
            return "🧼 For general use, **Simple Refreshing Face Wash** is a safe and gentle option."

    # 🟢 Makeup Keywords
    if "foundation" in q:
        return "🎨 Try **Maybelline Fit Me**, **L'Oréal True Match**, or **MAC Studio Fix** – good coverage and variety."

    if "lipstick" in q:
        return "💄 **Maybelline SuperStay**, **MAC Retro Matte**, or **Sugar Matte Attack** are popular picks!"

    if "mascara" in q:
        return "👁️ **L'Oreal Lash Paradise** and **Maybelline Colossal Waterproof** are user favorites."

    if "concealer" in q:
        return "🎯 Try **Maybelline Age Rewind** for dark circles or **LA Girl Pro HD** for full coverage."

    # 🟢 Haircare
    if "shampoo" in q:
        if "dandruff" in q:
            return "🧴 Try **Head & Shoulders Neem** or **Sebamed Anti-Dandruff** for best results."
        elif "color" in q:
            return "🎨 Use **L'Oreal Color Protect Shampoo** or **Biolage Colorlast** for colored hair."

    if "serum" in q and "vitamin c" in q:
        return "🍊 **Minimalist 10% Vitamin C** and **Plum 15% Vitamin C** are highly rated for brightening."

    # 🟢 Fragrance
    if "perfume" in q or "fragrance" in q:
        return "🌸 Try **YSL Black Opium**, **Carolina Herrera**, or **Titan Skinn**. Under ₹1500? Try **Layer'r Wottagirl!**"

    # 🟢 Special: All-about-beauty question
    if "what all things" in q or "topics" in q:
        return ("📚 I can help you with skincare, makeup, haircare, body care, fragrance, and trending products. "
                "Ask me about moisturizers, sunscreens, hair oils, lipsticks, face masks, and more!")

    # 🔁 Fallback for beauty-related
    beauty_keywords = ["cream", "spf", "makeup", "serum", "skin", "hair", "lip", "face", "oil", "mask"]
    if any(word in q for word in beauty_keywords):
        return "✨ Try asking something more specific, like: _'Best moisturizer for dry skin'_ or _'Top budget sunscreen'_"

    # ❌ Final fallback
    return "🧴 I'm here to help with skincare and beauty tips. Please ask something in that area! 💖"
