from ninja import NinjaAPI
from ninja.security import HttpBearer

from utils import ServiceUnavailableError

class GlobalAuth(HttpBearer):
    def authenticate(self, request, token):
        if token == "supersecret":
            return token

api = NinjaAPI(title="Documentação Todo app", auth = GlobalAuth())

api.add_router("/tasks/", "tasks.api.router")
api.add_router("/auth/", "auth.api.router")

@api.exception_handler(ServiceUnavailableError)
def service_unavailable(request, excp):
    return api.create_response(
        request,
        {'message': "Please retry later, service unavailable"},
        status=503
    )
