class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


book1 = Book("1984", "George Orwell", 1949)

book2 = Book("Alchemist", "Paulo Coelho", 1988)

print("1-kitob:")
print(book1.title, book1.author, book1.year)

print("\n2-kitob:")
print(book2.title, book2.author, book2.year)