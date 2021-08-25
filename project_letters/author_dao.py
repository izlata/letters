from project_letters.exceptions import ObjectAlreadyExistsError


class AuthorDao():
    def __init__(self, authors=dict()):
        self.authors = authors

    def get_author(self, author_id):
        return self.authors[author_id]

    def save_author(self, author, author_id=None):
        if author_id is None:  # create author
            if author in self.authors.values():
                raise ObjectAlreadyExistsError
            else:
                new_id = len(self.authors) + 1
                author.author_id = new_id
                self.authors[new_id] = author
        else:  # update author
            dict_copy = self.authors.copy()
            del dict_copy[author_id]
            if author in dict_copy.values():
                raise ObjectAlreadyExistsError
            else:
                author.author_id = author_id
                self.authors[author_id] = author
