import json

book_data = json.load(open('books.json'))

book_ids = {}

first_dict_idx = 3
while first_dict_idx < 10:
    first_author_number = book_data[first_dict_idx]['google_id']
    first_author_number2 = book_data[first_dict_idx]['title']
    first_author_number3 = book_data[first_dict_idx]['isbn']
    first_author_number4 = book_data[first_dict_idx]['publication_date']
    first_author_number5 = book_data[first_dict_idx]['image_url']
    first_author_number6 = book_data[first_dict_idx]['description']
    first_dict_idx += 1
    

print(first_author_number)
print(first_author_number2)
print(first_author_number3)
print(first_author_number4)
print(first_author_number5)
print(first_author_number6)



##for key in book_data:
##    info = book_data[key]
##    for book_data in book:
##        format_book = book_ids(
##            id = info['google_id'],
##            title = info['title'],
##            isbn = info['isbn'],
##            pub_date = info['publication_date'],
##            image_url = info['image_url'],
##        description = info['description'])
##    session.merge(format_book)

##print(format_book)
    

    
##def get_obj(row):
##    return {
##        'id' : row.id,
        
      
