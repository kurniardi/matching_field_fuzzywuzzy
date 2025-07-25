# Import necessary packages.
import pandas as pd
from fuzzywuzzy import fuzz, process

# Load Excel files into DataFrames.
df_name_a = pd.read_excel("Names A.xlsx")  # DataFrame for the first dataset
df_name_b = pd.read_excel("Names B.xlsx")  # DataFrame for the second dataset

# Extract unique non-null names from the column named in each DataFrame.
a_names = df_name_a['Names A'].dropna().unique()
b_names = df_name_b['Names B'].dropna().unique()

# Clean and strip whitespace from the names in both datasets.
# Converts all values to string, strips whitespace, and ignores empty strings.
a_name_clean = [str(x).strip() for x in a_names if str(x).strip()]
b_name_clean = [str(x).strip() for x in b_names if str(x).strip()]

# Set the threshold for fuzzy match score (0-100 scale).
threshold = 85  # Only matches with a score >= 85 will be considered as matches

# Initialize a list to store match results.
result_rows = []

# Loop through each name in Dataset A.
for a_name in a_name_clean:
    # Find top 3 closest matches in Dataset B using token set ratio.
    matches = process.extract(a_name, b_name_clean, limit=3, scorer=fuzz.token_set_ratio)
    matched = False  # Flag to check if there's any match above the threshold
    
    # Loop through the top matches and check if any score is above the threshold.
    for match_name, score in matches:
        if score >= threshold:
            # If matched, save the matched pair and score.
            result_rows.append({
                'Name (A)': a_name,
                'Name (B)': match_name,
                'MatchScore': score
            })
            matched = True
    
    # If no matches are found above the threshold, log it as unmatched.
    if not matched:
        result_rows.append({
            'Name (A)': a_name,
            'Name (B)': None,
            'MatchScore': None
        })

# Create a DataFrame from the result list.
result_df = pd.DataFrame(result_rows)

# Save the result to an Excel file.
result_df.to_excel("Fuzzy_Matched.xlsx", index=False)

# Notify user that the process is completed.
print("Done! Check Fuzzy_Matched.xlsx")
