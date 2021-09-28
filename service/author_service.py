from project_letters.exceptions import ObjectAlreadyExistsError


class AuthorService():
    def __init__(self, dao):
        self.dao = dao

    def get_author(self, author_id):
        return self.dao.get_author(author_id)

    def activate_author(self, new_author):
        if new_author in self.dao.authors.values():
            raise ObjectAlreadyExistsError
        else:
            new_author.active = True
            return new_author

    def save_author(self, author, author_id=None):
        if author_id is None:
            new_author = self.activate_author(author)
            self.dao.create_author(new_author)
        else:
            self.dao.update_author(author_id, author)
