class Author():
    def __init__(self, author_id, name, info, photo, link):
        self.author_id = author_id
        self.name = name
        self.info = info
        self.photo = photo
        self.link = link

    def __eq__(self, other):
        return isinstance(other, Author) and \
            self.author_id == other.author_id and \
            self.name == other.name and \
            self.info == other.info and \
            self.photo == other.photo and \
            self.link == other.link
