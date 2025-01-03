class Library:
    """this is class library"""
    
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def showBooks(self):
        print(f'There are {self.no_of_books} books which are \n')
        for book in self.books:
            print(book)

    def check(self):
        # print(len(self.books))
        # print(self.books)
        if self.no_of_books == len(self.books):
            print("Books and there number is equal")
        else:
            print('Books and there numbers are not equal')


library1 = Library()
no_of_books = int(input("Enter number of books:"))
while True:
    book = input('Enter the book:')
    library1.add(book)
    ch = input("Would you like to add another book (Y/N):")
    if ch != 'Y' and ch != 'y':
        break
print()
library1.showBooks()
print()
library1.check()