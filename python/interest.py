from collections import defaultdict
from collections import Counter

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

# return user by his interest
def data_scientist_who_like(target_interest):
	scientists = []
	for interest in interests:
		if interest[1] == target_interest and interest[0] not in scientists:
			scientists.append(interest[0])

	return scientists

print(data_scientist_who_like('Big Data'))

# empty dict
user_by_interests = defaultdict(list)

# key is interest, value is array of userId
for userId, interest in interests:
	user_by_interests[interest].append(userId)

# empty dict
interest_by_users = defaultdict(list)

# key is interest, value is array of userId
for userId, interest in interests:
	interest_by_users[userId].append(interest)

# return mutual interest between 2 users
def mutual_interest(user, other):
	mutual = [x for x in interest_by_users[user] if x in interest_by_users[other]]
	return mutual

# return user who like the same thing as given user
def data_scientist_you_should_know(user):
	users = []
	cnt = Counter()
	for interest_user in interest_by_users[user]:
		for user_interest in user_by_interests[interest_user]:
			if user_interest != user:
				cnt[user_interest] += 1
				users.append(user_interest)
	return cnt

print(data_scientist_you_should_know(0))
print(mutual_interest(0, 9))
