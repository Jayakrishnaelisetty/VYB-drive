#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json

def load_nutrition_data(excel_path):
    df = pd.read_excel(excel_path, sheet_name="Nutrition source")
    df = df[["food_name", "energy_kcal", "protein_g", "carb_g", "fat_g", "fibre_g"]].dropna(subset=["food_name"])
    nutrition_dict = {
        row["food_name"].strip().lower(): {
            "calories": row["energy_kcal"],
            "protein": row["protein_g"],
            "carbs": row["carb_g"],
            "fat": row["fat_g"],
            "fiber": row["fibre_g"]
        }
        for _, row in df.iterrows()
    }
    return nutrition_dict

def load_unit_mappings(excel_path):
    df = pd.read_excel(excel_path, sheet_name="Unit of measurements")
    unit_dict = {
        "piece": 1,  # Customize per item
        "katori_150ml": 150,
        "glass_250ml": 250,
        "teaspoon_5ml": 5,
        "tablespoon_15ml": 15
    }
    return unit_dict

def extract_grams(value):
    if isinstance(value, str) and value.strip().lower().endswith("g"):
        return int(value.strip().lower().replace("g", "").strip())
    return None

def load_food_categories(excel_path):
    df = pd.read_excel(excel_path, sheet_name="Food categories")
    df["Weight_g"] = df["Weight Cat"].apply(extract_grams)
    df = df.dropna(subset=["Weight_g"])
    food_cat_dict = {
        row["Food category name"].strip().lower(): int(row["Weight_g"])
        for _, row in df.iterrows()
    }
    return food_cat_dict

def save_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    path = "Assignment Inputs.xlsx"  # Ensure this file is in the same directory
    nutrition = load_nutrition_data(path)
    units = load_unit_mappings(path)
    food_cats = load_food_categories(path)

    save_json(nutrition, "nutrition_data.json")
    save_json(units, "unit_conversion.json")
    save_json(food_cats, "food_categories.json")

    print("✅ Data extracted and saved as JSON.")


# In[ ]:




