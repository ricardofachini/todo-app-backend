from ninja import Schema


class TaskRequestEntity(Schema):
    """
    Schema entity (data class) for tasks in api requests
    """

    title: str
    description: str
    is_completed: bool = False


class TaskResponseEntity(Schema):
    """
    Schema entity (data class) for tasks in api responses
    """
    id: int
    title: str
    description: str
    is_completed: bool
