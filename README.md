# VYB-drive
# Nutrition Estimation Pipeline for Indian Dishes

This project involves building a nutrition estimation pipeline for Indian dishes. The goal of this pipeline is to extract the ingredient list, standardize quantities, map ingredients to a nutrition database, and calculate the nutrition values based on serving sizes. This pipeline will help estimate the nutritional content of Indian dishes with the accuracy of household measurements.

## Steps Involved

1. **Ingredient List Extraction**: 
   - Extract ingredients from recipe descriptions.
   
2. **Quantity Standardization**:
   - Standardize quantities from various units (e.g., teaspoons, tablespoons, cups) to grams for accurate nutrition calculation.

3. **Ingredient Mapping to Nutrition Database**:
   - Map the ingredients to a nutrition database to get the nutrient profile of each ingredient.

4. **Quantity Conversion**:
   - Convert the quantities to grams based on common conversion tables and factors for Indian household measurements.

5. **Nutrition Calculation**:
   - Calculate the total nutritional content of the dish based on the extracted ingredients and their quantities.

6. **Food Type Classification**:
   - Classify the dish into a category (e.g., vegetarian, vegan, non-vegetarian) to adjust the nutritional considerations accordingly.

7. **Serving Size Extrapolation**:
   - Estimate the serving size based on the ingredients and dish composition.

8. **Failure Handling**:
   - Implement error handling for cases where an ingredient cannot be mapped or quantities are incorrect.

## Requirements

- Python 3.x
- pandas
- numpy
- requests (for API calls to nutrition databases)
- BeautifulSoup (for web scraping recipe data)
- scikit-learn (for any potential machine learning models)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nutrition-estimation-pipeline.git
   cd nutrition-estimation-pipeline
