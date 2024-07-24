from ninja import NinjaAPI

api = NinjaAPI()

api.add_router("/tasks/", "tasks.api.router")
api.add_router("/users/", "users.api.router")