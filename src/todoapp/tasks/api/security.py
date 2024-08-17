from ninja.security import HttpBasicAuth


class Auth(HttpBasicAuth):
    def authenticate(self, request, username, password):

        if username == "admin" and password == "<PASSWORD>":
            return username