import pandas as pd

# Load the file
# Note: Use the correct path for your environment
df = pd.read_csv(
    'Global Netflix Price - by regions(12-2025).csv')

# 1. Remove unnecessary columns (CNY values, duplicate Country, translations, etc.)
cols_to_drop = [
    'MobileCNY', 'With_Ads_CNY', 'BasicCNY', 'StandardCNY', 'PremiumCNY',
    'Country.1', 'Translation', 'Updated On 2025-12-02'
]
df_cleaned = df.drop(columns=cols_to_drop)

# 2. Rename columns for better use in Tableau (replace spaces with underscores)
rename_map = {
    'Standard with ads': 'Standard_with_ads_Local',
    'Extra member slots': 'Extra_member_slots_Details',
    'MobileUSD': 'Price_Mobile_USD',
    'With_Ads_USD': 'Price_With_Ads_USD',
    'BasicUSD': 'Price_Basic_USD',
    'StandardUSD': 'Price_Standard_USD',
    'PremiumUSD': 'Price_Premium_USD'
}
df_cleaned = df_cleaned.rename(columns=rename_map)

# 3. Handle missing values (NaN)
# In USD price columns, we set 0 where there is no value (means the plan is not available)
price_cols = ['Price_Mobile_USD', 'Price_With_Ads_USD',
              'Price_Basic_USD', 'Price_Standard_USD', 'Price_Premium_USD']
df_cleaned[price_cols] = df_cleaned[price_cols].fillna(0)

# In the description of Extra slots, we put 'Not Available' instead of NaN
df_cleaned['Extra_member_slots_Details'] = df_cleaned['Extra_member_slots_Details'].fillna(
    'Not Available')

# 4. Text cleaning (removing any leading/trailing spaces from country names)
df_cleaned['Country'] = df_cleaned['Country'].str.strip()

# --- ADDITION: Align Country Names ---
# Mapping to match the naming convention of cleaned_netflix_data_final2.csv
country_mapping = {
    'Czechia': 'Czech Republic',
    'Türkiye': 'Turkey'
}
df_cleaned['Country'] = df_cleaned['Country'].replace(country_mapping)
# --------------------------------------

# 5. Save the cleaned file
df_cleaned.to_csv(
    'cleaned_netflix_pricing_2025.csv', index=False)

print("Το αρχείο αποθηκεύτηκε επιτυχώς με ενημερωμένα ονόματα χωρών.")
