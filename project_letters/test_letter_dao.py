from letter import Letter
from letter_dao import LetterDao
from exceptions import ObjectAlreadyExistsError

import unittest


class TestLetterDao(unittest.TestCase):
    def test_get_letter(self):
        letter_dao = LetterDao(letters={1: Letter(1, 3, 'Hello'), 2: Letter(2, 1, 'ABCD')})
        self.assertEqual(letter_dao.get_letter(1), Letter(1, 3, 'Hello'))
        with self.assertRaises(KeyError):
            letter_dao.get_letter(5)

    def test_create_letter(self):
        letter_dao = LetterDao(letters={1: Letter(letter_id=1, author_id=3, content='Hello')})
        letter_dao.create_letter(Letter(letter_id=0, author_id=3, content='ABCD'))
        self.assertEqual(letter_dao.letters, {1: Letter(1, 3, 'Hello'), 2: Letter(2, 3, 'ABCD')})
        with self.assertRaises(ObjectAlreadyExistsError):
            letter_dao.create_letter(Letter(letter_id=0, author_id=3, content='Hello'))
