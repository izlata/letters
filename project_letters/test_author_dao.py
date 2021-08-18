from author import Author
from author_dao import AuthorDao
from exceptions import ObjectAlreadyExistsError

import unittest
from datetime import date


class TestAuthorDao(unittest.TestCase):
    def setUp(self):
        self.dao = AuthorDao(authors={1: Author(1, 'A A', date(1980, 12, 20)),
                                      2: Author(2, 'B B', date(1990, 1, 15))})

    def test_get_author_existing_key(self):
        self.assertEqual(self.dao.get_author(1), Author(1, 'A A', date(1980, 12, 20)))
        self.assertEqual(self.dao.get_author(2), Author(2, 'B B', date(1990, 1, 15)))

    def test_get_author_wrong_key(self):
        with self.assertRaises(KeyError):
            self.dao.get_author(5)

    def test_create_author_new_record(self):
        self.dao.create_author(Author(0, 'C C', date(2000, 2, 2)))
        updated_dict = {1: Author(1, 'A A', date(1980, 12, 20)),
                        2: Author(2, 'B B', date(1990, 1, 15)),
                        3: Author(3, 'C C', date(2000, 2, 2))}
        self.assertEqual(self.dao.authors, updated_dict)

    def test_create_author_existing_record(self):
        with self.assertRaises(ObjectAlreadyExistsError):
            self.dao.create_author(Author(0, 'A A', date(1980, 12, 20)))
