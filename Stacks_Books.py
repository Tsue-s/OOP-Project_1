from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    @abstractmethod
    def description(self):
        pass

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price:.2f}"

# Genre classes
class Fiction(Book):
    def description(self):
        return "A work of fiction"

class NonFiction(Book):
    def description(self):
        return "A non-fiction book"

class SciFi(Fiction):
    def description(self):
        return "A science fiction novel"

class Fantasy(Fiction):
    def description(self):
        return "A fantasy novel"

class Romance(Fiction):
    def description(self):
        return "A romance novel"

class Biography(NonFiction):
    def description(self):
        return "A biography"

# Sub Book classes
class Dune(SciFi):
    def __init__(self):
        super().__init__("Dune", "Frank Herbert", 15.99)

class Hyperion(SciFi):
    def __init__(self):
        super().__init__("Hyperion", "Dan Simmons", 12.99)

class Foundation(SciFi):
    def __init__(self):
        super().__init__("Foundation", "Isaac Asimov", 14.99)

class DoAndroidsDreamOfElectricSheep(SciFi):
    def __init__(self):
        super().__init__("Do Androids Dream of Electric Sheep?", "Philip K. Dick", 13.99)

class LordOfTheRings(Fantasy):
    def __init__(self):
        super().__init__("The Lord of the Rings", "J.R.R. Tolkien", 19.99)

class TheHobbit(Fantasy):
    def __init__(self):
        super().__init__("The Hobbit", "J.R.R. Tolkien", 16.99)

class TheWheelOfTime(Fantasy):
    def __init__(self):
        super().__init__("The Wheel of Time", "Robert Jordan", 18.99)

class PrideAndPrejudice(Romance):
    def __init__(self):
        super().__init__("Pride and Prejudice", "Jane Austen", 10.99)

class JaneEyre(Romance):
    def __init__(self):
        super().__init__("Jane Eyre", "Charlotte Brontë", 12.99)

class WutheringHeights(Romance):
    def __init__(self):
        super().__init__("Wuthering Heights", "Emily Brontë", 11.99)

class SteveJobs(Biography):
    def __init__(self):
        super().__init__("Steve Jobs", "Walter Isaacson", 14.99)

class AlbertEinstein(Biography):
    def __init__(self):
        super().__init__("Albert Einstein", "Walter Isaacson", 15.99)

class MarieCurie(Biography):
    def __init__(self):
        super().__init__("Marie Curie", "Susan Quinn", 13.99)

# store class
class BookStore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print(f"***Welcome to {self.name}!***\n")
        print("Available books sorted by genre:\n")
        for i, book in enumerate(self.books, 1):  # numbering
            print(f"{i}. {book}")
            print("  ", book.description())
            print()

# Creating the book store and adding books
store = BookStore("Stacks Books")
store.add_book(Dune())
store.add_book(Hyperion())
store.add_book(Foundation())
store.add_book(DoAndroidsDreamOfElectricSheep())
store.add_book(LordOfTheRings())
store.add_book(TheHobbit())
store.add_book(TheWheelOfTime())
store.add_book(PrideAndPrejudice())
store.add_book(JaneEyre())
store.add_book(WutheringHeights())
store.add_book(SteveJobs())
store.add_book(AlbertEinstein())
store.add_book(MarieCurie())

# Output
store.list_books()

# Test 
try:
    
    fiction = Fiction("Test Fiction", "Test Author", 10.99)
    assert fiction.description() == "A work of fiction"
except TypeError as e:
    print(f"Error creating Fiction object: {e}")


try:
    
    scifi = SciFi("Test SciFi", "Test Author", 10.99)
    assert scifi.description() == "A science fiction novel"
except TypeError as e:
    print(f"Error creating SciFi object: {e}")


try:
    store = BookStore("Test Book Store")
    assert store.name == "Test Book Store"
    assert store.books == []

    
    book1 = Fiction("Test Book 1", "Test Author 1", 10.99) 
    book2 = NonFiction("Test Book 2", "Test Author 2", 12.99)
    store.add_book(book1)
    store.add_book(book2)
    assert len(store.books) == 2
    assert book1 in store.books
    assert book2 in store.books
except TypeError as e:
    print(f"Error creating BookStore object: {e}")

print("Press any key to exit...")
input(">>> ")
print("Goodbye!")