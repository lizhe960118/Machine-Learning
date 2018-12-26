val rawData = sc.textFile("/home/lizhe/ML-Spark/chapter_04/ml-100k/u.data")
rawData.first()

val rawRatings = rawData.map(_.split("\t").take(3))
rawRatings.first()

import org.apache.spark.mllib.recommendation.ALS
ALS.train

import org.apache.spark.mllib.recommendation.Rating 
Rating()

val ratings = rawRatings.map{case Array(user, movie, rating) => Rating(user.toInt, movie.toInt, rating.toDouble)}
ratings.first()

val model = ALS.train(ratings, 50, 10, 0.01)

model.userFeatures

model.userFeatures.count

model.productFeatures.count

val predictedRating = model.predict(789, 123)

val userId = 789
val K = 10
val topKRecs = model.recommendationProducts(userId, K)
println(topKRecs.mkString("\n"))

val movies = sc.textFile("/home/lizhe/ML-Spark/chapter_04/ml-100k/u.item")
val titles = movies.map(line => line.split("\\|").take(2)).map(array => (array(0).toInt, array(1))).collectAsMap()

titles(123)

val moviesForUser = ratings.keyBy(_.user).lookup(789)

println(moviesForUser.size)

moviesForUser.sortBy(-_.rating).take(10).map(rating => (title(rating.product), rating.rating)).foreach(println)

topKRecs.map(rating => (title(rating.product), rating.rating)).foreach(println)

import org.jblas.DoubleMatrix
val aMatrix = new DoubleMatrix(Array(1.0, 2.0, 3.0))

def cosineSimilarity(vec1:DoubleMatrix, vec2:DoubleMatrix):Double = {
	vec1.dot(vec2) / (vec1.norm2() * vec2.norm2())
}

val itemId = 567
val itemFactor = model.productFeatures.lookup(itemId).head

val itemVector = new DoubleMatrix(itemFactor)

cosineSimilarity(itemFactor, itemVector)

val sims = model.productFeatures.map{ case (id, factor) =>
	val factorVector = new DoubleMatrix(factor)
	val sim = cosineSimilarity(factorVector, itemVector)
	(id, sim)
}

val sortedSims = sims.top(K).(Ordering.by[(Int, Double), Double]{case (id, similarity) => similarity})
println(sortedSims.mkString("\n"))

println(titles(itemId))

val sortedSims2 = sims.top(K + 1)(Ordering.by[(Int, Double)] {case (id, similarity) => similarity})

sortedSims2.slice(1, 11).map{case (id, sim) => (titles(id), sim)}.mkString("\n")

val actualRating = moviesForUser.take(1)(0)
val predictedRating = model.predict(789, actualRating.product)

val squaredError = math.pow(predictedRating - actualRating.rating, 2.0)

val usersProducts = ratings.map{case Rating(user, product, rating) => (user, product)}

val predictions = model.predict(usersProducts),map{
	case Rating(user, product, rating) => ((user, product), rating)
}

val ratingsAndPredctions = ratings.map{
	case Rating(user, product, rating) => ((user, product), rating)
}.join(predictions)

val MSE = ratingsAndPredctions.map{
	case ((user, product), (actualRating, predicted)) => math.pow((actualRating - predicted), 2)
}.reduce(_ + _) / ratingsAndPredctions.count

println("Mean Squared Error = " + MSE)

val RMSE = math.sqrt(MSE)
println("Root Mean Squared Error = " + RMSE)


def avgPrecisionK(actual: Seq[Int], predicted:Seq[Int], k:Int):Double = {
	val predK = predicted.take(k)
	val score = 0.0
	val numHits = 0.0
	for ((p,i) <- predK.zipWithIndex){
		if (actual.contains(p)){
			numHits += 1.0
			score += numHits / (i.toDouble + 1.0)
		}
	}
	if (actual.isEmpty){
		1.0
	}else{
		score / scala.math.min(actual.size, k).toDouble
	}
}

val actualMovies = moviesForUser.map(_.product)
val predictedMovies = topKRecs.map(_.product)
val apk10 = avgPrecisionK(actualMovies, predictedMovies, 10)

val itemFactors = model.productFeatures.map{
	case (id, factor) => factorVector
}.collect()
val itemMatrix = new DoubleMatrix(itemFactors)
println(itemMatrix.rows, itemMatrix.columns)

val imBroadcast = sc.broadcast(itemMatrix)

val allRecs = model.userFeatures.map{case (userId, array) =>
	val userVector = new DoubleMatrix(array)
	val scores = imBroadcast.value.mmul(userVector)
	val sortedWithId = scores.data.zipWithIndex.sortBy(-_._1)
	val recommendedIds = sortedWithId.map(_._2 + 1).toSeq(userId, recommendedIds)
}

val userMovies = ratings.map{
	case Rating(user, product, rating) => (user, product)
}.groupBy(_._1)

val K = 10
val MAPK = allRecs.join(userMovies).map{case (userId, (predicted, actualWithIds)) =>
	val actual = actualWithIds.map(_._2).toSeq
	avgPrecisionK(actual, predicted, K)
}.reduce(_ + _) / allRecs.count
println("Mean Average Precision at K = " + MAPK)

import org.apache.spark.mllib.evaluation.RegressionMetrics
val predictedAndTrue = ratingsAndPredctions.map{
	case ((user, product), (actual, predicted)) => (actual, predicted)
}
val regressionMetrics = new RegressionMetrics(predictedAndTrue)
println("Mean Squared Error = " + regressionMetrics.meanSquaredError)
println("Root Mean Squared Error = " + regressionMetrics.rootMeanSquaredError)

import org.apache.spark.mllib.evaluation.RankingMetrics
val predictedAndTrueForRanking = allRecs.join(userMovies).map{ case (userId, (predicted, actualWithIds)) =>
	val actual = actualWithIds.map(_._2)
	(predicted.toArray, actual.toArray)
}
val rankingMetrics = new RankingMetrics(predictedAndTrueForRanking)
println("Mean Average Precision = " + rankingMetrics.meanAveragePrecision)

val MAPK2000 = allRecs.join(userMovies).map{case (userId, (predicted, actualWithIds)) =>
	val actual = actualWithIds.map(_._2).toSeq
	avgPrecisionK(actual, predicted, 2000)
}.reduce(_ + _) / allRecs.count
println("Mean Average Precision = " + MAPK2000)