from collections import defaultdict
from collections import Counter

users_interests = [
	["Hadoop", "Big Data", "HBase", "Java", "Spark", "Storm", "Cassandra"],
	["NoSQL", "MongoDB", "Cassandra", "HBase", "Postgres"],
	["Python", "scikit-learn", "scipy", "numpy", "statsmodels", "pandas"],
	["R", "Python", "statistics", "regression", "probability"],
	["machine learning", "regression", "decision trees", "libsvm"],
	["Python", "R", "Java", "C++", "Haskell", "programming languages"],
	["statistics", "probability", "mathematics", "theory"],
	["machine learning", "scikit-learn", "Mahout", "neural networks"],
	["neural networks", "deep learning", "Big Data", "artificial intelligence"],
	["Hadoop", "Java", "MapReduce", "Big Data"],
	["statistics", "R", "statsmodels"],
	["C++", "deep learning", "artificial intelligence", "probability"],
	["pandas", "R", "Python"],
	["databases", "HBase", "Postgres", "MySQL", "MongoDB"],
	["libsvm", "regression", "support vector machines"]
]

#output: [('Python', 4), ('R', 4), ('Java', 3), ('regression', 3), ('statistics', 3), ('probability', 3), # ... ]

popular_interests = Counter(interest
						for sublist in users_interests
						for interest in sublist
					).most_common()

print(popular_interests)
interest_by_popularity = defaultdict(list)

for interest, popularity in popular_interests:
    interest_by_popularity[popularity].append(interest)

print(interest_by_popularity[4])
popularity_by_interest = defaultdict(list)
for interest, popularity in popular_interests:
    popularity_by_interest[interest].append(popularity)

print(popularity_by_interest["Hadoop"])

def same_popular_new_interests(interests, max_result = 5):
	new_interests = []
	cpt = 0
	for interest in interests:
		pop = popularity_by_interest[interest][0]
		for interest_same_popularity in interest_by_popularity[pop]:
			if interest_same_popularity not in interests and interest_same_popularity not in new_interests and cpt <= max_result:
				new_interests.append(interest_same_popularity)
				cpt += 1

	return new_interests

def most_popular_new_interests(interests, max_result = 5):
	new_interests = []
	cpt = 0
	for interest, popularity in popular_interests:
		if interest not in interests and interest not in new_interests and cpt <= max_result:
			new_interests.append( (interest, popularity) )
			cpt += 1

	return new_interests

print(most_popular_new_interests(users_interests[1], 7))
