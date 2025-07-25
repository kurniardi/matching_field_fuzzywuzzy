# 📌 Name Matching using FuzzyWuzzy
## 🧾 Description
This repository provides a Python script that performs fuzzy string matching between two name lists from separate Excel files using the fuzzywuzzy or rapidfuzz libraries.

The goal is to identify and match name records across systems, where names may vary due to formatting, spelling inconsistencies, or abbreviations.
---

## ⚙️ Features
📥 Read names from two Excel files (Name A.xlsx and Name B.xlsx).

🧹 Clean and preprocess the names (trim spaces, remove nulls).

🤖 Match each name A to the closest name B using fuzzy logic.

📊 Score matches with configurable threshold using token_set_ratio.

💾 Export matched results to a new Excel file (Fuzzy_Matched_Customers.xlsx)
---

## 🧰 Use Cases
🧼 Data cleansing and deduplication.

🔗 Master data harmonization.

🔄 Reconciliation between ERP / CRM systems.

🕵️‍♂️ Detect similar but inconsistent naming.

## 📦 Requirements & Installation
Make sure you have Python installed (preferably 3.8 or newer). Then install the required libraries below:

### 🔧 Basic Setup
```bash
pip install pandas
pip install openpyxl
```

### 🔍 Fuzzy Matching Options
#### Option 1: Using FuzzyWuzzy (classic).
⚠️ Slower, but easy to use.
```bash
pip install fuzzywuzzy
pip install python-Levenshtein  # Optional but recommended for speed.
```

#### Option 2: Using RapidFuzz (modern & faster)
🚀 Much faster and actively maintained.
```bash
pip install rapidfuzz
```
