import pandas as pd

# Load the files
netflix = pd.read_csv(
    'cleaned_netflix_pricing_2025.csv')
wb = pd.read_csv(
    'cleaned_world_bank_data4.csv')

# Mapping dictionary (World Bank Name -> Netflix Name)
country_mapping = {
    'Antigua and Barbuda': 'Antigua & Barbuda',
    'Bosnia and Herzegovina': 'Bosnia & Herzegovina',
    'Brunei Darussalam': 'Brunei',
    'Cabo Verde': 'Cape Verde',
    'Congo Dem. Rep.': 'Congo - Kinshasa',
    'Congo Rep.': 'Congo - Brazzaville',
    "Cote d'Ivoire": "Côte d’Ivoire",
    'Curacao': 'Curaçao',
    'Macao': 'Macau',
    'Micronesia Fed. Sts.': 'Micronesia',
    'Myanmar': 'Myanmar (Burma)',
    'Sao Tome and Principe': 'São Tomé & Príncipe',
    'Sint Maarten (Dutch part)': 'Sint Maarten',
    'St. Kitts and Nevis': 'St. Kitts & Nevis',
    'St. Martin (French part)': 'St. Martin',
    'St. Vincent and the Grenadines': 'St. Vincent & Grenadines',
    'Turks and Caicos Islands': 'Turks & Caicos Islands',
    'Virgin Islands (U.S.)': 'U.S. Virgin Islands'
}

# Apply the mapping to the Country_Name column
wb['Country_Name'] = wb['Country_Name'].replace(country_mapping)

# Optional: Convert all " and " to " & " for any other remaining cases
wb['Country_Name'] = wb['Country_Name'].str.replace(
    ' and ', ' & ', regex=False)

# Save the new aligned file
wb.to_csv(
    'aligned_world_bank_data.csv', index=False)

print("The file 'aligned_world_bank_data.csv' has been created successfully.")
