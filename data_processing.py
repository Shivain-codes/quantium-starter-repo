import pandas as pd

# Load the three datasets
file_paths = ['./data/daily_sales_data_0.csv', './data/daily_sales_data_1.csv', './data/daily_sales_data_2.csv']
combined_data = pd.concat([pd.read_csv(f) for f in file_paths])

# 1. Filter for only "pink morsel"
# We ignore all other morsel types
pink_morsels_only = combined_data[combined_data['product'] == 'pink morsel'].copy()

# 2. Create the "sales" field
# Convert price to a number (removing the '$') and multiply by quantity
pink_morsels_only['price'] = pink_morsels_only['price'].str.replace('$', '', regex=False).astype(float)
pink_morsels_only['sales'] = pink_morsels_only['price'] * pink_morsels_only['quantity']

# 3. Keep only the required fields: Sales, Date, Region
final_data = pink_morsels_only[['sales', 'date', 'region']]

# 4. Output to a single formatted CSV file
final_data.to_csv('formatted_data.csv', index=False)

print("File 'formatted_data.csv' created successfully!")