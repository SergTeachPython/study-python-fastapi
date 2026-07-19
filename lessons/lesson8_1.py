import random

source_words = ["good", "interesting", "cool", "amazing", "fine"]

COMMENT_LENGTH = 3

result_words = [source_words[random.randint(0, len(source_words) - 1)] for i in range(COMMENT_LENGTH)]

final_comment = "This film is very " + ", ".join(result_words) + " ☺"

print(final_comment)
