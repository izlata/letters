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
            self.dao.create_author(new_author)

    def update_author(self, author_id, author):
        assert author_id is not None, "author_id should not be None"
        self.dao.update_author(author_id, author)
