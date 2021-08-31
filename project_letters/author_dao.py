from project_letters.exceptions import ObjectAlreadyExistsError


class AuthorDao():
    def __init__(self, authors=dict()):
        self.authors = authors

    def get_author(self, author_id):
        return self.authors[author_id]

    def create_author(self, author):
        if author in self.authors.values():
            raise ObjectAlreadyExistsError
        else:
            new_id = len(self.authors) + 1
            author.author_id = new_id
            self.authors[new_id] = author

    def update_author(self, author_id, author):
        for key, value in self.authors.items():
            if author == value and author_id != key:
                raise ObjectAlreadyExistsError
        author.author_id = author_id
        self.authors[author_id] = author

    def save_author(self, author, author_id=None):
        if author_id is None:
            self.create_author(author)
        else:
            self.update_author(author_id, author)
