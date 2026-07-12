# users = {"Tom", "Bob", "Alice", "Tom"}
# print(users)
# print(type(users))
#
# people = ["Mike", "Bill", "Ted"]
# users = set(people)
# print(users)

# user = "Tom"
#
# if user in users:
#     users.remove(user)
# print(users)
#
# users.discard("Tom") # елемент "Tom" відсутній, і метод нічого не робить
# print(users)
#
# users.clear()
# print(users)

users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)

users4 = users.intersection(users2)
print(users4)

#альтернатива
print(users & users2)

# users.intersection_update(users2)
# print(users)

users3 = users.difference(users2)
print(users3)

print(users - users2)

# users.difference_update(users2)
# print(users)

users3 = users.symmetric_difference(users2)
print(users3)

users4 = users ^ users2
print(users4)

users = {"Tom", "Bob", "Alice"}
superusers = {"Tom", "Sam", "Kate", "Bob", "Alice", "Greg"}

print(users.issubset(superusers))
print(superusers.issuperset(users))