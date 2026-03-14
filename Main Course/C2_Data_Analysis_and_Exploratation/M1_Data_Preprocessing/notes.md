# Data Processing

Data Processing is the process of collecting, cleaning, transforming, and preparing data so it can be used for analysis, visualization, or machine learning.

Raw data is usually:
- Incomplete
- Noisy
- Inconsistent
- Unstructured

Therefore it must be processed before analysis.

Typical Data Processing Pipeline:
1. Data Sourcing
2. Data Loading
3. Data Cleaning
4. Data Transformation
5. Data Analysis

---

# 1. Data Sourcing

Data sourcing refers to collecting data from different sources for analysis.

Common data sources:
- Files (CSV, Excel, JSON)
- Databases
- APIs
- Public datasets
- Web scraping
- Internal company systems

Good data sourcing ensures:
- Reliable data
- Relevant data
- Accurate analysis

---

# Segment 1: Introduction to Data Preprocessing

Data preprocessing prepares raw data before analysis or machine learning.

Real-world datasets often contain:
- Missing values
- Incorrect values
- Outliers
- Duplicate rows
- Inconsistent formats

Main preprocessing steps:
- Data cleaning
- Handling missing values
- Removing duplicates
- Handling outliers
- Feature scaling
- Data transformation

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head()
```

Useful commands:

```python
df.info()
df.describe()
df.shape
```

---

# Segment 2: Public and Private Data

## Public Data

Public data is freely available for anyone to use.

Examples:
- Government datasets
- Research datasets
- Open-source datasets

Popular platforms:
- Kaggle
- UCI Machine Learning Repository
- Google Dataset Search
- World Bank Data

Advantages:
- Free access
- Good for learning
- Useful for experimentation

Limitations:
- May not represent real-world business problems.

---

## Private Data

Private data belongs to organizations and is not publicly accessible.

Examples:
- Company sales data
- Customer transaction data
- Medical records
- Banking data

Challenges:
- Privacy issues
- Security restrictions
- Compliance requirements

---

# Segment 3: Loading Data from Files

Data scientists commonly load data from files.

Common file formats:
- CSV
- Excel
- JSON
- TXT

Most used Python library: Pandas

Load CSV file:

```python
import pandas as pd

df = pd.read_csv("data.csv")
```

Load Excel file:

```python
df = pd.read_excel("data.xlsx")
```

Load JSON file:

```python
df = pd.read_json("data.json")
```

Useful functions:

```python
df.head()
df.tail()
df.columns
df.shape
df.info()
```

---

# Segment 4: Loading Data from Public Sources

Data can be loaded directly from online sources.

Example:

```python
url = "https://example.com/data.csv"
df = pd.read_csv(url)
```

Other sources include:
- APIs
- Kaggle datasets
- Cloud storage
- Database connections

Libraries used:
- pandas
- requests
- kaggle API

---

# Segment 5: Web Scraping HTML Tables

Web scraping extracts data from websites.

Sometimes websites contain data inside HTML tables.

Libraries used:
- requests
- BeautifulSoup
- pandas

Example:

```python
import pandas as pd

url = "https://example.com/table"
tables = pd.read_html(url)

df = tables[0]
```

This extracts the first HTML table from the webpage.

---

# 2. Data Cleaning

Data cleaning improves data quality by fixing errors and inconsistencies.

Goals:
- Remove incorrect data
- Handle missing values
- Fix formatting issues
- Remove duplicates

Clean data improves:
- Analysis accuracy
- Machine learning model performance

---

# Segment 1: Introduction

Real-world data is rarely perfect.

Common problems include:
- Missing values
- Incorrect data types
- Duplicate rows
- Outliers
- Invalid values

Example to check missing values:

```python
df.isnull().sum()
```

---

# Segment 2: Data Types

Each column has a specific data type.

Common data types:

Integer → 10  
Float → 10.5  
String → "John"  
Boolean → True / False  
Datetime → 2025-01-01  

Check data types:

```python
df.dtypes
```

Convert data types:

```python
df['age'] = df['age'].astype(int)
```

---

# Segment 3: Fixing Rows and Columns

Sometimes datasets contain:
- Incorrect column names
- Extra rows
- Misaligned data

Rename columns:

```python
df.rename(columns={'old_name':'new_name'}, inplace=True)
```

Remove columns:

```python
df.drop(columns=['column_name'])
```

Remove rows:

```python
df.drop(index=0)
```

---

# Segment 4: Handling Missing Values

Missing values occur when data is not recorded.

Common methods to handle them:

1. Remove rows
2. Replace with mean
3. Replace with median
4. Replace with mode
5. Forward/Backward fill

Remove missing values:

```python
df.dropna()
```

Fill missing values:

```python
df.fillna(0)
```

Replace with mean:

```python
df['age'].fillna(df['age'].mean())
```

---

# Segment 5: Handling Outliers

Outliers are extreme values that differ significantly from other data points.

Example:

Dataset:  
[10, 12, 11, 13, 100]

100 is an outlier.

Methods to detect outliers:
- Boxplot
- Z-score
- IQR method

Example:

```python
import seaborn as sns

sns.boxplot(x=df['salary'])
```

---

# Segment 6: Standardising Values

Standardization scales data so features have similar ranges.

Common scaling techniques:

1. Standardization (Z-score)
2. Normalization (Min-Max scaling)

Standardization formula:

Z = (X - Mean) / Standard Deviation

Example:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
```

---

# Segment 7: Fixing Invalid Values and Filtering Data

Invalid values occur due to:
- Data entry mistakes
- Incorrect formats
- System errors

Example:
Age = -5 (invalid)

Filtering data:

```python
df[df['age'] > 0]
```

Replace invalid values:

```python
df.loc[df['age'] < 0, 'age'] = df['age'].mean()
```

---

# Segment 8: Handling Missing Values (Additional Practice)

Advanced techniques:

Forward Fill:

```python
df.fillna(method='ffill')
```

Backward Fill:

```python
df.fillna(method='bfill')
```

Interpolation:

```python
df.interpolate()
```

These methods estimate missing values using surrounding data.

---

# Summary

Data Processing includes:

1. Data Sourcing
2. Data Loading
3. Data Cleaning
4. Handling Missing Values
5. Handling Outliers
6. Standardizing Data

Proper data processing ensures:
- Better analysis
- Better machine learning models
- Accurate insights