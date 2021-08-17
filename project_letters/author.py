class Author():
    def __init__(self, author_id, name, dob=None, info=None, photo=None, link=None):
        self.author_id = author_id
        self.name = name
        self.dob = dob
        self.info = info
        self.photo = photo
        self.link = link

    def __eq__(self, other):
        return isinstance(other, Author) and \
            self.name == other.name and \
            self.dob == other.dob
