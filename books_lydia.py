import json
##from model import Books, Authors, Publishers

book_data = json.load(open('books.json'))
hi=0
##for i in book_data:
##	if len(i["authors"])>1:
##		print(i["authors"]["name"])
##print(hi)

for i in book_data:
	for j in range(len(i["authors"])):
		if i["authors"][j]["name"] == "Steven Levitt":
			born = i["authors"][j]["born"]
print(born)


##print(book_data)

