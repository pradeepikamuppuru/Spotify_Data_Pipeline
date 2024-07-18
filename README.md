
# Spotify Data Pipeline

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Procedure](#procedure)
  - [Data Collection](#data-collection)
  - [Creating an EC2 Instance and Launching Airflow](#creating-an-ec2-instance-and-launching-airflow)
  - [Using Airflow to Execute and Activate the Pipeline](#using-airflow-to-execute-and-activate-the-pipeline)



## Overview
The Spotify Data Pipeline project is a robust data engineering solution designed to automate the collection, processing, and analysis of data from Spotify. This pipeline leverages various tools and technologies to ensure seamless data extraction, transformation, and loading, facilitating real-time insights and analytics.

## Features
- Automated data extraction from Spotify API.
- Data processing and transformation using Pandas.
- Scheduling and orchestration with Apache Airflow.
- Deployment on AWS EC2 for scalability.
- Data storage on AWS S3 for persistence.
- Real-time data insights and analytics.

## Architecture
The architecture of the Spotify Data Pipeline consists of the following components:
- **Data Collection**: Extract data from Spotify API.
- **Data Processing**: Transform the data using Pandas.
- **Data Orchestration**: Schedule and manage the data pipeline with Apache Airflow.
- **Deployment**: Host the pipeline on AWS EC2.
- **Data Storage**: Store the processed data on AWS S3.

## Technologies Used
- Python
- Spotify API
- Pandas, spotipy
- Apache Airflow
- AWS EC2
- AWS S3

## Procedure

### 4.1. Data Collection:
Source used: [Spotify API](https://developer.spotify.com/documentation/web-api)

1. Create an account on Spotify.
2. Navigate to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
3. Choose 'Create new app' and enter the necessary details.
4. Copy the 'Client ID' and 'Client Secret' displayed for later use.
5. Using the derived 'Client ID' and 'Client Secret', request an access token.
6. Use the access token to retrieve the necessary data. The output data is in JSON format.
7. Write a code to retrieve essential columns for the project. This code is used in further parts of the project and is named `spotify_etl`.

### 4.2. Creating an EC2 Instance and Launching Airflow:
1. Log in to the AWS Management Console.
2. Select the location and launch an EC2 instance.
3. Choose the following details:
   - Name: Airflow_compute
   - AMI: Ubuntu
   - Instance type: t2.small
   - Key pair: set
   - Allow HTTP and HTTPS traffic
4. Launch the instance.

### 4.3. Using Airflow to Execute and Activate the Pipeline:
1. Find the active `spotify_dag` in the Airflow dashboard.
2. Select the code part of the DAG from the navbar.
3. Run the code by selecting the graph from the navbar and debug if any issues arise.
4. After execution, check if the pipeline is functioning properly by checking the S3 bucket (destination) in the AWS Management Console.


