class Letter():
    def __init__(self, letter_id, author_id, content, date=None, source=None):
        self.letter_id = letter_id
        self.author_id = author_id
        self.date = date
        self.content = content
        self.source = source

    def __eq__(self, other):
        return isinstance(other, Letter) and \
            self.author_id == other.author_id and \
            self.content == other.content
