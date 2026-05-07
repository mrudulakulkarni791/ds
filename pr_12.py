#12th
#code for the references
from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder.appName("Simple Spark Program").getOrCreate()

# Create Data
data = [
    ("Alice", 30, "HR"),
    ("Bob", 35, "Engineering"),
    ("Charlie", 40, "Marketing"),
    ("David", 28, "Engineering"),
    ("Eve", 45, "HR")
]

# Create DataFrame
df = spark.createDataFrame(data, ["name", "age", "department"])

# Show Original Data
print("Original Data:")
df.show()

# Filter
filtered = df.filter(df.age > 30).select("name", "age")
print("Filtered Data:")
filtered.show()

# Aggregation
avgAge = df.groupBy("department").avg("age")
print("Average Age:")
avgAge.show()

# Stop Spark
spark.stop()