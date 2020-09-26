import re

text = "RegEx  1234 566 76 76can be used to check ___Rakib___if a string contains the specified search pattern.Python has a built-in package called re, which can be used to work with Regular Expressions Re Rrakx."

# data = re.compile(r"^R.*?x")
data = re.compile(r"[A-Z]+")

result = data.finditer(text)
for i in result:
	print(i)


# result = data.findall(text)
# print(result)


# result = data.search(text)
# print(result)

