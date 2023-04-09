from models.book import *


book1 = Book(1, "The Book Thief", "Markus Zusak", "Young Adult")
book2 = Book(2, "Nineteen Eighty-Four", "George Orwell", "Science Fiction")
book3 = Book(3, "The Very Hungry Caterpillar", "Eric Carle", "Childrens Book")
book4 = Book(4, "The Autobiography of Malcolm X", "Alex Haley", "Autobiography")

books = [book1, book2, book3, book4]

def find_book_by_title(title):
    for book in books:
        if book.title== title:
            return book
    return None


def find_book(id):
    for book in books:
        if book.id== id:
            return book
    return None

def add_new_book(book):
    books.append(book)

def book_to_remove(book_title):
    book_to_checkout = None
    for book in books:
        if book_title== book_title:
            book_to_checkout = book
            break

    books.remove(book_to_checkout)