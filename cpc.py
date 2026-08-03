def recommend_cpc(text):
    # Dummy logic
    if "AI" in text:
        return "G06N (Artificial Intelligence)"
    else:
        return "General Category"

# Test
print(recommend_cpc("AI based patent system"))
