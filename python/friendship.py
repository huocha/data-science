from collections import Counter
users = [
	{ "id": 0, "name": "Hero" },
	{ "id": 1, "name": "Dunn" },
	{ "id": 2, "name": "Sue" },
	{ "id": 3, "name": "Chi" },
	{ "id": 4, "name": "Thor" },
	{ "id": 5, "name": "Clive" },
	{ "id": 6, "name": "Hicks" },
	{ "id": 7, "name": "Devin" },
	{ "id": 8, "name": "Kate" },
	{ "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2),  (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
	user["friends"] = []

for user1, user2 in friendships:
	users[user1]["friends"].append(users[user2])
	users[user2]["friends"].append(users[user1])

# return the number of friends given user id
def number_of_friends(user):
	return len(user["friends"])

# take second element for sort
def takeSecond(elem):
    return elem[1]

# get all the connections
total_connection = sum(number_of_friends(user) for user in users)
# get average connection
avg_connection = total_connection/len(users)

print( "total_connection: ", total_connection )
print( "avg_connection: ", avg_connection )

# Create a list to find the most connected people
connection = [ (user["id"],  number_of_friends(user)) for user in users ]
print("All connection: ", connection)

mostConnection = sorted( connection, key=takeSecond, reverse=True )
print("Most connected people :", mostConnection)

leastConnection = sorted( connection, key=takeSecond )
print("Least connected people :", leastConnection)

# search for friendId of given user
def friends_of_user(user):
	return [ friend["id"] for friend in users[user]["friends"] ]
	# return [ (friend["id"], friend["name"]) for friend in users[user]["friends"] ]

print(friends_of_user(0))

# search for friends of friends
def friends_of_friends2(user):
	friends = []
	for friendId in friends_of_user(user):
		friends += friends_of_user(friendId)
	return friends

def not_same_user(user, other):
	return user["id"] != other["id"]

def mutual_friend(user, other):
	mutual = [x for x in friends_of_user(user) if x in friends_of_user(other)]
	return mutual

def friends_of_friends(user):
	friends = []
	friends_user = friends_of_user(user)
	cnt = Counter()
	for friendId in friends_user:
		friends_friends = friends_of_user(friendId)
		for f in friends_friends:
			if f not in friends and f not in friends_user and f != user :
				cnt[f] = len(mutual_friend(user, f))
				friends.append(cnt)
	return cnt

print(friends_of_friends(3))
