class CourseNotFoundError(Exception):
    pass


class ResourceNotFoundError(Exception):
    pass

class CourseCreationError(Exception):
    pass

class CourseUpdateError(Exception):
    pass

class CourseDeleteError(Exception):
    pass

class DatabaseOperationError(Exception):
    pass

class CourseReadError(Exception):
    pass