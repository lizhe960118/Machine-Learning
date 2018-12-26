from pyspark import SparkContext

sc = SparkContext('local[2]', 'First Spark App')

data = sc.textFile("data/UserPurchaseHistory.csv").map(lambda line:
	line.split(",")).map(lambda record:(record[0], record[1], record[2]))

# count purchase number
numPurchases = data.count()

# count users number
uniqueUsers = data.map(lambda record:record[0]).distinct().count()

# count all income
totalRevenue = data.map(lambda record:float(record[2])).sum()

# count most popular products
products = data.map(lambda record:(record[1], 1.0)).reduceByKey(lambda a,b:a + b).collect()
mostPopular = sorted(products, key=lambda x:x[1], reverse=True)[0]

print("Total purchases %d " % numPurchases)
print("Unique users: %d " % uniqueUsers)
print("Total revenue: %2.2f " % totalRevenue)
print("Most popular product: %s with %d purchases " % (mostPopular[0], mostPopular[1]))
