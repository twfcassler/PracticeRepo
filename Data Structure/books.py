# books = ["Book 1", "Book 2", "Book 3"]

# books.append("Book 4")
# books.insert(0, "Book 0")
# books.pop(2)

# for book in books:
#     print(book)

# print(books.index("Book 1"))

# # When you update a string, it allocates new memory
# # book = "The Lightning Thief"
# # print(id(book))
# # book = "Another Book Title"
# # print(id(book))

# #Tuple
# #Like a list, but immutable
# classicBooks = ("The Great Gatsby", "The Catcher in the Rye", "To Kill a Mockingbird")

# #Sets
# #Like a list, but does not allow duplicates
# authors = {"Rick Riordan", "J.K Rowling", "JRR Tolkien"}
# authors.add("J.K Rowling")
# print(authors)

# #Dictionary
# #Key-Value Data Structure
# authorNumBooks = {
#     "Jane Austen": 6, 
#     "Charlotte Bronte": 4, 
#     "Emily Bronte": 2, 
# }

# authorNumBooks["Mark Twain"] = 28

# print(authorNumBooks)

books = {}

for count in range(0, 3):
    books[count] = input("What is the author name? ")

print(books)



booksByAuthors = {
    "Brandon Sanderson": ["TWOK", "WOR"]
}

print(booksByAuthors["Brandon Sanderson"])

bookQueue = []

for i in range(0, 3):
    bookQueue.append(input("Enter book name: "))

while len(bookQueue) > 0:
    print(bookQueue[0])
    print(bookQueue)
    bookQueue.pop(0)