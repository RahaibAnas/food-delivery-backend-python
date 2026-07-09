from services.auth_service import AuthService
from models.owner import Owner

class AuthController:
    def __init__(self,authService:AuthService):
        self.service = authService


    def login(self,email,password):
        try:
            return self.service.login(email,password)
        except ValueError as e:
            print(e)

    def register(self,owner:Owner):
        try:
            return self.service.register(owner)
        except ValueError as e:
            print(e)

    def logout(self):
        try:
            self.service.logout()
        except ValueError as e:
            print(e)

    def current_user(self):
        try:
            return self.service.get_current_user()
        except ValueError as e:
            print(e)
