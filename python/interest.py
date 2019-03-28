from collections import defaultdict

interests = [
	(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"),(0, "Cassandra"),
	(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
	(2, "Python"), (2, "scikit-learn"), (2, "scipy"), (2, "numpy"), (2, "statsmodels"), (2, "pandas"),
	(3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"),
	(4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm"),
	(5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages"),
	(6, "statistics"), (6, "probability"), (6, "mathematics"), (6, "theory"),
	(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
	(8, "neural networks"), (8, "deep learning"), (8, "Big Data"), (8, "artificial intelligence"),
	(9, "Hadoop"), (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]



def data_scientist_who_like(target_interest):
	scientists = []
	for interest in interests:
		if interest[1] == target_interest and interest[0] not in scientists:
			scientists.append(interest[0])

	return scientists

print(data_scientist_who_like('Big Data'))

# empty dict
user_by_interest = defaultdict(list)

# key is interest, value is array of userId
for userId, interest in interests:
	user_by_interest[interest].append(userId)

# empty dict
interest_by_users = defaultdict(list)

# key is interest, value is array of userId
for userId, interest in interests:
	interest_by_users[userId].append(interest)

print(interest_by_users)
