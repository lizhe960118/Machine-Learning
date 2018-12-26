val collection = List("a", "b", "c", "d", "e")

val rddFromCollection = sc.parallelize(collection)

val rddFromTextFile = sc.textFile("LICENSE")

val intsFromStringsRDD = rddFromTextFile.map(line => line.size)

intsFromStringsRDD.count

val sumOfRecords = intsFromStringsRDD.sum 

val numRecords = intsFromStringsRDD.count

val aveLengthOfRecord = sumOfRecords / numRecords

val aveLengthOfRecordChained = rddFromTextFile.map(line => line.size).sum / rddFromTextFile.count

val transformedRDD = rddFromTextFile.map(line => line.size).filter(size => size > 10).map(size => size * 2)

val computation = transformedRDD.sum

rddFromTextFile.cache

val aveLengthOfRecordChained = rddFromTextFile.map(line => line.size).sum / rddFromTextFile.count

val aveLengthOfRecordChainedFromCached = rddFromTextFile.map(line => line.size).sum / rddFromTextFile.count

val broadcastAList = sc.brodacast(List("a", "b", "c", "d", "e"))

sc.parallelize(List("1", "2", "3")).map(x => broadcastAList.value ++ x).collect