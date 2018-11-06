import json
##from model import Books, Authors, Publishers

book_data = json.load(open('books.json'))
print(book_data)


publishers2 = []
key = 0
for line in book_data:
    try:
        id = book_data[key]['google_id']
        title = book_data[key]['title']
        isbn = book_data[key]['isbn']
        pub_date = book_data[key]['publication_date']
        image_url = book_data[key]['image_url']
        description = book_data[key]['description']
        publishers = book_data[key]['publishers']
        authors = book_data[key]['authors']
##        for line2 in publishers:
##            try:
##                founded = publishers[key2]['founded']
##            except NameError:
##                pass
    except KeyError:
        pass
    key += 1

print(publishers)

key2 = 0
for line2 in publishers:
    try:
        founded = publishers[key2]['founded']
        name = publishers[key2]['name']
        location = publishers[key2]['location']
        wiki = publishers[key2]['wikipedia_url']
        description2 = publishers[key2]['description']
        company = publishers[key2]['parent company']
        website = publishers[key2]['website']
    except KeyError:
        pass
    key2 += 1
    print(founded)
    print(name)
    print(location)
    print(wiki)

key3 = 0
for line3 in authors:
    try:
        born = authors[key3]['born']
        name = authors[key3]['name']
        nationality = authors[key3]['nationality']
        description3 = authors[key3]['description']
        alma = authors[key3]['alma_mater']
        wiki2 = authors[key3]['wikipedia_url']
        image = authors[key3]['image_url']
        

##first_dict_idx = 0
##while first_dict_idx < len(book_data):
##    first_author_number = book_data[first_dict_idx]['google_id']
##    first_author_number2 = book_data[first_dict_idx]['title']
##    first_author_number3 = book_data[first_dict_idx]['isbn']
##    first_author_number4 = book_data[first_dict_idx]['publication_date']
##    first_author_number5 = book_data[first_dict_idx]['image_url']
##    first_author_number6 = book_data[first_dict_idx]['description']
##    first_dict_idx += 1
    



##for key in info:
##    key = 0
##    for info in book_data:
##        id = book_data['google_id']
##        title = book_data[key]['title']
##        isbn = book_data[key]['isbn']
##        pub_date = book_data[key]['publication_date']
##        image_url = book_data[key]['image_url']
##        description = book_data[key]['description']
##    print(id)
##

    

    
##def get_obj(row):
##    return {
##        'id' : row.id,