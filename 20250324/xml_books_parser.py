import xml.etree.ElementTree as ET
#get parsed data
tree = ET.parse("books.xml")
#get root and print
root = tree.getroot()
print("Root element:", root.tag)
#interate all elements with tag 'book'
for book in root.findall('book'):
    #1.get attribute 'id'
    book_id = book.get('id')
    #2.get value for tag 'title', 'author', 'year'
    title = book.find('title').text
    author = book.find('author').text
    year =  book.find('year').text
    #3. get value for tag 'publisher/name, 
    publisher_name = book.find('publisher/name').text
    publisher_city=  book.find('publisher/address/city').text
    publisher_zip=  book.find('publisher/address/zip').text

    #4. print
    print(f'Book ID: {book_id}')
    print('Title:', title)
    print('Author: {0:s}'.format(author))
    print(f'Year: {year}')
    print(f'Publisher: {publisher_name}')
    print(f'Adress: {publisher_city}, {publisher_zip}')
