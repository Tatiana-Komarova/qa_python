from main import BooksCollector
import pytest
class TestBooksCollector:

    @pytest.mark.parametrize('title', ['J', 'Книга о книге, которой нет, но должна бы', 'Истории о Шерлоке'])
    def test_add_new_book_with_valid_name(self, book, title):
        book.add_new_book(title)
        assert title in book.get_books_genre()
        assert book.get_books_genre()[title] == ''

    @pytest.mark.parametrize('title', ['', 'Книга о книге, которой нет, но должна быть'])
    def test_add_new_book_with_invalid_name(self, book, title):
        book.add_new_book(title)
        books = book.get_books_genre()
        assert title not in books

    def test_add_the_same_book_twice(self, book):
        book.add_new_book('Война миров')
        book.add_new_book('Война миров')
        assert len(book.books_genre) == 1

    def test_set_book_genre(self, book):
        book.add_new_book('Война миров')
        book.set_book_genre('Война миров', 'Фантастика')
        assert book.get_book_genre('Война миров') == 'Фантастика'

    def test_get_book_genre(self, book):
        book.add_new_book('Зомби в городе')
        book.set_book_genre('Зомби в городе', 'Ужасы')
        book_genre = book.get_book_genre('Зомби в городе')
        assert book_genre == 'Ужасы'

    def test_get_books_with_specific_genre(self, book):
        book.add_new_book('Люди и пришельцы')
        book.add_new_book('Война миров')
        book.set_book_genre('Люди и пришельцы', 'Фантастика')
        book.set_book_genre('Война миров', 'Фантастика')
        books = book.get_books_with_specific_genre('Фантастика')
        assert 'Люди и пришельцы' in books
        assert 'Война миров' in books

    def test_get_books_for_children(self, book):
        children_books = ['Летучий корабль', 'Колобок']
        adult_books = ['Зомби в городе', 'Истории о шерлоке']
        for books in children_books + adult_books:
            book.add_new_book(books)

        book.set_book_genre('Летучий корабль', 'Мультфильмы')
        book.set_book_genre('Колобок', 'Комедии')
        book.set_book_genre('Зомби в городе', 'Ужасы')
        book.set_book_genre('Истории о Шерлоке', 'Детективы')

        result = book.get_books_for_children()
        for books in children_books:
            assert books in result
        for books in adult_books:
            assert books not in result


    def test_add_book_in_favorites(self, book):
        book.add_new_book('Война миров')
        book.add_book_in_favorites('Война миров')
        favorite_books = book.get_list_of_favorites_books()
        assert 'Война миров' in favorite_books

    def test_delete_book_from_favorites(self, book):
        book.add_new_book('Зомби в городе')
        book.add_book_in_favorites('Зомби в городе')
        favorite_books = book.get_list_of_favorites_books()
        book.delete_book_from_favorites('Зомби в городе')
        assert 'Зомби в городе' not in favorite_books

    def test_get_list_of_favorities_books(self, book):
        book.add_new_book('Летучий корабль')
        book.add_book_in_favorites('Летучий корабль')
        favorite_books = book.get_list_of_favorites_books()
        assert 'Летучий корабль' in favorite_books

