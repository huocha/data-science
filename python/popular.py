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

popular_interests = defaultdict(list)

# for sublist in l:
#    for item in sublist:
#        flat_list.append(item)

interests = [interest for sublist in users_interests for interest in sublist]


print(Counter(interests))
