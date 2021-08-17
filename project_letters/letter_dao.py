from exceptions import ObjectAlreadyExistsError


class LetterDao():
    def __init__(self, letters=dict()):
        self.letters = letters

    def get_letter(self, letter_id):
        return self.letters[letter_id]

    def create_letter(self, new_letter):
        if new_letter in self.letters.values():
            raise ObjectAlreadyExistsError
        else:
            new_id = len(self.letters) + 1
            new_letter.letter_id = new_id
            self.letters[new_id] = new_letter
