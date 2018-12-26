import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._


object ScalaApp{
	def main(args: Array[String]){
		val sc = new SparkContext("local[2]", "Frist Spark App")
		val data = sc.textFile("data/UserPurchaseHistory.csv").map(line => line.split(",")).map(purchaseRecord => (purchaseRecord(0), purchaseRecord(1), purchaseRecord(2))
		val numPurchases = data.count()
		val uniqueUsers = data.map{case (user, product, price) => user}.distinct().count()
		val totalRevenue = data.map{case (user, product, price) => price.toDouble}.sum()
		val productsByPopularity = data.map{case (user, product, price) => (product, 1)}.reduceByKey(_ + _).collect().sortBy(-_._2)
		val mostPopular = productsByPopularity(0)
		printIn("Total purchases:" + numPurchases)
		printIn("Unique users:" + uniqueUsers)
		printIn("Total revenue:" + totalRevenue)
		printIn("Most popular product : %s with %d purchases".format(mostPopular._1, productsByPopularity._2))
	}
}