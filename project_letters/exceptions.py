class ObjectAlreadyExistsError(Exception):
    def __init__(self, message="Object already exists"):
        self.message = message
        super().__init__(self.message)

