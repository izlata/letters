class ObjectAlreadyExistsError(Exception):
    def __init__(self, message="Object already exists"):
        super().__init__(message)
