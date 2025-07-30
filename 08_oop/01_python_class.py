# Class in Python
class Book:
  def __init__(self, title, author, pages):
    self.title = title
    self.author = author
    self.pages = pages
    self.__edition = 1  # Private attribute

  def book_info(self):
    return f"'{self.title}' by {self.author}, {self.pages} pages"
  
  def update_edition(self, new_edition):
    self.__edition = new_edition
  
  def get_edition(self):
    return self.__edition
  
  @classmethod
  def from_string(cls, book_string):
    title, author, pages = book_string.split(", ")
    return cls(title, author, int(pages))
  
  @staticmethod
  def is_valid_page_count(pages):
    return isinstance(pages, int) and pages > 0
    
# Create an instance of the Book class
my_book = Book("1984", "George Orwell", 328)

# Print the book information
print(my_book.book_info()) # Output: '1984' by George Orwell, 328 pages
  
# Type and IsInstance checks
print(type(my_book))  # Output: <class '__main__.Book'>
print(isinstance(my_book, Book))  # Output: True

# Create a book from a string
book_string = "To Kill a Mockingbird, Harper Lee, 281"
new_book = Book.from_string(book_string)
print(new_book.book_info())  # Output: 'To Kill a Mockingbird' by Harper Lee, 281 pages

# Check if the page count is valid
print(Book.is_valid_page_count(281))  # Output: True
print(Book.is_valid_page_count(-5))  # Output: False

# Example of using the private attribute
print(f"Edition: {my_book.get_edition()}")  # Output: Edition: 1
my_book.update_edition(2)
print(f"Updated Edition: {my_book.get_edition()}")  # Output: Updated Edition: 2
