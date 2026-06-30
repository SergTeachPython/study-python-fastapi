# import time
#
#
# i = 12
#
# while True:
#     print(i)
#     i += 2
#     time.sleep(1)
#
# i = 0
#
# while True:
#
#     if i == 2:
#         i += 1
#         continue
#
#     if i > 5:
#         print("break ...")
#         break
#
#     print(i)
#     i += 1

while True:
    rating = int(input("Enter your rating from 1 to 3 (0 for exit: "))

    if rating == 0:
        print("Exit...")
        break

    if rating < 1 or rating > 3:
        print("Your rating must be between 1 and 3")
        continue

    match rating:
        case 1:
            print("Bad rating")
        case 2:
            print("Normal rating")
        case 3:
            print("Excellent rating")

