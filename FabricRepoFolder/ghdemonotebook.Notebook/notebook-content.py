# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "b9058056-c0e4-4bf7-972b-a8227e59de29",
# META       "default_lakehouse_name": "GitHubdemolkhouse",
# META       "default_lakehouse_workspace_id": "0c34e8e4-135c-4bec-896c-9bb5d346b36c",
# META       "known_lakehouses": [
# META         {
# META           "id": "b9058056-c0e4-4bf7-972b-a8227e59de29"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ### Fabric - Git Integration - Fabric/ADO Demo Notebook #### 
# Fabric notebook metadata and content will be synchronized with test branch (created from main) in GH Git repository

# CELL ********************

### Load data - Spark ###
df = spark.read.format("csv").option("header","true").load("Files/sales_gh.csv")
# df now is a Spark DataFrame containing CSV data from "Files/sales_gh.csv".
display(df.limit(10))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

### Load data - Pandas ###
import pandas as pd
# Load data into pandas DataFrame from "/lakehouse/default/" + "Files/sales_gh.csv"
df = pd.read_csv("/lakehouse/default/" + "Files/sales_gh.csv")
display(df.head(10))


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
