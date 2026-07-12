users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

# print(users["+11111111"])
# print(users["+33333333"])
# print(users["+55555555"])
#
# print(users.get("+111111119", "key not found"))
# deleted_value = users.pop("+555555551", "key not exist")
#
# print(deleted_value)
# print(users)
#
# users.clear()
# print(users)

#json
users =  {
    "Vasya": {"phone": "123123",
              "email": "qwerty@gmail.com",
              "hobbies": ["one", "two", "three"]
    },
    "Petya": {"phone": "134555",
             "email": "asdffgadsg@gmil.com",
              "hobby": "sport",
              "add_data": {
                  1: "test-1",
                  2: "test-2"
              }
    }
}
# print(users["Vasya"]["hobbies"][1])
# print(users["Petya"]["add_data"][2])
#
# print(users.get("Vasya").get("hobbies")[1])
# print(users.get("Petya").get("add_data")[2])

key = input("Enter key ").strip().lower()
for curr_key in users.keys():
    if curr_key.lower() == key:
        print(users[curr_key])
        break
else:
    print("Nothing found")