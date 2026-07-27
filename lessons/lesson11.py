import re

result = re.findall(r'@\w+.(\w+)', "test1@gmail.com, test2@qqq.ua, test3@www.com")
print(result)
