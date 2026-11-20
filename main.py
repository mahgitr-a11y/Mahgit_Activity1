class Greeter:
    def greet(self):
        print("Hello! Welcome to Python OOP!")

# Create an object
person = Greeter()

# Call the method
person.greet()

class Car:
    wheels = 4

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometers = 0

    def drive(self, km):
        if km > 0:
            self.kilometers += km
            print(f"{self.model} drove {km} km.")
        else:
            print("Invalid distance!")

    def age(self, year):
        return year - self.year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

car1 = Car("Toyota", "Vios", 2022)
car2 = Car("Honda", "Civic", 2023)
car3 = Car("Mitsubishi", "Mirage", 2021)

print("\nCAR METHODS")

car1.drive(50)
car1.drive(30)

print("Car:", car1)
print("Total kilometers:", car1.kilometers)
print("Car age:", car1.age(2026), "years")

class LibraryBook:
    counter = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False
        LibraryBook.counter += 1
    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is already borrowed.")
    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")
    def __str__(self):
        status = "Borrowed" if self.borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return f"LibraryBook('{self.title}', '{self.author}')"

book1 = LibraryBook("Harry Potter", "J.K. Rowling")
book2 = LibraryBook("The Little Prince", "Antoine de Saint-Exupery")
book3 = LibraryBook("Noli Me Tangere", "Jose Rizal")

print("\nLIBRARY BOOK SYSTEM")

print(book1)
print(book2)
print(book3)

book1.borrow()
book2.borrow()

print("\nAFTER BORROWING:")
print(book1)
print(book2)

book1.return_book()

print("\nAFTER RETURNING:")
print(book1)

print("\nTOTAL BOOKS:", LibraryBook.counter)

print("\nBOOK REPRESENTATION:")
print(repr(book1))