from pyspark import SparkConf, SparkContext
from pyspark.sql import HiveContext
sc = SparkContext()
sqlContext = HiveContext(sc)
result = sqlContext.sql("FROM test.abc SELECT col1, col2").collect()
print result
