# CSCI461 - Big Data Assignment 1

## Overview

This project is for **CSCI461: Introduction to Big Data** at Nile University (Spring 2025). It involves setting up a **Dockerized data pipeline** to process a dataset using Python inside a container.

## Tasks

- Create a **Dockerfile** that sets up an Ubuntu-based environment with Python and necessary libraries.
- Implement Python scripts to:
  - **Load data (`load.py`)** from a user-provided path.
  - **Preprocess data (`dpre.py`)** (cleaning, transformation, reduction, discretization).
  - **Perform Exploratory Data Analysis (`eda.py`)** and save insights.
  - **Generate a visualization (`vis.py`)** and save it as an image.
  - **Apply K-means clustering (`model.py`)** and store cluster sizes.
- Use a **Bash script (`final.sh`)** to copy results from the container and stop it.

## Execution Steps

1. **Pull the Docker Image from Docker Hub**

   ```sh
   docker pull omarbassamtawfik/bigdata-a1
   ```

2. **Build the Docker Image**
   ```sh
   docker build -t bigdata-a1 .
   ```

3. **Run the Docker Container**

   ```sh
   docker run -it --name <container-name> bigdata-a1  
   ```

4. **Execute the Pipeline** (inside the container)

   ```sh
   python3 load.py <dataset-path>  
   ```

5. **Exit the Container**

   ```sh
   exit
   ```
   
6. **Restart the Container** (in detach mode)

   ```sh
   docker start <container-name>
   ```
   
7. **Copy Results to Local Machine & Stop Container**

   ```sh
   bash final.sh <container-name>
   ```

## Expected Output Files

- `res_dpre.csv` → Processed dataset after preprocessing.
- `eda-in-1.txt`, `eda-in-2.txt`, `eda-in-3.txt`, `eda-in-4.txt`, `eda-in-5.txt` → Insights from EDA.
- `vis-1-gender.png`, `vis-2-survival.png`, `vis-3-age.png` → Visualization of the dataset.
- `k.txt` → Number of records in each cluster from K-means.

## Contributors

- [**Omar Bassam**](https://github.com/OmarBassamTawfik)  
- [**AbdelRahman AlSammany**](https://github.com/Sammany1)  
- [**Mostafa Alsheikh**](https://github.com/Mostafa-alsheikh)
- [**Shahd Mansour**](https://github.com/shaahdmaansour)  

---

