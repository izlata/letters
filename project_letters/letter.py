class Letter():
    def __init__(self, letter_id, author_id, content, date=None, source=None):
        self.letter_id = letter_id
        self.author_id = author_id
        self.date = date
        self.content = content
        self.source = source

    def __eq__(self, other):
        is_instance_letter = isinstance(other, Letter)
        is_same_author_id = self.author_id == other.author_id
        is_same_content = self.content == other.content
        return is_instance_letter and is_same_author_id and is_same_content
