from author import Author

class AuthorDao():
    def __init__ (self, authors=dict()):
        self.authors = authors

    def get_all_names(self):
        names_list = []
        for i in self.authors.values():
            names_list.append(i.name)
        return names_list

    def get_author(self, author_id):
        if author_id in self.authors.keys():
            author = self.authors[author_id]
            return author
        else:
            print("author_id does not exist")

    def create_author(self, name, info=None, photo=None, link=None):
        names_list = self.get_all_names()
        if name in names_list:
            print("Author already exists")
        else:
            new_id = len(self.authors) + 1
            new_author = Author(new_id, name, info, photo, link)
            self.authors[new_id] = new_author

        

    
