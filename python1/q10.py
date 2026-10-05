# # 6. Classes & Methods:
# Create a class Library that allows you to:

# 1.Add books (title and author).

# 2.Display all books.

# 3.Search for a book by title

class Library:
    def __init__(self):
        self.book=[]
    def add_book(self,title,author):
        self.book.append([title,author])

    def display(self):
        for books in self.book:
            print("title",books[0])
            print("author",books[1])
            print()

    def search(self,title):
        for books in self.book:
            if books[0].lower() == title.lower():
                print("Book found")
                print("Title:", books[0])
                print("Author:", books[1])
                return
        print("Book not found")
l1=Library()
l1.add_book("story of football","sabu")
l1.add_book("story of cricket","abu")
l1.add_book("Harry Potter", "J.K. Rowling")
l1.display()
l1.search("Harry Potter")