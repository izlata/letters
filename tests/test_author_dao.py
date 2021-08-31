from project_letters.author import Author
from project_letters.author_dao import AuthorDao
from project_letters.exceptions import ObjectAlreadyExistsError

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
        self.dao.create_author(Author(None, 'C C', date(2000, 2, 2)))
        updated_dict = {1: Author(1, 'A A', date(1980, 12, 20)),
                        2: Author(2, 'B B', date(1990, 1, 15)),
                        3: Author(3, 'C C', date(2000, 2, 2))}
        self.assertEqual(self.dao.authors, updated_dict)

    def test_create_author_existing_record(self):
        with self.assertRaises(ObjectAlreadyExistsError):
            self.dao.create_author(Author(None, 'A A', date(1980, 12, 20)))

    def test_update_author(self):
        self.dao.update_author(2, Author(2, 'B C', date(1990, 1, 15), info='Journalist'))
        updated_dict = {1: Author(1, 'A A', date(1980, 12, 20)),
                        2: Author(2, 'B C', date(1990, 1, 15), info='Journalist')}
        self.assertEqual(self.dao.authors, updated_dict)

    def test_update_author_error(self):
        with self.assertRaises(ObjectAlreadyExistsError):
            self.dao.update_author(2, Author(2, 'A A', date(1980, 12, 20)))

    def test_save_author_create(self):
        self.dao.save_author(author=Author(None, 'C C', date(2000, 2, 2)))
        updated_dict = {1: Author(1, 'A A', date(1980, 12, 20)),
                        2: Author(2, 'B B', date(1990, 1, 15)),
                        3: Author(3, 'C C', date(2000, 2, 2))}
        self.assertEqual(self.dao.authors, updated_dict)

    def test_save_author_update(self):
        self.dao.save_author(author_id=2, author=Author(2, 'B C', date(1990, 1, 15), info='Journalist'))
        updated_dict = {1: Author(1, 'A A', date(1980, 12, 20)),
                        2: Author(2, 'B C', date(1990, 1, 15), info='Journalist')}
        self.assertEqual(self.dao.authors, updated_dict)
