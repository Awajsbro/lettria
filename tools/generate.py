import os

FILE = "/mnt/g/--Code_42--/try/ressource/table"

file = open(FILE, "w")
str = "tree3 = [\n"
for i in range(97,123) :
	str += "\t[\t#{}\n".format(chr(i))
	for j in range(97,123) :
		str += "\t\t[\t#{}{}\n".format(chr(i), chr(j))
		for k in range(97,123) :
			str += "\t\t\t[\t#{}{}{}\n\t\t\t],\n".format(chr(i), chr(j), chr(k))

		str += "\t\t],\n"

	str += "\t],\n"

str += "]\n\ntree2 = [\n"
for i in range(97,123) :
	str += "\t[\t#{}\n".format(chr(i))
	for j in range(97,123) :
		str += "\t\t[\t#{}{}\n\t\t],\n".format(chr(i), chr(j))

	str += "\t],\n"

str += "]\n\ntree1 = [\n"
for i in range(97,123) :
	str += "\t[\t#{}\n\t],\n".format(chr(i))

str += "]\n"

file.write(str)
file.close
# print(str)

# https://code.tutsplus.com/fr/tutorials/introducing-the-natural-language-toolkit-nltk--cms-28620
# natural language toolkit
