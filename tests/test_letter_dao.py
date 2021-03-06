from project_letters.letter import Letter
from project_letters.letter_dao import LetterDao
from project_letters.exceptions import ObjectAlreadyExistsError

import unittest


class TestLetterDao(unittest.TestCase):
    def setUp(self):
        self.dao = LetterDao(letters={1: Letter(letter_id=1, author_id=3, content='Hello'),
                                      2: Letter(letter_id=2, author_id=3, content='ABCD')})

    def test_get_letter_existing_key(self):
        self.assertEqual(self.dao.get_letter(1), Letter(1, 3, 'Hello'))

    def test_get_letter_wrong_key(self):
        with self.assertRaises(KeyError):
            self.dao.get_letter(5)

    def test_create_letter_new_record(self):
        self.dao.create_letter(Letter(letter_id=None, author_id=3, content='Thank you'))
        updated_dict = {1: Letter(1, 3, 'Hello'),
                        2: Letter(2, 3, 'ABCD'),
                        3: Letter(3, 3, 'Thank you')}
        self.assertEqual(self.dao.letters, updated_dict)

    def test_create_letter_existing_record(self):
        with self.assertRaises(ObjectAlreadyExistsError):
            self.dao.create_letter(Letter(letter_id=None, author_id=3, content='Hello'))

    def test_update_letter(self):
        self.dao.update_letter(2, Letter(letter_id=2, author_id=3, content='ABCDEF', source='NN'))
        updated_dict = {1: Letter(letter_id=1, author_id=3, content='Hello'),
                        2: Letter(letter_id=2, author_id=3, content='ABCDEF', source='NN')}
        self.assertEqual(self.dao.letters, updated_dict)

    def test_update_letter_error(self):
        with self.assertRaises(ObjectAlreadyExistsError):
            self.dao.update_letter(2, Letter(letter_id=2, author_id=3, content='Hello'))

    def test_save_letter_create(self):
        self.dao.save_letter(letter=Letter(letter_id=None, author_id=3, content='Thank you'))
        updated_dict = {1: Letter(1, 3, 'Hello'),
                        2: Letter(2, 3, 'ABCD'),
                        3: Letter(3, 3, 'Thank you')}
        self.assertEqual(self.dao.letters, updated_dict)

    def test_save_letter_update(self):
        self.dao.save_letter(letter_id=2, letter=Letter(letter_id=2, author_id=3, content='ABCDEF'))
        updated_dict = {1: Letter(letter_id=1, author_id=3, content='Hello'),
                        2: Letter(letter_id=2, author_id=3, content='ABCDEF')}
        self.assertEqual(self.dao.letters, updated_dict)
