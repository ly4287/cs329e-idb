import json
##from model import Books, Authors, Publishers

book_data = json.load(open('books.json'))

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
    except KeyError:
        pass
    key += 1
    print(publishers)
    break

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
        
      
