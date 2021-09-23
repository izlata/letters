from project_letters.exceptions import ObjectAlreadyExistsError


class LetterDao():
    def __init__(self, letters=dict()):
        self.letters = letters

    def get_letter(self, letter_id):
        return self.letters[letter_id]

    def create_letter(self, letter):
        if letter in self.letters.values():
            raise ObjectAlreadyExistsError
        else:
            new_id = len(self.letters) + 1
            letter.letter_id = new_id
            self.letters[new_id] = letter

    def update_letter(self, letter_id, letter):
        for key, value in self.letters.items():
            if letter == value and letter_id != key:
                raise ObjectAlreadyExistsError
        # letter.letter_id = letter_id
        self.letters[letter_id] = letter

    def save_letter(self, letter, letter_id=None):
        if letter_id is None:
            self.create_letter(letter)
        else:
            self.update_letter(letter_id, letter)
