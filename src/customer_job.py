from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CustomerDemo") \
    .getOrCreate()

data = [
    (1, "John"),
    (2, "Mary"),
    (3, "Peter")
]

df = spark.createDataFrame(
    data,
    ["id", "name"]
)

df.show()