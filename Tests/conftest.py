import pytest

from main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book

