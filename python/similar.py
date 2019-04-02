from numpy import dot
import math

def cosine_similarity(v, w):
	return dot(v, w)/ math.sqrt( dot(v,v) * dot(w,w) )

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

# sort users_interests by aphabetic
unique_interests = sorted(list({ interest
	for user_interests in users_interests
	for interest in user_interests }))

def make_user_interest_vector(user_interests):
	return [1 if interest in user_interests else 0
		for interest in unique_interests]

# map vector of similarity vs user_interest
user_interest_matrix = list(map(make_user_interest_vector, users_interests))

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
	for interest_vector_j in user_interest_matrix]
	for interest_vector_i in user_interest_matrix]

print(user_similarities[0][9])
