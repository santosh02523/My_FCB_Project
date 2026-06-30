import pandas as pd

from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.getOrCreate()

# Create RDD
rdd = spark.sparkContext.parallelize([1, 2, 3, 4])

# Apply transformation
result = rdd.map(lambda x: x * 2)

# Action
print(result.collect())

# Stop Spark Session
spark.stop()