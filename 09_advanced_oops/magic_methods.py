# Magic Methods in Python

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __str__(self):
        return f"Book has {self.pages} pages"

book = Book(200)
print(book)
