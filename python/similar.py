import numpy
import math
from collections import defaultdict

def cosine_similarity(v, w):
	return numpy.dot(v, w)/ math.sqrt( numpy.dot(v,v) * numpy.dot(w,w) )

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

# map vector of similarity vs user_interest: map(f, iterable) =  [f(x) for x in iterable]
user_interest_matrix = list(map(make_user_interest_vector, users_interests))

user_similarities = [[cosine_similarity(interest_vector_i, interest_vector_j)
	for interest_vector_j in user_interest_matrix]
	for interest_vector_i in user_interest_matrix]
# print(user_similarities)


# user_similarities_sorted = [ sorted(user_similarity, reverse=True) for user_similarity in user_similarities]
# print(user_similarities_sorted)

# find the most similar user to a given user
def most_similar_users_to(user, max_result = 5):
	user_similarities_sorted = sorted(enumerate(user_similarities[user]), key= lambda x:x[1], reverse=True)
	return user_similarities_sorted[1: max_result+1]

print(most_similar_users_to(0))

# given a user_id return a list of interests he not interested yet from most to least
def user_based_suggestion(user_id):
	suggestions = defaultdict(float)
	# cumulate similarity
	for other_user, similarity in most_similar_users_to(user_id):
		for interest in users_interests[other_user]:
			suggestions[interest] += similarity
	suggestions = sorted(suggestions.items(), key=lambda x:x[1], reverse=True)

	return [ (suggestion, totalSimilarity)
			for suggestion, totalSimilarity in suggestions
			if suggestion not in users_interests[user_id] ]


user_suggestion = user_based_suggestion(0)
print(user_suggestion)
