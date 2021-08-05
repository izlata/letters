from author import Author
from exceptions import ObjectAlreadyExistsError

class AuthorDao():
    def __init__ (self, authors=dict()):
        self.authors = authors

    def get_author(self, author_id):
        author = self.authors[author_id]
        return author

    def create_author(self, new_author):
        if new_author in self.authors.values():
            raise ObjectAlreadyExistsError
        else:
            new_id = len(self.authors) + 1
            self.authors[new_id] = new_author
  

    
