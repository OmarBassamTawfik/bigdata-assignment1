import sys
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# Check if the dataset path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python3 model.py <processed-data-path>")
    sys.exit(1)

# Get the dataset path from the command-line argument
dataset_path = sys.argv[1]

# Validate the dataset path
if not os.path.isfile(dataset_path):
    print(f"Error: The file '{dataset_path}' does not exist.")
    sys.exit(1)

# Read the dataset
try:
    df = pd.read_csv(dataset_path)
    print(f"Dataset loaded successfully from {dataset_path}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)

# Select numeric columns for K-means clustering
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_columns) == 0:
    print("Error: No numeric columns found for clustering.")
    sys.exit(1)

# Prepare the data for K-means
try:
    # Take only numeric columns for clustering
    data_for_clustering = df[numeric_columns]
    
    # Handle missing values if any
    data_for_clustering = data_for_clustering.fillna(data_for_clustering.mean())
    
    # Standardize the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_for_clustering)
    
    # Apply K-means with k=3
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    
    # Count records in each cluster
    cluster_counts = np.bincount(clusters)
    
    # Save the number of records in each cluster to k.txt
    output_path = "/home/doc-bd-a1/k.txt"
    with open(output_path, 'w') as f:
        for i, count in enumerate(cluster_counts):
            f.write(f"Cluster {i}: {count} records\n")
    
    print(f"K-means clustering completed. Results saved to {output_path}")
    
except Exception as e:
    print(f"Error during K-means clustering: {e}")
    sys.exit(1)

print("Model.py executed successfully - pipeline complete!")