'''
Create a Library class with no_of_books as two instance variables. Write a program to create
a library from this Library class and show how you can print all books, add a book and get the 
number of books using different methods. Show that your program doesn't persist the books after 
the program is stopped!
'''

class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.noBooks = len(self.books) 
    
    def showInfo(self):
        print("The library has",self.noBooks, "books. The books are :")
        for book in self.books:
            print(book)

l1 = Library()       # type: ignore
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.showInfo()