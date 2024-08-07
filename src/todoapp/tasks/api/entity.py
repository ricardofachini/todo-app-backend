from ninja import Schema

class TaskRequestSchema(Schema):
    """
    Schema entity (data class) for tasks in api requests
    """

    title: str
    description: str
    is_completed: bool = False