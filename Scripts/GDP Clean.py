import pandas as pd


def clean_indicator_file(file_path, indicator_name_short):
    """
    Loads a World Bank CSV, removes metadata headers, and reshapes it 
    from a wide format (years as columns) to a long format (years as rows).
    """
    # World Bank CSVs usually have 4 rows of descriptive text at the top.
    df = pd.read_csv(file_path, skiprows=4)

    # Remove any trailing empty columns (e.g., 'Unnamed: 69') that often appear in exports.
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    # The original data is "Wide" (years as columns). We 'melt' it into "Long" format (years as rows).
    id_vars = ['Country Name', 'Country Code',
               'Indicator Name', 'Indicator Code']
    year_columns = [col for col in df.columns if col.isdigit()]

    df_melted = df.melt(id_vars=id_vars,
                        value_vars=year_columns,
                        var_name='Year',
                        value_name=indicator_name_short)

    # Convert the Year column to integers for consistent filtering and sorting.
    df_melted['Year'] = df_melted['Year'].astype(int)

    return df_melted


# --- STEP 1: Process individual indicator files ---
# We clean each indicator separately using the function defined above.
gdp_df = clean_indicator_file(
    'GDP.csv', 'GDP')

gdp_pcap_df = clean_indicator_file(
    'GDP_per_capita.csv', 'GDP_per_Capita')

pop_df = clean_indicator_file(
    'Population.csv', 'Population')


# --- STEP 2: Merge all indicators into one master dataframe ---
# We merge on Country Code and Year using an 'outer' join to preserve all data points.
merged_df = gdp_df[['Country Name', 'Country Code', 'Year', 'GDP']].merge(
    gdp_pcap_df[['Country Code', 'Year', 'GDP_per_Capita']],
    on=['Country Code', 'Year'],
    how='outer'
).merge(
    pop_df[['Country Code', 'Year', 'Population']],
    on=['Country Code', 'Year'],
    how='outer'
)


# --- STEP 3: Add Country Metadata ---
# This file provides the Region and Income Group for each country code.
meta_df = pd.read_csv(
    'Country_Metadata.csv')
meta_df = meta_df[['Country Code', 'Region', 'IncomeGroup']]

# Merge metadata into the main dataset.
final_df = merged_df.merge(meta_df, on='Country Code', how='left')


# --- STEP 4: Final Data Cleanup & Alignment ---

# 1. Keep only data from 2010 onwards.
final_df = final_df[final_df['Year'] >= 2010]

# 2. Keep ONLY actual countries.
# Aggregate regions (like 'World') have a null Region in the metadata file.
final_df = final_df.dropna(subset=['Region'])

# 3. Map World Bank names to Netflix country names for compatibility.
COUNTRY_MAP = {
    'Bahamas, The': 'Bahamas',
    'Czechia': 'Czech Republic',
    'Egypt, Arab Rep.': 'Egypt',
    'Gambia, The': 'Gambia',
    'Hong Kong SAR, China': 'Hong Kong',
    'Iran, Islamic Rep.': 'Iran',
    'Korea, Rep.': 'South Korea',
    'Korea, Dem. People\'s Rep.': 'North Korea',
    'Kyrgyz Republic': 'Kyrgyzstan',
    'Lao PDR': 'Laos',
    'Macao SAR, China': 'Macao',
    'Russian Federation': 'Russia',
    'Slovak Republic': 'Slovakia',
    'Somalia, Fed. Rep.': 'Somalia',
    'Syrian Arab Republic': 'Syria',
    'Turkiye': 'Turkey',
    'Venezuela, RB': 'Venezuela',
    'Viet Nam': 'Vietnam',
    'Yemen, Rep.': 'Yemen',
    'Puerto Rico (US)': 'Puerto Rico',
    'West Bank and Gaza': 'Palestine'
}
final_df['Country Name'] = final_df['Country Name'].replace(COUNTRY_MAP)

# 4. Fix the "10 columns" alignment issue.
# We remove remaining commas from country names to prevent CSV splitting errors.
final_df['Country Name'] = final_df['Country Name'].str.replace(
    ',', '', regex=False)

# 5. Reorder the columns for a logical flow.
cols = ['Country Name', 'Country Code', 'Region', 'IncomeGroup',
        'Year', 'GDP', 'GDP_per_Capita', 'Population']
final_df = final_df[cols].sort_values(['Country Name', 'Year'])

# 6. Remove rows where all three indicator data points are empty.
final_df = final_df.dropna(
    subset=['GDP', 'GDP_per_Capita', 'Population'], how='all')


# --- STEP 5: Export the result ---
output_path = 'cleaned_world_bank_data4.csv'
final_df.to_csv(output_path, index=False)

print(f"Success! Final cleaned file saved at: {output_path}")
print(f"Total country rows (2010-present): {len(final_df)}")
