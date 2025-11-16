from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder \
    .appName("Education Data Example") \
    .getOrCreate()

# Example education sector data (SchoolName, StudentCount, City)
data = [
    ("Greenwood High", 520, "New York"),
    ("Sunrise Academy", 350, "Los Angeles"),
    ("Maple Leaf School", 440, "Chicago"),
    ("River Valley High", 610, "Houston"),
    ("Pinecrest School", 280, "Phoenix"),
    ("Hilltop Academy", 330, "Philadelphia"),
    ("Silver Oak High", 470, "San Antonio"),
    ("Oak Ridge School", 390, "San Diego"),
    ("Lakeside High", 520, "Dallas"),
    ("Cedar Grove School", 405, "San Jose"),
    ("Springfield Academy", 370, "Austin"),
    ("Bridgewater High", 480, "Jacksonville"),
    ("Redwood School", 515, "Fort Worth"),
    ("Sunnyside School", 285, "Columbus"),
    ("Parkview Academy", 415, "Charlotte"),
    ("Canyon Ridge High", 300, "San Francisco"),
    ("Willow Creek School", 395, "Indianapolis"),
    ("Meadowbrook High", 355, "Seattle"),
    ("Evergreen Academy", 540, "Denver"),
    ("Liberty High", 410, "Boston")
]

columns = ["SchoolName", "StudentCount", "City"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Stop Spark session
spark.stop()
