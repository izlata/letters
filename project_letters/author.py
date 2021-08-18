class Author():
    def __init__(self, author_id, name, dob=None, info=None, photo=None, link=None):
        self.author_id = author_id
        self.name = name
        self.dob = dob
        self.info = info
        self.photo = photo
        self.link = link

    def __eq__(self, other):
        is_instance_author = isinstance(other, Author)
        is_same_name = self.name == other.name
        is_same_dob = self.dob == other.dob
        return is_instance_author and is_same_name and is_same_dob
