from ninja import NinjaAPI
from utils import ServiceUnavailableError

api = NinjaAPI(title="Documentação Todo app")

api.add_router("/tasks/", "tasks.api.router")
api.add_router("/users/", "users.api.router")

@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, excp):
    return api.create_response(
        request,
        {'message': "Please retry later, service unavailable"},
        status=503
    )
