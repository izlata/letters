from author import Author
from author_dao import AuthorDao
from exceptions import ObjectAlreadyExistsError

import unittest
from datetime import date


class TestAuthorDao(unittest.TestCase):
    def test_get_author(self):
        author_dao = AuthorDao(authors={1: Author(1, 'A A', date(1980, 12, 20)),
                                        2: Author(2, 'B B', date(1990, 1, 15))})
        self.assertEqual(author_dao.get_author(1), Author(1, 'A A', date(1980, 12, 20)))
        self.assertEqual(author_dao.get_author(2), Author(2, 'B B', date(1990, 1, 15)))
        with self.assertRaises(KeyError):
            author_dao.get_author(5)

    def test_create_author(self):
        author_dao = AuthorDao(authors={1: Author(1, 'A A', date(1980, 12, 20))})
        author_dao.create_author(Author(0, 'B B', date(1990, 1, 15)))
        self.assertEqual(author_dao.authors,
                         {1: Author(1, 'A A', date(1980, 12, 20)), 2: Author(2, 'B B', date(1990, 1, 15))})
        with self.assertRaises(ObjectAlreadyExistsError):
            author_dao.create_author(Author(0, 'A A', date(1980, 12, 20)))
