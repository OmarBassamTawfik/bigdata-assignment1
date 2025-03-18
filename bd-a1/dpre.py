import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder, KBinsDiscretizer # type: ignore


# ensure a dataset path is provided
if len(sys.argv) != 2:
    print("Usage: python3 dpre.py <input-file>")
    sys.exit(1)

input_file = sys.argv[1]

print(f"Debug: Input file received - {input_file}")


# load dataset
try:
    df = pd.read_csv(input_file)
    print(f"Dataset loaded from {input_file}")

except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)


# data Cleaning
df.drop_duplicates(inplace=True)  # remove duplicates
df.dropna(inplace=True)  # remove rows with missing values


# data Transformation
# normalize numerical columns
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])


# encode categorical columns
categorical_cols = df.select_dtypes(include=['object']).columns
encoder = LabelEncoder()
for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])


# dimensionality Reduction (Optional: Remove Low Variance Features)
df = df.loc[:, df.var() > 0.01]  # drop low variance features


# data Discretization
# discretize numerical data into 3 bins
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
df[numerical_cols] = discretizer.fit_transform(df[numerical_cols])


# save processed data
output_file = "/home/doc-bd-a1/res_dpre.csv"
df.to_csv(output_file, index=False)
print(f"Processed dataset saved as {output_file}")