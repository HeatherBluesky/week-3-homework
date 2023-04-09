from flask import render_template, request, redirect, url_for
from app import app
from models.books import books, add_new_book, find_book_by_title, book_to_remove, find_book
from models.book import *



@app.route('/')
def index():
   return redirect(url_for('all_books'))

@app.route('/books')
def all_books():
   return render_template('index.html', title = 'Home', book_list = books)

@app.route('/books/<int:id>')
def see_book(id):
   book = find_book(id)
   return render_template('show.html', title="chosen book:", book=book)
   # return redirect(url_for('see_book', id=book.id))

# @app.route('/books/title/<title>')
# def view_book(book):
#    book = find_book_by_title(book)
#    render_template('show.html', title="Book", book=book)


@app.route('/books', methods=['POST'])
def add_book():
  id = len(books) +1
  title = request.form['title']
  author = request.form['author']
  genre = request.form['genre']
  new_book = Book(id = id, title= title, author=author, genre=genre)
  add_new_book(new_book)



  return render_template('index.html', title='books', book_list=books)


@app.route('/books/delete/<title>', methods=['POST'])
def delete(book):
  book_to_remove(book)
  return redirect('/books')
